# **Constellr API Documentation**

This guide covers the concepts and workflows behind the Constellr API. It complements, but doesn't replace the full endpoint reference:

- **Interactive reference (Swagger):** [https://api.constellr.com/docs](https://api.constellr.com/docs)
- **Reference documentation (ReDoc):** [https://api.constellr.com/redoc](https://api.constellr.com/redoc)

For request/response schemas, field types, and status codes, always defer to Swagger/ReDoc.

**Base URL:** `https://api.constellr.com`

---

## Getting Started

Constellr's API and UI are invitation-only. To get access:

1. Get invited to a workspace by an existing member or your Constellr Customer Success Manager (CSM).
2. Follow the signup link in your invitation email and activate your account.
3. Generate a workspace-scoped API key from [Account → Workspace API Keys](https://app.constellr.com/account/workspace-api-keys). It's shown only once, so store it securely right away.

---

## Authentication

- Requests are authenticated with an API key in the `X-Api-Key` header.
- Keys are **workspace-scoped**, which means each key grants access to **exactly one workspace**.
- Keys expire after a certain time. Please check the expiration date when generating a key and rotate it before it expires.
- When a workspace member is removed or an account is deleted, API keys created by that member are revoked immediately.
- Legacy bearer-token auth (`POST /token`) only works for accounts in a single workspace; workspace-scoped API keys are the recommended approach going forward.


!!! warning "Legacy Bearer Token Authentication"
    Bearer token authentication (`POST /token`) continues to work only if your user account belongs to a **single workspace**. If your account is added to a second workspace, bearer token authentication will **stop working** and your requests will fail.
    To avoid disruption, switch to workspace-scoped API keys now. They explicitly target a specific workspace and keep working regardless of how many workspaces your account belongs to. Generate one at [https://app.constellr.com/account/workspace-api-keys](https://app.constellr.com/account/workspace-api-keys).

---

## End-to-End Workflow
Here is a typical, summarized workflow for requesting and downloading satellite-derived data:

1. **Authenticate:** Generate an API key for your workspace. Send your API key in the `X-Api-Key` header of every request.
2. **Create AOI:** Submit your GeoJSON to the AOIs API to get a reusable `AOI ID`.
3. **Place Order:** Submit a new order using the Orders API.
4. **Search STAC:** Query the STAC API to find the metadata and items for your order.
5. **Download:** Use the temporary pre-signed URLs in the STAC response to download your imagery.

---

## The APIs

### Orders API

Request satellite-derived data products (e.g., `LSTprecision`) for a given area and time window. An order ties together a **product**, an **Area of Interest (AOI)**, and a **schedule**. Orders can be created individually or in batch, listed, updated, and deleted.

**Order Lifecycle States**

You can track an order's lifecycle using its `state` property. Once created, an order progresses through four states:

| State | Description                                                                                                                                                                                                                                 |
| :--- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`pending_validation`** | The order has been submitted and is awaiting manual review/validation by Constellr Customer Success Managers (CSMs).                                                                                                                        |
| **`in_progress`** | The order is active and the system is working to acquire and deliver images to you.                                                                                                                                                         |
| **`closing`** | The order's monitoring period is over. The system is no longer trying to acquire new images. However, we are waiting for any last images taken by the satellite to be downlinked, processed and quality controlled before the order closes. |
| **`closed`** | The order is complete and all of your data has been delivered.                                                                                                                                                                              |

> **State Sequence:** `pending_validation` → `in_progress` → `closing` → `closed`

### Areas of Interest (AOI) API

Defines the geographic regions that orders are placed against. AOIs are created once from GeoJSON and can be reused across multiple orders.

### Products API

A simple lookup of which data products are available to your workspace. Useful as a pre-flight check before placing orders.

### STAC API

Once an order is fulfilled, the results are available through the standard [SpatioTemporal Asset Catalog (STAC)](https://stacspec.org/). Use the STAC API to search collections and items by area, time, order id or other filters, and download the resulting assets using pre-signed URLs.

*For endpoint-level details on any of the above (parameters, schemas, error codes etc.) see [Swagger](https://api.constellr.com/docs) or [ReDoc](https://api.constellr.com/redoc).*

---

## Examples

### Download data from STAC API

The STAC API provides metadata and temporary pre-signed URLs for accessing your ordered data products. These URLs can be used to download the available assets associated with an order.
A Python example script demonstrating how to download assets from the STAC API for a specific order is available here:
[download_assets_from_stac.py](<https://github.com/constellr/product-lst/blob/main/docs/code_examples/download_assets_from_stac.py>)