# **Event Types**

Every webhook request contains a JSON body describing a single event. All events share the same envelope; the `data` object depends on the event type.

| Event type | Sent when |
| :--- | :--- |
| [`order.validated`](#ordervalidated) | An order has been validated by a constellr CSM and its state moves to `in_progress`. |
| [`order.rejected`](#orderrejected) | An order has been rejected during validation. |
| [`order.closed`](#orderclosed) | An order is complete and moves to `closed` state. |
| [`delivery.published`](#deliverypublished) | A new delivery for an order is available to download. |

---

## Event envelope

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | string (UUID) | Unique event ID. Identical to the `webhook-id` header and the same across retries; use it to detect duplicates. |
| `version` | integer | Payload schema version. Currently `1`. |
| `type` | string | The event type, e.g. `order.validated`. |
| `timestamp` | string (ISO 8601, UTC) | When the event happened. |
| `data` | object | Event-specific data, see below. |

## Request headers

| Header | Description |
| :--- | :--- |
| `content-type` | `application/json` |
| `user-agent` | `Constellr-Webhooks/1.0` |
| `webhook-id` | The event `id`. |
| `webhook-timestamp` | Unix timestamp (seconds) of this delivery attempt. |
| `webhook-signature` | Signature used to [verify the request](verify-webhooks.md). |

---

## `order.validated`

The order has been reviewed by constellr and is now active. The system is working to acquire and deliver images.

| Field | Type | Description |
| :--- | :--- | :--- |
| `data.order_id` | string (UUID) | The order ID. |
| `data.state` | string | The new order state: `in_progress`. |

```json
{
  "id": "0c8e4a3f-6b1d-4f2a-9e7c-3d5b8a1f2e64",
  "version": 1,
  "type": "order.validated",
  "timestamp": "2026-10-22T09:15:00Z",
  "data": {
    "order_id": "a1003715-03fa-4433-9ef0-db9b836f160c",
    "state": "in_progress"
  }
}
```

## `order.rejected`

The order has been reviewed by constellr and rejected.

| Field | Type | Description |
| :--- | :--- | :--- |
| `data.order_id` | string (UUID) | The order ID. |
| `data.state` | string | The new order state: `rejected`. |
| `data.rejection_reason` | string | Why the order was rejected. |

```json
{
  "id": "3f6c1e2a-8b1d-4c1e-9f0a-2d7c5b9e1a44",
  "version": 1,
  "type": "order.rejected",
  "timestamp": "2026-10-22T09:15:00Z",
  "data": {
    "order_id": "a1003715-03fa-4433-9ef0-db9b836f160c",
    "state": "rejected",
    "rejection_reason": "Area of interest outside the coverage area"
  }
}
```

## `order.closed`

The order is complete and all of its data has been delivered.

| Field | Type | Description |
| :--- | :--- | :--- |
| `data.order_id` | string (UUID) | The order ID. |
| `data.state` | string | The new order state: `closed`. |

```json
{
  "id": "7d2b9f41-5c3e-4a8d-b1f6-9e0c2a7d4b13",
  "version": 1,
  "type": "order.closed",
  "timestamp": "2026-12-01T00:05:00Z",
  "data": {
    "order_id": "a1003715-03fa-4433-9ef0-db9b836f160c",
    "state": "closed"
  }
}
```

## `delivery.published`

A new delivery is available. Use `stac_item_id` and `stac_collection` to fetch the item and download its assets from the [STAC API](../../API-documentation.md#stac-api).

| Field | Type | Description |
| :--- | :--- | :--- |
| `data.order_id` | string (UUID) | The order the delivery belongs to. |
| `data.stac_item_id` | string | ID of the STAC item for this delivery. |
| `data.stac_collection` | string | STAC collection containing the item, e.g. `lstprecision`. |
| `data.acquisition_datetime` | string (ISO 8601, UTC) | When the image was acquired by the satellite. |

```json
{
  "id": "9a4e7c12-2f8b-4d6a-8c3e-1b5f0d9a7e28",
  "version": 1,
  "type": "delivery.published",
  "timestamp": "2026-10-23T11:42:10Z",
  "data": {
    "order_id": "a1003715-03fa-4433-9ef0-db9b836f160c",
    "stac_item_id": "lstprecision_20261023_101407_field_a12",
    "stac_collection": "lstprecision",
    "acquisition_datetime": "2026-10-23T10:14:07Z"
  }
}
```

!!! tip "Fetching the delivery"
    `GET https://api.constellr.com/stac/collections/{stac_collection}/items/{stac_item_id}` returns the item with pre-signed download URLs for its assets.
