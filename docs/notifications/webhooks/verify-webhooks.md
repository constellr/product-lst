# **Verifying Webhooks**

Your webhook URL is public, so anyone could send requests to it. Every webhook we send is signed with your endpoint's **signing secret**, so you can confirm that it came from constellr and that its content wasn't modified.

Our signatures follow the [Standard Webhooks](https://www.standardwebhooks.com/) specification. You can use any Standard Webhooks library, or verify the signature yourself as described below.

!!! tip "Example script"
    A minimal FastAPI example that verifies signatures without any third-party verification library is available here: [verify_webhook.py](https://github.com/constellr/product-lst/blob/main/docs/code_examples/verify_webhook.py)

---

## Signature headers

Each request includes three headers:

| Header | Example | Description |
| :--- | :--- | :--- |
| `webhook-id` | `9a4e7c12-2f8b-4d6a-8c3e-1b5f0d9a7e28` | Unique event ID. Same across retries. |
| `webhook-timestamp` | `1792748530` | Unix timestamp (seconds) of this delivery attempt. |
| `webhook-signature` | `v1,K5oZfzN95Z9UVu1EsfQmfVNQhnkZ2pj9o9NDN/H/pI4=` | One or more space-separated signatures. |

---

## How to verify a request

1. **Read the raw request body.** Sign the exact bytes you received. Parsing and re-serializing the JSON can change it and break the signature.
2. **Check the timestamp.** Reject requests whose `webhook-timestamp` is more than **5 minutes** away from your current time. This limits how long a captured, validly-signed request could be resent to your endpoint later (a replay attack).
3. **Build the signed content** by joining the ID, the timestamp and the raw body with a dot:

    ```
    {webhook-id}.{webhook-timestamp}.{body}
    ```

4. **Compute the expected signature.**
    * Remove the `whsec_` prefix from your signing secret and **base64-decode** the rest. The result is the key.
    * Compute an **HMAC-SHA256** of the signed content using that key.
    * **Base64-encode** the result.
5. **Compare signatures.** The `webhook-signature` header contains one or more space-separated entries in the form `v1,<signature>` — more than one appears only during a [secret rotation](#rotating-the-signing-secret). The request is valid if **any** `v1` entry matches your expected signature. Use a constant-time comparison.

If verification fails, respond with `400` and ignore the request.

### Handling duplicate webhooks

A valid signature and timestamp only prove a request is genuine and recent — not that you haven't seen it before. The same event can be [retried](retries.md), and a captured, validly-signed request can still be replayed within the timestamp tolerance. Make your endpoint **idempotent**: processing the same event twice shouldn't repeat its side effects.

Use the `webhook-id` header as an idempotency key:

1. After verifying the signature, check whether you've already processed this `webhook-id`.
2. If you have, return a `2xx` without repeating the processing.
3. If you haven't, process the event and store the `webhook-id` in persistent storage, so duplicates are caught across retries and restarts.

!!! note
    The timestamp check limits how long a request can be replayed; deduplication stops it from being processed twice. You need both.

---

## Rotating the signing secret

Rotate your signing secret regularly, or immediately if you believe it has been exposed. You can rotate it on the [Webhooks page](https://app.constellr.com/account/webhooks) or via the API (`POST /webhook-endpoints/{id}/rotate-secret`, see [Swagger](https://api.constellr.com/docs) or [ReDoc](https://api.constellr.com/redoc)).

The response contains the new `secret` (shown **only once**), `secret_rotated_at` and, if there is an overlap, `previous_secret_expires_at`.

| `overlap_hours` | Behavior | Use when |
| :--- | :--- | :--- |
| `24` (default) | For 24 hours, every request is signed with **both** the new and the previous secret, so `webhook-signature` contains two entries. | Routine rotation. Gives you time to deploy the new secret without missing events. |
| `0` | The previous secret stops working immediately. | The secret may have been compromised. |

Because a request is valid if **any** signature matches, your server keeps accepting webhooks during the overlap whether it uses the old or the new secret.

---

## Additional security tips

* Keep your signing secret out of source control; store it in a secret manager or environment variable.
* Only accept requests over HTTPS (we never send webhooks to `http://` URLs).
* Treat the payload as a notification: for critical decisions, fetch the latest data from our API using the IDs in the event.
