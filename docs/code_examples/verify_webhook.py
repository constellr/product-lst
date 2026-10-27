"""
Receive and verify constellr webhooks with a minimal FastAPI server.

Webhooks are signed following the Standard Webhooks specification
(https://www.standardwebhooks.com/). The `verify_webhook` function below has no
third-party dependencies and can be dropped into any framework; only the HTTP
server around it uses FastAPI.

Before running:
    - Set `WEBHOOK_SECRET` to your endpoint's signing secret (starts with `whsec_`).
    - Expose the server through HTTPS (e.g. a reverse proxy or a tunnel such as
      ngrok) and register that HTTPS URL as your webhook endpoint.

Run:
    pip install fastapi uvicorn
    uvicorn verify_webhook:app --port 8000
"""

import base64
import hashlib
import hmac
import json
import time

from fastapi import FastAPI, HTTPException, Request, Response

WEBHOOK_SECRET = "whsec_lab8Cj/bkYzuNNLaTvNf8mTodgKf32eMRrrmEo+Tac0="
TOLERANCE_SECONDS = 5 * 60

if WEBHOOK_SECRET == "whsec_YOUR_SIGNING_SECRET":
    raise RuntimeError("Set WEBHOOK_SECRET to your endpoint's real signing secret before running this script.")

app = FastAPI()

# Delivery is *at least once*: track processed event ids to skip duplicates.
# Use a persistent store instead of memory in production.
seen_event_ids: set[str] = set()


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
    # Standard Webhooks sends the message id, timestamp and signature(s) in these headers.
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

    # Recompute the HMAC over "{id}.{timestamp}.{body}" using the shared secret.
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


@app.post("/webhooks/constellr")
async def receive_webhook(request: Request):
    # Read the raw body: re-serialized JSON would not match the signature.
    body = await request.body()

    try:
        event = verify_webhook(WEBHOOK_SECRET, request.headers, body)
    except WebhookVerificationError as error:
        raise HTTPException(status_code=400, detail=str(error))

    # Delivery is at least once: the event id (same as the webhook-id header)
    # lets you recognize and skip a duplicate delivery of the same event.
    if event["id"] in seen_event_ids:
        return Response(status_code=204)
    seen_event_ids.add(event["id"])

    # Respond quickly; move heavy processing (e.g. downloads) to a background job.
    print(f"Received {event['type']} ({event['id']}): {event['data']}")
    return Response(status_code=204)
