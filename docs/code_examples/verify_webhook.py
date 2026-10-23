"""
Receive and verify constellr webhooks without any third-party library.

Webhooks are signed following the Standard Webhooks specification
(https://www.standardwebhooks.com/). This script starts a small HTTP server
that verifies the signature of every incoming request and prints the event.

Before running:
    - Set `WEBHOOK_SECRET` to your endpoint's signing secret (starts with `whsec_`).
    - Expose the server through HTTPS (e.g. a reverse proxy or a tunnel such as
      ngrok) and register that HTTPS URL as your webhook endpoint.

Run:
    python verify_webhook.py
"""

import base64
import hashlib
import hmac
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

WEBHOOK_SECRET = "whsec_YOUR_SIGNING_SECRET"
TOLERANCE_SECONDS = 5 * 60
PORT = 8000


class WebhookVerificationError(Exception):
    pass


def verify_webhook(secret: str, headers, body: bytes) -> dict:
    """
    Verify a webhook request and return the parsed event.

    Args:
        secret: The endpoint's signing secret, including the `whsec_` prefix.
        headers: The request headers (any mapping with `.items()`).
        body: The raw request body, exactly as received.

    Raises:
        WebhookVerificationError: If the request is not a valid constellr webhook.
    """
    headers = {key.lower(): value for key, value in headers.items()}
    msg_id = headers.get("webhook-id")
    msg_timestamp = headers.get("webhook-timestamp")
    msg_signatures = headers.get("webhook-signature")
    if not (msg_id and msg_timestamp and msg_signatures):
        raise WebhookVerificationError("Missing webhook headers")

    # Reject old or future-dated requests to prevent replay attacks.
    try:
        timestamp = int(msg_timestamp)
    except ValueError:
        raise WebhookVerificationError("Invalid webhook-timestamp header")
    if abs(time.time() - timestamp) > TOLERANCE_SECONDS:
        raise WebhookVerificationError("Timestamp outside the tolerance window")

    key = base64.b64decode(secret.removeprefix("whsec_"))
    signed_content = f"{msg_id}.{msg_timestamp}.".encode() + body
    expected = base64.b64encode(
        hmac.new(key, signed_content, hashlib.sha256).digest()
    ).decode()

    # During a secret rotation the header holds several space-separated
    # signatures; the request is valid if any of them matches.
    for versioned_signature in msg_signatures.split(" "):
        version, _, signature = versioned_signature.partition(",")
        if version == "v1" and hmac.compare_digest(signature, expected):
            return json.loads(body)

    raise WebhookVerificationError("No matching signature")


class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the raw body: re-serialized JSON would not match the signature.
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))

        try:
            event = verify_webhook(WEBHOOK_SECRET, self.headers, body)
        except WebhookVerificationError as error:
            print(f"Rejected webhook: {error}")
            self.send_response(400)
            self.end_headers()
            return

        # Respond quickly; move heavy processing (e.g. downloads) to a background job.
        # Use event["id"] to skip events you have already processed.
        print(f"Received {event['type']} ({event['id']}): {event['data']}")
        self.send_response(204)
        self.end_headers()


if __name__ == "__main__":
    print(f"Listening for webhooks on http://localhost:{PORT}")
    HTTPServer(("", PORT), WebhookHandler).serve_forever()
