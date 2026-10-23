# **Webhooks**

Webhooks let your systems react to your orders in real time. Instead of repeatedly polling our API to check whether something has changed, you register a URL and we send an HTTP `POST` request to it the moment an event happens, for example when an order is validated or a new delivery is published.

Typical uses:

* Alert your own customers as soon as a new delivery is available.
* Automatically download new data via the [STAC API](../../API-documentation.md#stac-api).
* Keep order statuses in your own systems in sync with ours.

---

## How it works

1. You register a **webhook endpoint**: an HTTPS URL on your server and the [event types](event-types.md) you want to receive.
2. We give you a **signing secret** for that endpoint.
3. When a subscribed event happens on an order in your workspace, we send a JSON `POST` request to your URL.
4. Your server [verifies the signature](verify-webhooks.md) and responds with a `2xx` status code.
5. If your server doesn't respond with a `2xx`, we [retry](retries.md) on a fixed schedule.

Webhook endpoints are **workspace-scoped**: an endpoint receives events for all eligible orders in its workspace, regardless of who placed them. Webhooks are independent of [email notifications](../email-notifications.md).

---

## Quickstart

**1. Create an endpoint on your server**

Your endpoint must:

* Be reachable from the public internet over **HTTPS**.
* Accept `POST` requests with a JSON body.
* Respond with a `2xx` status code within **20 seconds**.

```python
# Minimal example using FastAPI
from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.post("/webhooks/constellr")
async def constellr_webhook(request: Request):
    event = await request.json()
    print(event["type"], event["data"])
    return Response(status_code=204)
```

For a complete, dependency-free example that also verifies the signature, see [verify_webhook.py](https://github.com/constellr/product-lst/blob/main/docs/code_examples/verify_webhook.py).

!!! tip "Testing locally"
    To receive webhooks on your own machine during development, expose your local server through an HTTPS tunnel (for example [ngrok](https://ngrok.com/)) and register the tunnel's URL.

**2. Register the endpoint**

=== "UI"

    1. Go to [Account > Workspace > Webhooks](https://app.constellr.com/account/webhooks).
    2. Click **Create Webhook** and enter your endpoint URL, the events to subscribe to and, optionally, a description.
    3. Copy the **signing secret** shown after creation.

    From the same page you can edit or delete an endpoint, rotate its signing secret, and view its delivery history in the **Events log**. See the [UI documentation](../../UI-documentation.md#webhooks) for a step-by-step guide with screenshots.

=== "API"

    ```bash
    curl -X POST https://api.constellr.com/webhook-endpoints \
      -H "X-Api-Key: $CONSTELLR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
            "url": "https://example.com/webhooks/constellr",
            "event_types": ["order.validated", "order.rejected", "order.closed", "delivery.published"],
            "description": "Production listener"
          }'
    ```

    Response (`201 Created`):

    ```json
    {
      "id": "5b3f8c2e-1d4a-4b7e-9c6f-2a8d0e1f3b47",
      "url": "https://example.com/webhooks/constellr",
      "event_types": ["order.validated", "order.rejected", "order.closed", "delivery.published"],
      "description": "Production listener",
      "created": "2026-10-22T09:00:00Z",
      "updated": "2026-10-22T09:00:00Z",
      "secret": "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw8m0p3Yq8L0E="
    }
    ```

!!! warning "The signing secret is shown only once"
    The `secret` is returned only when the endpoint is created (and when it is [rotated](verify-webhooks.md#rotating-the-signing-secret)). Store it securely right away; it can't be retrieved later.

**3. Verify incoming requests**

Use the signing secret to check that each request really comes from constellr and hasn't been tampered with. See [Verifying webhooks](verify-webhooks.md).

**4. Receive your first event**

Events are sent as orders progress. Place an order, or wait for the next validation or delivery on an existing order, and check the request arriving at your endpoint. You can review every delivery attempt, including your server's response, in the endpoint's [delivery history](#managing-endpoints) (`GET /webhook-endpoints/{id}/delivery-attempts`, also documented in [Swagger](https://api.constellr.com/docs) and [ReDoc](https://api.constellr.com/redoc)).

---

## Managing endpoints

All endpoints below require your workspace API key in the `X-Api-Key` header. For full schemas and error codes, see [Swagger](https://api.constellr.com/docs) or [ReDoc](https://api.constellr.com/redoc).

| Action | Request |
| :--- | :--- |
| Create an endpoint | `POST /webhook-endpoints` |
| List endpoints | `GET /webhook-endpoints` |
| Get an endpoint | `GET /webhook-endpoints/{id}` |
| Update URL, event types or description | `PATCH /webhook-endpoints/{id}` |
| Delete an endpoint | `DELETE /webhook-endpoints/{id}` |
| Rotate the signing secret | `POST /webhook-endpoints/{id}/rotate-secret` |
| View delivery history | `GET /webhook-endpoints/{id}/delivery-attempts` |

**Limits and rules**

* Up to **50** endpoints per workspace.
* Each URL can only be registered once per workspace.
* URLs must use `https://`, must not contain credentials (`user:password@`), and must resolve to a public address. Private, loopback and link-local addresses are rejected.
* Redirects are **not** followed. Register the final URL.

**Delivery history**

Each delivery attempt is recorded with the event payload, the attempt number, whether it succeeded, your server's response status code and body, and the request duration. Use it to debug failing deliveries.

---

## Best practices

* **Respond quickly.** Return a `2xx` as soon as you've received and verified the request, and do any heavy processing (e.g. downloading data) asynchronously. Requests time out after 20 seconds.
* **Always verify signatures** before trusting the payload. See [Verifying webhooks](verify-webhooks.md).
* **Handle duplicates.** Delivery is *at least once*, so the same event may arrive more than once. Use the `webhook-id` header (equal to the event `id`) to ignore events you've already processed.
* **Don't rely on ordering.** Events may arrive in a different order than they happened. Use the event `timestamp`, or fetch the latest order state from the [Orders API](../../API-documentation.md#orders-api), if order matters.
* **Subscribe only to what you need.** Each endpoint only receives the event types it's subscribed to.
