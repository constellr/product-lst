# **Retries**

A delivery is **successful** when your endpoint responds with any `2xx` status code within 20 seconds. If it doesn't, we retry the delivery on a fixed schedule.

---

## Retry schedule

Each event is attempted up to **6 times** in total: the first attempt plus 5 retries. Each delay is counted from the previous failed attempt.

| Attempt | Delay after previous attempt |
| :--- | :--- |
| 1 | Immediately |
| 2 | 5 seconds |
| 3 | 5 minutes |
| 4 | 30 minutes |
| 5 | 2 hours |
| 6 | 5 hours |

The last attempt happens roughly **7.5 hours** after the first one. If it also fails, the event is not delivered again.

---

## What is retried

| Outcome | Retried? |
| :--- | :--- |
| `2xx` response | No, delivery succeeded |
| Timeout (no response within 20 seconds) or connection error | Yes |
| `5xx` response | Yes |
| `408 Request Timeout`, `425 Too Early`, `429 Too Many Requests` | Yes |
| Any other `4xx` response | No |
| `3xx` redirect | No, redirects are not followed |

!!! tip
    Return a `4xx` (for example `400` for an invalid signature) only when retrying would not help. If your server is temporarily unavailable, return a `5xx` (e.g. `503`) so the event is retried.

---

## Good to know

* **Retries carry the same event.** The body and the `webhook-id` header stay the same on every attempt. The `webhook-timestamp` and `webhook-signature` headers are regenerated for each attempt.
* **Duplicates can happen.** Because delivery is *at least once*, you may occasionally receive an event you've already processed. Use the `webhook-id` to deduplicate.
* **Endpoints are never disabled automatically.** A failing endpoint keeps receiving new events.
* **Each endpoint is retried independently.** A failure on one endpoint doesn't affect deliveries to your other endpoints.
* **Check the delivery history** with `GET /webhook-endpoints/{id}/delivery-attempts` (or on the [Webhooks page](https://app.constellr.com/account/webhooks)) to see each attempt, its status code and your server's response.
* **Missed events?** If all attempts fail, use the [Orders API](../../API-documentation.md#orders-api) and [STAC API](../../API-documentation.md#stac-api) to catch up on order states and deliveries.
