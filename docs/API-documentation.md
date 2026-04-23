# **Constellr API Documentation**
 
This guide outlines how to authenticate, place orders, search, and download your data using the constellr API. For a detailed overview of the latest API, including live examples, refer to the [interactive Swagger documentation](https://api.constellr.com/docs) or [Redoc documentation](https://api.constellr.com/redoc).

## Base URL

All API endpoints use
```
https://api.constellr.com
```
---

## Initial Preparation

- **Access requirements:** The Constellr API and UI are invitation-only. You cannot sign up independently. You must be invited to a specific workspace by an existing member or a Constellr Customer Success Manager (CSM).

- **Create your account:** If you do not yet have a Constellr account, open the invitation email and follow the signup link. You will be asked to provide your email address and set a password.

- **Activate your account:** After registering, confirm your email address to activate your account.

- **Generate your API key:** Once your account is active, create a workspace-scoped API key in the Constellr UI by navigating to the Account page:
  [https://app.constellr.com/account/workspace-api-keys](https://app.constellr.com/account/workspace-api-keys)

  > **Security Note:** The full API key is returned **only once** during the creation process. It cannot be retrieved again. Please store it securely immediately.

---

## Authentication

- **Authentication Header:** All API requests must include your API key in the `X-Api-Key` header.

- **Workspace Scoping:** All API keys are workspace-scoped. The key is bound to a specific workspace and automatically sets the context for your requests. If you belong to multiple workspaces, you must use the key corresponding to the workspace you wish to access.

- **Security Best Practices:**
    - **No plaintext storage:** Never store API keys in plain text within your production code. Use environment variables or a secret management service.
    - **Automatic revocation:** When a member is removed from a workspace, or when a user account is deleted, all associated API keys are automatically revoked.
    - **Immediate effect:** Revocation takes effect immediately. Rotate keys promptly if you suspect a key has been compromised.


!!! warning "Legacy Bearer Token Authentication"
    Bearer token authentication (using `POST /token`) continues to work if your user account belongs to a **single workspace**. However, if your account is added to multiple workspaces, bearer token authentication will **stop working** and your requests will fail. For simplicity and to avoid confusion, this guide focuses on workspace-scoped API key authentication and does not document the legacy bearer-token flow.    

    To avoid disruptions, we recommend switching to workspace-scoped API keys now. API keys explicitly target a specific workspace and will continue to work regardless of how many workspaces your account belongs to.

    Generate your API key at: [https://app.constellr.com/account/workspace-api-keys](https://app.constellr.com/account/workspace-api-keys)
---


## Orders API

The `/orders` endpoint allows you to create, list, and retrieve orders for your workspace.

<h3>1. Create Orders in Batch</h3>

**Endpoint:** `POST /orders/batch`  
**Description:** Create multiple new orders for your workspace in a single request. <br />
**Order Validation:** All orders are validated upon submission. If any order is invalid, the entire request is rejected with a 400/404 status code and an error message. <br />

- **Order Limit**: Each `/orders/batch` request can contain a maximum of **25** orders per request.

- **Product Specific Validation**:<br />

| Feature | LSTprecision / LSTzoom | LSTfusion                                                                                         |
| :--- | :--- |:--------------------------------------------------------------------------------------------------|
| **AOI Limit** | Bounding box limit max **15,000m** x **15,000m** | Bounding box limit min **60 meters** x **60 meters**, max **110,000 meters** x **110,000 meters** |
| **Start Date** | Starting from today | No restriction                                                                                    |
| **Duration** | Min **7 days**, Max **1 year** | No restriction                                                                                    |
| **Frequency** | `single_image`, `max_frequency`, `once_every_two_weeks`, `monthly`, `weekly`. | `daily`                                                                                           |
| **Maximum Number Of Images** | when `frequency` is `single_image`, its value must be `1` | Not supported                                                                                     |

- **General Validation(All Products)**: <br />
    - Tags: <br />
        - Max 10 tags per order.
        - Each tag max length 50 characters.
        - No duplicate tags are allowed for the same order.
        - Tag entities are created if they do not already exist.
    - Illumination Constraint: <br />
        - Used to specify if imaging needs to take place during an astronomical day, night or either.
        - Options: `day`, `night`, or `null`
        - Default: `null`

**Request Body Example:**
```json
{
  "use_case": "Yield Prediction",
  "comment": "Urgent order for Q3 analysis",
  "orders": [
    {
      "area_of_interest_id": "1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770",
      "start_date": "2025-09-27T10:30:08.004000Z",
      "end_date": "2025-10-18T10:30:08.004000Z",
      "frequency": "single_image",
      "product_name": "LSTprecision",
      "comment": "Order for field 42",
      "tags": ["field42"],
      "illumination_constraint": "day",
      "maximum_number_of_images": 1
    }
  ]
}
```


**Example: cURL**
```sh
curl -X POST "https://api.constellr.com/orders/batch" \
  -H 'accept: application/json' \
  -H "X-Api-Key: <your_api_key>" \
  -H "Content-Type: application/json" \
  -d @order_payload.json
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/orders/batch"
headers = {
    "X-Api-Key": "<your_api_key>",
    "Content-Type": "application/json",
    "accept": "application/json"
}

payload = {
    "use_case": "Yield Prediction",
    "comment": "Urgent order for Q3 analysis",
    "orders": [
        {
            "area_of_interest_id": "1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770",
            "start_date": "2025-09-27T10:30:08.004000Z",
            "end_date": "2025-10-18T10:30:08.004000Z",
            "frequency": "single_image",
            "product_name": "LSTprecision",
            "comment": "Order for field 42",
            "tags": ["field42"],
            "illumination_constraint": "day",
            "maximum_number_of_images": 1
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```


**Response (201):**
```json
[
  {
    "area_of_interest_id": "1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770",
    "start_date": "2025-09-27T10:30:08.004000Z",
    "end_date": "2025-10-18T10:30:08.004000Z",
    "frequency": "single_image",
    "product_name": "LSTprecision",
    "comment": "Order for field 42",
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "created": "2025-08-27T11:54:24.206072Z",
    "state": "initial_state",
    "rejection_reason": null,
    "tags": [
      {
        "name": "field42",
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "created": "2025-11-28T10:05:36.362Z"
      }
    ],
    "illumination_constraint": "day",
    "maximum_number_of_images": 1
  }
]
```

**Error Responses:**

- **400:** Invalid order request body values.
- **401:** Invalid API key.
- **403:** User not authorized to create orders.
- **404:** Resource not found (e.g., AOI or product does not exist).
- **422:** Request body validation error (including when a customer order contains more than 25 data orders).
---

<h3>2. List All Orders</h3>

**Endpoint:** `GET /orders`  
**Description:** List all orders for your workspace with pagination and sorting.

**Query Parameters:**

- `limit` (optional, default: 10): Maximum number of orders to return.

- `offset` (optional, default: 0): Number of orders to skip.

- `sort` (optional): Sort orders by the `-created` field.


**Example: cURL**
```bash
curl -G "https://api.constellr.com/orders" \
  -H "X-Api-Key: <your_api_key>" \
  --data-urlencode "limit=10" \
  --data-urlencode "offset=0" \
  --data-urlencode "sort=-created"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/orders"
headers = {
    "X-Api-Key": "<your_api_key>"
}
params = {
    "limit": 10,
    "offset": 0,
    "sort": "-created"
}

resp = requests.get(url, headers=headers, params=params)
resp.raise_for_status()
data = resp.json()
print(data["count"], len(data["items"]))
```

**Response (200):**
```json
{
  "count": 1,
  "items": [
    {
      "area_of_interest_id": "1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770",
      "start_date": "2025-09-27T10:30:08.004000Z",
      "end_date": "2025-10-18T10:30:08.004000Z",
      "frequency": "single_image",
      "product_name": "LSTprecision",
      "comment": "Order for field 42",
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "created": "2025-08-27T11:54:24.206072Z",
      "state": "initial_state",
      "rejection_reason": null,
      "tags": [
        {
          "name": "field42",
          "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "created": "2025-11-28T10:05:36.362Z"
        }
      ],
      "illumination_constraint": "day",
      "maximum_number_of_images": 1
    }
  ]
}
```
**Error Responses:**

- **401:** Invalid API key.
- **403:** User not authorized to view orders.
- **422:** Query parameter validation error.

---

<h3>3. Get Order by ID</h3>

**Endpoint:** `GET /orders/{order_id}`  
**Description:** Retrieve a specific order by its unique ID.


**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/orders/123e4567-e89b-12d3-a456-426614174000" \
  -H "X-Api-Key: <your_api_key>"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/orders/123e4567-e89b-12d3-a456-426614174000"
headers = {
    "X-Api-Key": "<your_api_key>"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())

```

**Response (200):**
```json
{
  "area_of_interest_id": "1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770",
  "start_date": "2025-09-27T10:30:08.004000Z",
  "end_date": "2025-10-18T10:30:08.004000Z",
  "frequency": "single_image",
  "product_name": "LSTprecision",
  "comment": "Order for field 42",
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "created": "2025-08-27T11:54:24.206072Z",
  "state": "rejected",
  "rejection_reason": "AOI is outside of the supported coverage area.",
  "tags": [
      {
        "name": "field42",
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "created": "2025-11-28T10:05:36.362Z"
      }
  ],
  "illumination_constraint": "day",
  "maximum_number_of_images": 1
}
```
**Error Responses:**

- **401:** Invalid API key.
- **403:** User not authorized to view the order.
- **404:** Order not found.
- **422:** Request parameter validation error.

---

<h3>4. Partially Update Order by ID</h3>

**Endpoint:** `PATCH /orders/{order_id}`  
**Description:** Updates specific fields of an existing order.
The update operation is limited to certain fields as defined in the example request schema.
Only the fields provided in the request body will be updated; other fields will remain unchanged.

**Example: cURL**
```sh
curl -X 'PATCH' \
  'https://api.constellr.com/orders/b131326b-20ea-44ff-b589-231ea77a7456' \
  -H 'accept: application/json' \
  -H 'X-Api-Key: <your_api_key>' \
  -H 'Content-Type: application/json' \
  -d '{
  "tags": [
    "field42"
  ]
}'
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/orders/123e4567-e89b-12d3-a456-426614174000"
headers = {
    "X-Api-Key": "<your_api_key>",
    "Content-Type": "application/json",
    "accept": "application/json"
}

payload = {
    "tags": [
        "field42"
    ]
}
response = requests.patch(url, headers=headers, json=payload)

print(response.status_code)
print(response.json())

```

**Response (200):**
```json
{
  "area_of_interest_id": "1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770",
  "start_date": "2025-09-27T10:30:08.004000Z",
  "end_date": "2025-10-18T10:30:08.004000Z",
  "frequency": "single_image",
  "product_name": "LSTprecision",
  "comment": "Order for field 42",
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "created": "2025-08-27T11:54:24.206072Z",
  "state": "initial_state",
  "rejection_reason": null,
  "tags": [
      {
        "name": "field42",
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "created": "2025-11-28T10:05:36.362Z"
      }
  ],
  "illumination_constraint": "day",
  "maximum_number_of_images": 1
}
```
**Error Responses:**

- **401:** Invalid API key.
- **403:** User not authorized to update the order.
- **404:** Order not found.
- **422:** Request parameter validation error.

---

<h3>5. Delete Order by ID</h3>

**Endpoint:** `DELETE /orders/{order_id}`  
**Description:** Deletes an existing order. Only orders with status `pending_validation` or `rejected` can be deleted.

**Path Parameters**

- `order_id` (required, UUID): Unique ID of the order to delete.

**Example: cURL**
```sh
curl -X DELETE "https://api.constellr.com/orders/123e4567-e89b-12d3-a456-426614174000" \
  -H "X-Api-Key: <your_api_key>" \
  -H "accept: */*"
```

**Example: Python**
```python
import requests

order_id = "123e4567-e89b-12d3-a456-426614174000"
url = f"https://api.constellr.com/orders/{order_id}"
headers = {"X-Api-Key": "<your_api_key>"}

resp = requests.delete(url, headers=headers)
print(resp.status_code)
```

**Success Response (204)**

Order deleted successfully. No response body is returned.

**Error Responses:**

- **401:** Invalid API key.
- **403:** User not authorized to delete the order.
- **404:** Order not found.
- **409:** Order cannot be deleted in its current state. Only `pending_validation` or `rejected` orders can be deleted.

---

<h3>6. Get Available Order Use Cases</h3>

**Endpoint:** `GET /orders/meta/use-cases`  
**Description:**  Returns a list of available order use cases supported by the API.  

**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/orders/meta/use-cases" \
  -H "X-Api-Key: <your_api_key>"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/orders/meta/use-cases"
headers = {
    "X-Api-Key": "<your_api_key>"
}

response = requests.get(url, headers=headers)

print(response.status_code)
```

**Response (200):**
```json
[
  "Unknown",
  "Adoption of regenerative ag",
  "Algae/Bacteria bloom",
  "Cover crop monitoring",
  "Drought Stress",
  "Yield Prediction"
]
```

**Error Responses:**

- **401:** Invalid API key.
- **403:** User not authorized to view use cases.

---

## Areas of Interest API

The `/areas-of-interest` endpoint allows you to create, list, and retrieve Areas of Interest (AOIs) for your workspace. AOIs define geographic regions used in data orders.

<h3>1. Create an Area of Interest</h3>

**Endpoint:**  `POST /areas-of-interest`  
**Description:** Creates a new Area of Interest (AOI) for your workspace.

**Request Body Example**
```json
{
  "name": "Test AOI",
  "description": "Test area",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [8.68483, 49.885416],
        [8.684889, 49.876422],
        [8.670971, 49.876383],
        [8.67091, 49.885378],
        [8.68483, 49.885416]
      ]
    ]
  }
}
```

**Example: cURL**
```bash
curl -X POST "https://api.constellr.com/areas-of-interest" \
  -H "X-Api-Key: <your_api_key>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test AOI",
    "description": "Test area",
    "geometry": {
      "type": "Polygon",
      "coordinates": [
        [
          [8.68483, 49.885416],
          [8.684889, 49.876422],
          [8.670971, 49.876383],
          [8.67091, 49.885378],
          [8.68483, 49.885416]
        ]
      ]
    }
  }'
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/areas-of-interest"
headers = {
    "X-Api-Key": "<your_api_key>",
    "Content-Type": "application/json"
}
payload = {
    "name": "Test AOI",
    "description": "Test area",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [8.68483, 49.885416],
                [8.684889, 49.876422],
                [8.670971, 49.876383],
                [8.67091, 49.885378],
                [8.68483, 49.885416]
            ]
        ]
    }
}

resp = requests.post(url, headers=headers, json=payload)
resp.raise_for_status()
print(resp.json())
```


**Success Response (201)**
```json
{
  "name": "Test AOI",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [8.68483, 49.885416],
        [8.684889, 49.876422],
        [8.670971, 49.876383],
        [8.67091, 49.885378],
        [8.68483, 49.885416]
      ]
    ]
  },
  "description": "Test area",
  "bbox_width": 1200.1,
  "bbox_height": 1300.1,
  "id": "f1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770",
  "created": "2025-07-31T11:05:29.157539"
}
```


**Error Responses**

- **400:** Invalid AOI request body values.
- **401:** Invalid API key.
- **403:** User not authorized to create AOIs.
- **409:** An Area of Interest with this name already exists.
- **422:** Request body validation error.

---

<h3>2. Get an Area of Interest by ID</h3>

**Endpoint:**  `GET /areas-of-interest/{area_of_interest_id}`  
**Description:** Retrieves a specific AOI by its unique ID.

**Example: cURL**
```bash
curl -X GET "https://api.constellr.com/areas-of-interest/f1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770" \
  -H "X-Api-Key: <your_api_key>"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/areas-of-interest/f1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770"
headers = {
    "X-Api-Key": "<your_api_key>"
}

resp = requests.get(url, headers=headers)
resp.raise_for_status()
print(resp.json())
```

**Success Response (200)**
```json
{
  "name": "Test AOI",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [8.68483, 49.885416],
        [8.684889, 49.876422],
        [8.670971, 49.876383],
        [8.67091, 49.885378],
        [8.68483, 49.885416]
      ]
    ]
  },
  "description": "Test area",
  "bbox_width": 1200.1,
  "bbox_height": 1300.1,
  "id": "f1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770",
  "created": "2025-07-31T11:05:29.157539"
}
```

**Error Responses**

- **401:** Invalid API key.
- **403:** User not authorized to view the AOI.
- **404:** AOI not found.
- **422:** Request parameter validation error.

---

<h3>3. List Areas of Interest</h3>

**Endpoint:**  `GET /areas-of-interest`  
**Description:** Lists all AOIs for your workspace with pagination and sorting.

**Query Parameters**

- `limit` (optional, default: 10): Maximum number of items to return.

- `offset` (optional, default: 0): Zero-based index of the first item to return.

- `sort` (optional): Property to sort results by the `-created` field. Use `+` or `-` as a prefix for ascending or descending order.

**Example: cURL**
```bash
curl -G "https://api.constellr.com/areas-of-interest" \
  -H "X-Api-Key: <your_api_key>" \
  --data-urlencode "limit=10" \
  --data-urlencode "offset=0" \
  --data-urlencode "sort=-created"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/areas-of-interest"
headers = {"X-Api-Key": "<your_api_key>"}
params = {
    "limit": 10,
    "offset": 0,
    "sort": "-created"
}

resp = requests.get(url, headers=headers, params=params)
resp.raise_for_status()
data = resp.json()

print(f"Total AOIs: {data['count']}")
for item in data["items"]:
    print(item["id"], item["name"])
```

**Success Response (200)**
```json
{
  "count": 1,
  "items": [
    {
      "name": "Test AOI",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-8.558478, 40.317694],
            [-8.343601, 40.314150],
            [-8.365829, 40.186899],
            [-8.545914, 40.188510],
            [-8.558478, 40.317694]
          ]
        ]
      },
      "description": "Test area",
      "bbox_width": 1200.1,
      "bbox_height": 1300.1,
      "id": "f1c53eaaa-9b26-4c3d-8998-bfc8e9ac1770",
      "created": "2025-04-03T10:36:40.348842"
    }
  ]
}
```


**Error Responses**

- **401:** Invalid API key.
- **403:** User not authorized to view AOIs.
- **422:** Query parameter validation error.

---

<h3>4. Delete an Area of Interest by ID</h3>

**Endpoint:**  `DELETE /areas-of-interest/{area_of_interest_id}`  
**Description:** Deletes a specific Area of Interest (AOI) by its unique ID.

**Path Parameters**

- `area_of_interest_id` (required, UUID): Unique ID of the AOI to delete.

**Example: cURL**
```sh
curl -X DELETE "https://api.constellr.com/areas-of-interest/cd9a3472-5e4d-495c-bb3a-8cf0408b2a3d" \
  -H "X-Api-Key: <your_api_key>" \
  -H "accept: */*"
```

**Example: Python**
```python
import requests

area_of_interest_id = "cd9a3472-5e4d-495c-bb3a-8cf0408b2a3d"
url = f"https://api.constellr.com/areas-of-interest/{area_of_interest_id}"
headers = {"X-Api-Key": "<your_api_key>"}

resp = requests.delete(url, headers=headers)
print(resp.status_code)
```

**Success Response (204)**

Area of interest deleted successfully. No response body is returned.

**Error Responses**

- **401:** Invalid API key.
- **403:** Forbidden (AOI does not belong to the user's workspace or user is not authorized).
- **409:** Conflict (AOI has active orders and cannot be deleted).
- **404:** Area of interest not found.
- **422:** Request parameter validation error.

---

<h3>5. Get Geometry Info from AOI</h3>

**Endpoint:**  `POST /areas-of-interest/geometry-info`  
**Description:** Get geometry information (bounding box width/height, area) for a provided GeoJSON AOI geometry.

**Request Body Example**
```json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [11.053963, 51.690862],
        [11.976814, 51.690862],
        [11.976814, 51.059955],
        [10.944099, 51.073763],
        [11.053963, 51.690862]
      ]
    ]
  }
}
```

**Example: cURL**
```sh
curl -X POST "https://api.constellr.com/areas-of-interest/geometry-info" \
  -H "X-Api-Key: <your_api_key>" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "Feature",
    "geometry": {
      "type": "Polygon",
      "coordinates": [
        [
          [11.053963, 51.690862],
          [11.976814, 51.690862],
          [11.976814, 51.059955],
          [10.944099, 51.073763],
          [11.053963, 51.690862]
        ]
      ]
    }
  }'
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/areas-of-interest/geometry-info"
headers = {
    "X-Api-Key": "<your_api_key>",
    "Content-Type": "application/json",
}
payload = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [11.053963, 51.690862],
                [11.976814, 51.690862],
                [11.976814, 51.059955],
                [10.944099, 51.073763],
                [11.053963, 51.690862],
            ]
        ],
    },
}

resp = requests.post(url, headers=headers, json=payload)
resp.raise_for_status()
data = resp.json()

print(f"bbox_width: {data['bbox_width']}")
print(f"bbox_height: {data['bbox_height']}")
print(f"area: {data['area']}")
```


**Success Response (200)**
```json
{
  "bbox_width": 74218.0,
  "bbox_height": 72561.2,
  "area": 4728768008.0
}
```

**Error Responses**

- **400:** Invalid AOI geometry in request body.
- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.
- **422:** Request body validation error.

---

## Products API

The `/products` endpoint provides access to the list of available constellr products. Use it to explore product details before creating data orders.

<h3>1. List Available Products</h3>

**Endpoint:**  `GET /products`  
**Description:** Retrieves a list of available products for your workspace.


**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/products" \
  -H "X-Api-Key: <your_api_key>"
```

**Success Response (200)**

```json
[
  {"name": "LSTprecision"},
  {"name": "LSTfusion"}
]
```

**Error Responses**

- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.


## STAC API
The `/stac` endpoint provides access to SpatioTemporal Asset Catalog (STAC) API, allowing you to search and retrieve geospatial data in a standardized format.
The endpoints comply with the STAC API specification.

<h3>1. Get STAC Landing Page</h3>

**Endpoint:**  `GET /stac`  
**Description:** Fetches landing page data for the STAC Browser.

**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/stac" \
  -H "X-Api-Key: <your_api_key>"
```

**Success Response (200)**
```json
{
  "type": "Catalog",
  "id": "constellr-stacapi",
  "title": "Constellr STAC API",
  "description": "Constellr STAC API",
  "stac_version": "1.0.0",
  "links": [
    {
      "rel": "self",
      "type": "application/json",
      "title": "This document",
      "href": "https://api.constellr.com/stac/"
    },
    {
      "rel": "data",
      "type": "application/json",
      "title": "Collections available for this Catalog",
      "href": "https://api.constellr.com/stac/collections"
    }
  ],
  "stac_extensions": []
}
```

**Error Responses**

- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.

---

<h3>2. Get Conformance Classes</h3>

**Endpoint:**  `GET /stac/conformance`  
**Description:** Fetches the conformance classes supported by the STAC API.

**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/stac/conformance" \
  -H "X-Api-Key: <your_api_key>"
```

**Success Response (200)**
```json
{
  "conformsTo": [
    "http://www.opengis.net/spec/cql2/1.0/conf/basic-cql2",
    "http://www.opengis.net/spec/cql2/1.0/conf/cql2-json",
    "http://www.opengis.net/spec/cql2/1.0/conf/cql2-text",
    "https://api.stacspec.org/v1.0.0/ogcapi-features#sort"
  ]
}
```

**Error Responses**

- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.


---

<h3>3. List Available Collections</h3>

**Endpoint:**  `GET /stac/collections`  
**Description:** Fetches the available STAC collections for your workspace.

**Query Parameters (optional):**

- `limit`: Limits the number of results per page.

- `offset`: Number of items to skip before starting to collect the result set.

- `bbox`: Only return items intersecting this bounding box.

- `datetime`: Only return items with a temporal property intersecting this value.

- `sortby`: Array of property names to sort by, prefixed by `+` or `-`.

- `filter`: CQL filter expression for filtering items.

- `filter-lang`: The language used for the `filter` value (e.g., `cql2-json`).

**Example: cURL**
```sh
curl -G "https://api.constellr.com/stac/collections" \
  -H "X-Api-Key: <your_api_key>" \
  --data-urlencode "limit=5" \
  --data-urlencode "offset=0" \
  --data-urlencode "bbox=-122.1,5.1,35.4,53.6"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/stac/collections"
headers = {"X-Api-Key": "<your_api_key>"}
params = {
    "limit": 5,
    "offset": 0,
    "bbox": "-122.1,5.1,35.4,53.6"
}

resp = requests.get(url, headers=headers, params=params)
resp.raise_for_status()
data = resp.json()

for collection in data["collections"]:
    print(collection["id"], "-", collection["title"])
```


**Success Response (200)**
```json
{
  "collections": [
    {
      "id": "lstfusion",
      "type": "Collection",
      "links": [
        {
          "rel": "items",
          "href": "https://api.constellr.com/stac/collections/lstfusion/items"
        }
      ],
      "title": "LSTfusion Level-3 UTM LST Product",
      "extent": {
        "spatial": {"bbox": [[-122.1, 5.1, 35.4, 53.6]]},
        "temporal": {
          "interval": [["2015-02-26T17:00:00+00:00", "2025-08-18T11:00:00+00:00"]]
        }
      },
      "license": "other",
      "description": "Land Surface Temperature (LST) Fusion product.",
      "stac_version": "1.1.0"
    }
  ],
  "links": [
    {"rel": "root", "href": "https://api.constellr.com/stac/"}
  ],
  "numberMatched": 1,
  "numberReturned": 1
}
```

**Error Responses**

- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.
- **422:** Query parameter validation error.

---

<h3>4. Get a Single Collection</h3>

**Endpoint:**  `GET /stac/collections/{collection_id}`  
**Description:** Fetches a single STAC collection by its ID.


**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/stac/collections/lstfusion" \
  -H "X-Api-Key: <your_api_key>"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/stac/collections/lstfusion"

headers = {
    "X-Api-Key": "<your_api_key>"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())

```

**Success Response (200)**
```json
{
  "id": "lstfusion",
  "type": "Collection",
  "links": [
    {
      "rel": "items",
      "href": "https://api.constellr.com/stac/collections/lstfusion/items"
    },
    {
      "rel": "self",
      "href": "https://api.constellr.com/stac/collections/lstfusion"
    }
  ],
  "title": "LSTfusion Level-3 UTM LST Product",
  "extent": {
    "spatial": {"bbox": [[-122.1, 5.1, 35.4, 53.6]]},
    "temporal": {
      "interval": [["2015-02-26T17:00:00+00:00", "2025-08-18T11:00:00+00:00"]]
    }
  },
  "license": "other",
  "description": "Short description.",
  "stac_version": "1.1.0"
}
```

**Error Responses**

- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.
- **404:** Collection not found.
- **422:** Request parameter validation error.

---

<h3>5. Get a Single Item by Collection and Item ID</h3>

**Endpoint:**  `GET /stac/collections/{collection_id}/items/{item_id}`  
**Description:** Fetches a single STAC item(feature) by collection and item ID.


**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/stac/collections/lstfusion/items/item_id" \
  -H "X-Api-Key: <your_api_key>"
```

**Example: Python**
```python
import requests

collection_id = "lstfusion"
item_id = "item_id"
url = f"https://api.constellr.com/stac/collections/{collection_id}/items/{item_id}"
headers = {"X-Api-Key": "<your_api_key>"}

resp = requests.get(url, headers=headers)
resp.raise_for_status()
data = resp.json()

print(data["id"], "-", data["collection"])
```


**Success Response (200)**
```json
{
  "id": "item_id",
  "type": "Feature",
  "bbox": [8.3, 49.6, 9.0, 50.1],
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [8.3, 50.1],
        [8.3, 49.6],
        [9.0, 49.6],
        [9.0, 50.1],
        [8.3, 50.1]
      ]
    ]
  },
  "links": [
    {
      "rel": "collection",
      "href": "https://api.constellr.com/stac/collections/lstfusion"
    },
    {
      "rel": "self",
      "href": "https://api.constellr.com/stac/collections/lstfusion/items/item_id"
    }
  ],
  "assets": {
    "lst": {
      "href": "s3://bucket/path/lst.tiff",
      "type": "image/tiff"
    },
    "metadata": {
      "href": "s3://bucket/path/metadata.json",
      "type": "application/json"
    }
  },
  "collection": "lstfusion",
  "properties": {
    "gsd": 30,
    "datetime": "2025-08-18T11:00:00Z"
  },
  "stac_version": "1.1.0",
  "stac_extensions": []
}
```

**Error Responses**

- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.
- **404:** Item not found.
- **422:** Request parameter validation error.

---

<h3>6. Search STAC Collections (POST)</h3>

**Endpoint:**  `POST /stac/search`  
**Description:** Performs a search on STAC collections using a request body.


**Request Body Example**
```json
{
  "collections": ["lstfusion"],
  "bbox": [8.3, 49.6, 9.0, 50.1],
  "datetime": "2025-08-18T11:00:00Z/.."
}
```
**Example: cURL**
```sh
curl -X POST "https://api.constellr.com/stac/search" \
  -H "X-Api-Key: <your_api_key>" \
  -H "Content-Type: application/json" \
  -d '{
    "collections": ["lstfusion"],
    "bbox": [8.3, 49.6, 9.0, 50.1],
    "datetime": "2025-08-18T11:00:00Z/.."
  }'
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/stac/search"
headers = {
    "X-Api-Key": "<your_api_key>",
    "Content-Type": "application/json",
}
payload = {
    "collections": ["lstfusion"],
    "bbox": [8.3, 49.6, 9.0, 50.1],
    "datetime": "2025-08-18T11:00:00Z/..",
}

resp = requests.post(url, headers=headers, json=payload)
resp.raise_for_status()
data = resp.json()

print("numberMatched:", data.get("numberMatched"))
print("numberReturned:", data.get("numberReturned"))
```

**Success Response (200)**
```json
{
  "type": "FeatureCollection",
  "links": [
    {"rel": "root", "href": "https://api.constellr.com/stac/"},
    {"rel": "self", "href": "https://api.constellr.com/stac/search"}
  ],
  "features": [],
  "numberMatched": 1,
  "numberReturned": 0
}
```

**Error Responses**

- **400:** Invalid search request body values.
- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.
- **422:** Request body validation error.

---

<h3>7. Search STAC Collections (GET)</h3>

**Endpoint:**  `GET /stac/search`  
**Description:** Performs a search on STAC collections using query parameters.

**Query Parameters (optional):**

- `collections`: Array of collection IDs to search for items (comma-separated).
- `ids`: Array of item IDs to return (comma-separated).
- `bbox`: Only return items intersecting this bounding box.
- `intersects`: GeoJSON geometry to intersect with (mutually exclusive with `bbox`).
- `datetime`: Only return items with a temporal property intersecting this value.
- `limit`: Limits the number of results per page.
- `fields`: Include or exclude fields from items body.
- `filter`: CQL2-JSON filter expression as a JSON string.
- `filter-lang`: The language used for the `filter` value (currently `cql2-json`).
- `filter-crs`: CRS URI for interpreting filter geometry coordinates.
- `sortby`: Array of property names to sort by, prefixed by `+` or `-`.
- `token`: Pagination token from a previous response.

**Example: cURL**
```sh
curl -G "https://api.constellr.com/stac/search" \
  -H "X-Api-Key: <your_api_key>" \
  --data-urlencode "collections=lstfusion" \
  --data-urlencode "limit=5" \
  --data-urlencode "datetime=2025-08-18T11:00:00Z/.." \
  --data-urlencode "sortby=-datetime"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/stac/search"
headers = {"X-Api-Key": "<your_api_key>"}
params = {
    "collections": "lstfusion",
    "limit": 5,
    "datetime": "2025-08-18T11:00:00Z/..",
    "sortby": "-datetime",
}

resp = requests.get(url, headers=headers, params=params)
resp.raise_for_status()
data = resp.json()

print("numberMatched:", data.get("numberMatched"))
print("numberReturned:", data.get("numberReturned"))
```

**Success Response (200)**
```json
{
  "type": "FeatureCollection",
  "links": [
    {"rel": "root", "href": "https://api.constellr.com/stac/"},
    {"rel": "self", "href": "https://api.constellr.com/stac/search"}
  ],
  "features": [],
  "numberMatched": 0,
  "numberReturned": 0
}
```

**Error Responses**

- **400:** Invalid search request parameters.
- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.
- **422:** Query parameter validation error.

---

<h3>8. Get Collection Items</h3>

**Endpoint:**  `GET /stac/collections/{collection_id}/items`  
**Description:** Fetches STAC items for a specific collection using query parameters.

**Query Parameters (optional):**

- `bbox`: Only return items intersecting this bounding box.
- `datetime`: Only return items with a temporal property intersecting this value.
- `limit`: Limits the number of results per page.
- `fields`: Include or exclude fields from items body.
- `filter`: CQL2-JSON filter expression as a JSON string.
- `filter-lang`: The language used for the `filter` value (currently `cql2-json`).
- `filter-crs`: CRS URI for interpreting filter geometry coordinates.
- `sortby`: Array of property names to sort by, prefixed by `+` or `-`.
- `token`: Pagination token from a previous response.

**Example: cURL**
```sh
curl -G "https://api.constellr.com/stac/collections/lstfusion/items" \
  -H "X-Api-Key: <your_api_key>" \
  --data-urlencode "limit=5" \
  --data-urlencode "datetime=2025-08-18T11:00:00Z/.." \
  --data-urlencode "sortby=-datetime"
```

**Example: Python**
```python
import requests

collection_id = "lstfusion"
url = f"https://api.constellr.com/stac/collections/{collection_id}/items"
headers = {"X-Api-Key": "<your_api_key>"}
params = {
    "limit": 5,
    "datetime": "2025-08-18T11:00:00Z/..",
    "sortby": "-datetime",
}

resp = requests.get(url, headers=headers, params=params)
resp.raise_for_status()
data = resp.json()

print("numberMatched:", data.get("numberMatched"))
print("numberReturned:", data.get("numberReturned"))
```

**Success Response (200)**
```json
{
  "type": "FeatureCollection",
  "features": [],
  "links": [
    {
      "rel": "collection",
      "type": "application/json",
      "href": "https://api.constellr.com/stac/collections/lstzoom"
    },
    {
      "rel": "parent",
      "type": "application/json",
      "href": "https://api.constellr.com/stac/collections/lstzoom"
    },
    {
      "rel": "root",
      "type": "application/json",
      "href": "https://api.constellr.com/stac/"
    },
    {
      "rel": "self",
      "type": "application/geo+json",
      "href": "https://api.constellr.com/stac/collections/lstzoom/items"
    }
  ],
  "numberMatched": 0,
  "numberReturned": 0
}
```

**Error Responses**

- **400:** Invalid request parameters.
- **401:** Invalid API key.
- **403:** User not authorized to access this endpoint.
- **422:** Query parameter validation error.

---
