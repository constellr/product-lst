# **Constellr API Documentation**
 
This guide outlines how to authenticate, place orders, search, and download your data using the constellr API. For a detailed overview of the latest API, including live examples, refer to the [interactive Swagger documentation](https://api.constellr.com/docs) or [Redoc documentation](https://api.constellr.com/redoc).

---

## Initial Preparation
- To access the Constellr UI and API, your company’s email domain must be registered with Constellr. Once registered, you can create an account using your company email.

- Create an Account: You can create your account via Constellr's end-user platform, which can be found at [https://app.constellr.com/signup](https://app.constellr.com/signup)

- Activate Account: After registering, you must activate your account by confirming your e-mail address.

- Once activated, you can begin accessing and retrieving data using the API.

---

## Usage Notes

- Add the word `Bearer` before the access token in the `Authorization` header for all API requests (except `/token` endpoint):
  ```
  Authorization: Bearer <access_token>
  ```
- If your token expires, you will receive a 401 Not Authenticated error. Request a new token and retry.
- Never store your credentials in plain text in production code.

---

## Authentication API

**Endpoint:** `POST /token`   
**Description:** Generates an access token to call the API endpoints. Endpoints require a token in the `Authorization` header as `Bearer <token>`. Tokens are valid for **24 hours**.

**Headers:**
```
{
  Accept=application/json
  Content-Type=application/x-www-form-urlencoded
}
```

**Request Body (in url-encoded format):**
```
{
  username=your_username
  password=your_password
}
```

**Example: cURL**
```sh
curl --location 'https://api.constellr.com/token' \
--header 'Accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=your_username' \
--data-urlencode 'password=your_password'
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/token"
headers = {
  "Accept": "application/json",
  "Content-Type": "application/x-www-form-urlencoded",
}
data = {
    "username": "your_username",
    "password": "your_password",
}

resp = requests.post(url, headers=headers, data=data)
token = resp.json().get("access_token")
print(token)
```

**Success Response (200):**
```json
{
  "access_token": "string"
}
```

**Error Responses:**

- **401:** Invalid credentials, user not confirmed, token expired or password reset required.
- **422:** Request body validation error.

---


## Orders API

The `/orders` endpoint allows you to create, list, and retrieve orders for your organization. All operations require authentication via a Bearer token.

<h3>1. Create Orders in Batch</h3>

**Endpoint:** `POST /orders/batch`  
**Description:** Create multiple new orders for your organization in a single request. <br />
**Order Validation:** All orders are validated upon submission. If any order is invalid, the entire request is rejected with a 400/404 status code and an error message. <br />

- **Product Specific Validation**:<br />

| Feature | LSTprecision / LSTzoom | LSTfusion |
| :--- | :--- | :--- |
| **AOI Limit** | Bounding box limit max **15,000m** x **15,000m** | **No limit** |
| **Start Date** | At least **8 days** from today | No restriction |
| **Duration** | Min **7 days**, Max **1 year** | No restriction |
| **Frequency** | `single_image`, `max_frequency`,<br>`once_every_two_weeks`, `monthly` | `daily` only | <br />

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
      "area_of_interest_id": "1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
      "start_date": "2025-09-27T10:30:08.004000Z",
      "end_date": "2025-10-18T10:30:08.004000Z",
      "frequency": "single-image",
      "product_name": "LSTprecision",
      "comment": "Order for field 42",
      "tags": ["field42"],
      "illumination_constraint": "day"
    }
  ]
}
```


**Example: cURL**
```sh
curl -X POST "https://api.constellr.com/orders/batch" \
  -H 'accept: application/json' \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d @order_payload.json
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/orders/batch"
headers = {
    "Authorization": "Bearer <access_token>",
    "Content-Type": "application/json",
    "accept": "application/json"
}

payload = {
    "use_case": "Yield Prediction",
    "comment": "Urgent order for Q3 analysis",
    "orders": [
        {
            "area_of_interest_id": "1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
            "start_date": "2025-09-27T10:30:08.004000Z",
            "end_date": "2025-10-18T10:30:08.004000Z",
            "frequency": "single-image",
            "product_name": "LSTprecision",
            "comment": "Order for field 42",
            "tags": ["field42"],
            "illumination_constraint": "day"
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
    "area_of_interest_id": "1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
    "start_date": "2025-09-27T10:30:08.004000Z",
    "end_date": "2025-10-18T10:30:08.004000Z",
    "frequency": "single-image",
    "product_name": "LSTprecision",
    "comment": "Order for field 42",
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "created": "2025-08-27T11:54:24.206072Z",
    "state": "initial_state",
    "tags": [
      {
        "name": "field42",
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "created": "2025-11-28T10:05:36.362Z"
      }
    ],
    "illumination_constraint": "day"
  }
]
```

**Error Responses:**

- **400:** Invalid order request body values.
- **401:** Invalid authentication token.
- **403:** User not authorized to create orders.
- **404:** Resource not found (e.g., AOI or product does not exist).
- **422:** Request body validation error.
---

<h3>2. List All Orders</h3>

**Endpoint:** `GET /orders`  
**Description:** List all orders for your organization with pagination and sorting.

**Query Parameters:**

- `limit` (optional, default: 10): Maximum number of orders to return.

- `offset` (optional, default: 0): Number of orders to skip.

- `sort` (optional): Sort orders by the `-created` field.


**Example: cURL**
```bash
curl -G "https://api.constellr.com/orders" \
  -H "Authorization: Bearer <access_token>" \
  --data-urlencode "limit=10" \
  --data-urlencode "offset=0" \
  --data-urlencode "sort=-created"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/orders"
headers = {"Authorization": "Bearer <access_token>"}
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
      "area_of_interest_id": "1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
      "start_date": "2025-09-27T10:30:08.004000Z",
      "end_date": "2025-10-18T10:30:08.004000Z",
      "frequency": "single-image",
      "product_name": "LSTprecision",
      "comment": "Order for field 42",
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "created": "2025-08-27T11:54:24.206072Z",
      "state": "initial_state",
      "tags": [
        {
          "name": "field42",
          "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "created": "2025-11-28T10:05:36.362Z"
        }
      ],
      "illumination_constraint": "day"
    }
  ]
}
```
**Error Responses:**

- **401:** Invalid authentication token.
- **403:** User not authorized to view orders.
- **422:** Query parameter validation error.

---

<h3>3. Get Order by ID</h3>

**Endpoint:** `GET /orders/{order_id}`  
**Description:** Retrieve a specific order by its unique ID.


**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/orders/123e4567-e89b-12d3-a456-426614174000" \
  -H "Authorization: Bearer <access_token>"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/orders/123e4567-e89b-12d3-a456-426614174000"
headers = {
    "Authorization": "Bearer <access_token>"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())

```

**Response (200):**
```json
{
  "area_of_interest_id": "1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
  "start_date": "2025-09-27T10:30:08.004000Z",
  "end_date": "2025-10-18T10:30:08.004000Z",
  "frequency": "single-image",
  "product_name": "LSTprecision",
  "comment": "Order for field 42",
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "created": "2025-08-27T11:54:24.206072Z",
  "state": "initial_state",
  "tags": [
      {
        "name": "field42",
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "created": "2025-11-28T10:05:36.362Z"
      }
  ],
  "illumination_constraint": "day"
}
```
**Error Responses:**

- **401:** Invalid authentication token.
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
    "Authorization": "Bearer <access_token>"
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
  "area_of_interest_id": "1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
  "start_date": "2025-09-27T10:30:08.004000Z",
  "end_date": "2025-10-18T10:30:08.004000Z",
  "frequency": "single-image",
  "product_name": "LSTprecision",
  "comment": "Order for field 42",
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "created": "2025-08-27T11:54:24.206072Z",
  "state": "initial_state",
  "tags": [
      {
        "name": "field42",
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "created": "2025-11-28T10:05:36.362Z"
      }
  ],
  "illumination_constraint": "day"
}
```
**Error Responses:**

- **401:** Invalid authentication token.
- **403:** User not authorized to view the order.
- **404:** Order not found.
- **422:** Request parameter validation error.

---

<h3>5. Get Available Order Use Cases</h3>

**Endpoint:** `GET /orders/meta/use-cases`  
**Description:**  Returns a list of available order use cases supported by the API.  

**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/orders/meta/use-cases" \
  -H "Authorization: Bearer <access_token>"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/orders/meta/use-cases"
headers = {
    "Authorization": "Bearer <access_token>"
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

- **401:** Invalid authentication token.
- **403:** User not authorized to view use cases.

---

## Areas of Interest API

The `/areas-of-interest` endpoint allows you to create, list, and retrieve Areas of Interest (AOIs) for your organization. AOIs define geographic regions used in data orders. All operations require authentication via a Bearer token.

<h3>1. Create an Area of Interest</h3>

**Endpoint:**  `POST /areas-of-interest`  
**Description:** Creates a new Area of Interest (AOI) for your organization.

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
  -H "Authorization: Bearer <access_token>" \
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
    "Authorization": "Bearer <access_token>",
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
  "id": "f1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
  "created": "2025-07-31T11:05:29.157539"
}
```


**Error Responses**

- **400:** Invalid AOI request body values.
- **401:** Invalid authentication token.
- **403:** User not authorized to create AOIs.
- **409:** An Area of Interest with this name already exists.
- **422:** Request body validation error.

---

<h3>2. Get an Area of Interest by ID</h3>

**Endpoint:**  `GET /areas-of-interest/{area_of_interest_id}`  
**Description:** Retrieves a specific AOI by its unique ID.

**Example: cURL**
```bash
curl -X GET "https://api.constellr.com/areas-of-interest/f1c53eaa-9b26-4c3d-8998-bfc8e9ac1770" \
  -H "Authorization: Bearer <access_token>"
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
  "id": "f1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
  "created": "2025-07-31T11:05:29.157539"
}
```

**Error Responses**

- **401:** Invalid authentication token.
- **403:** User not authorized to view the AOI.
- **404:** AOI not found.
- **422:** Request parameter validation error.

---

<h3>3. List Areas of Interest</h3>

**Endpoint:**  `GET /areas-of-interest`  
**Description:** Lists all AOIs for your organization with pagination and sorting.

**Query Parameters**

- `limit` (optional, default: 10): Maximum number of items to return.

- `offset` (optional, default: 0): Zero-based index of the first item to return.

- `sort` (optional): Property to sort results by the `-created` field. Use `+` or `-` as a prefix for ascending or descending order.

**Example: cURL**
```bash
curl -G "https://api.constellr.com/areas-of-interest" \
  -H "Authorization: Bearer <access_token>" \
  --data-urlencode "limit=10" \
  --data-urlencode "offset=0" \
  --data-urlencode "sort=-created"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/areas-of-interest"
headers = {"Authorization": "Bearer <access_token>"}
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
      "id": "f1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
      "created": "2025-04-03T10:36:40.348842"
    }
  ]
}
```


**Error Responses**

- **401:** Invalid authentication token.
- **403:** User not authorized to view AOIs.
- **422:** Query parameter validation error.

---

<h3>4. Get Geometry Info from AOI</h3>

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
  -H "Authorization: Bearer <access_token>" \
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
    "Authorization": "Bearer <access_token>",
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
- **401:** Invalid authentication token.
- **403:** User not authorized to access this endpoint.
- **422:** Request body validation error.

---

## Products API

The `/products` endpoint provides access to the list of available constellr products. Use it to explore product details before creating data orders. All operations require authentication via a Bearer token.

<h3>1. List Available Products</h3>

**Endpoint:**  `GET /products`  
**Description:** Retrieves a list of available products for your organization.


**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/products" \
  -H "Authorization: Bearer <access_token>"
```

**Success Response (200)**

```json
[
  {"name": "LSTprecision"},
  {"name": "LSTfusion"}
]
```

**Error Responses**

- **401:** Invalid authentication token.
- **403:** User not authorized to access this endpoint.


## STAC API
The `/stac` endpoint provides access to SpatioTemporal Asset Catalog (STAC) API, allowing you to search and retrieve geospatial data in a standardized format.
All operations require authentication via a Bearer token. The endpoints comply with the STAC API specification.

<h3>1. Get STAC Landing Page</h3>

**Endpoint:**  `GET /stac`  
**Description:** Fetches landing page data for the STAC Browser.

**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/stac" \
  -H "Authorization: Bearer <access_token>"
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
      "href": "https://example.com/stac/"
    },
    {
      "rel": "data",
      "type": "application/json",
      "title": "Collections available for this Catalog",
      "href": "https://example.com/stac/collections"
    }
  ],
  "stac_extensions": []
}
```

**Error Responses**

- **401:** Invalid authentication token.
- **403:** User not authorized to access this endpoint.

---

<h3>2. Get Conformance Classes</h3>

**Endpoint:**  `GET /stac/conformance`  
**Description:** Fetches the conformance classes supported by the STAC API.

**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/stac/conformance" \
  -H "Authorization: Bearer <access_token>"
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

- **401:** Invalid authentication token.
- **403:** User not authorized to access this endpoint.


---

<h3>3. List Available Collections</h3>

**Endpoint:**  `GET /stac/collections`  
**Description:** Fetches the available STAC collections for your organization.

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
  -H "Authorization: Bearer <access_token>" \
  --data-urlencode "limit=5" \
  --data-urlencode "offset=0" \
  --data-urlencode "bbox=-122.1,5.1,35.4,53.6"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/stac/collections"
headers = {"Authorization": "Bearer <access_token>"}
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
          "href": "https://example.com/stac/collections/lstfusion/items"
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
    {"rel": "root", "href": "https://example.com/stac/"}
  ],
  "numberMatched": 1,
  "numberReturned": 1
}
```

**Error Responses**

- **401:** Invalid authentication token.
- **403:** User not authorized to access this endpoint.
- **422:** Query parameter validation error.

---

<h3>4. Get a Single Collection</h3>

**Endpoint:**  `GET /stac/collections/{collection_id}`  
**Description:** Fetches a single STAC collection by its ID.


**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/stac/collections/lstfusion" \
  -H "Authorization: Bearer <access_token>"
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/stac/collections/lstfusion"

headers = {
    "Authorization": "Bearer <access_token>"
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
      "href": "https://example.com/stac/collections/lstfusion/items"
    },
    {
      "rel": "self",
      "href": "https://example.com/stac/collections/lstfusion"
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

- **401:** Invalid authentication token.
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
  -H "Authorization: Bearer <access_token>"
```

**Example: Python**
```python
import requests

collection_id = "lstfusion"
item_id = "item_id"
url = f"https://api.constellr.com/stac/collections/{collection_id}/items/{item_id}"
headers = {"Authorization": "Bearer <access_token>"}

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
      "href": "https://example.com/stac/collections/lstfusion"
    },
    {
      "rel": "self",
      "href": "https://example.com/stac/collections/lstfusion/items/item_id"
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

- **401:** Invalid authentication token.
- **403:** User not authorized to access this endpoint.
- **404:** Item not found.
- **422:** Request parameter validation error.

---

<h3>6. Search STAC Collections</h3>

**Endpoint:**  `POST /stac/search `  
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
  -H "Authorization: Bearer <access_token>" \
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
    "Authorization": "Bearer <access_token>",
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
    {"rel": "root", "href": "https://example.com/stac/"},
    {"rel": "self", "href": "https://example.com/stac/search"}
  ],
  "features": [],
  "numberMatched": 1,
  "numberReturned": 0
}
```

**Error Responses**

- **400:** Invalid search request body values.
- **401:** Invalid authentication token.
- **403:** User not authorized to access this endpoint.
- **422:** Request body validation error.

---
