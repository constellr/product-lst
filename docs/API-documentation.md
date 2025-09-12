# **Constellr API Documentation**
 
This guide outlines how to authenticate, search, and download your data using the constellr API. For a detailed overview of the latest API, including live examples, refer to the [interactive Swagger documentation](https://api.constellr.com/docs) or access the OpenAPI JSON File.

---

## Initial Preparation

- Create an Account: Users should create their accounts via Constellr's end-user platform, which can be found at [https://app.constellr.com/signup](https://app.constellr.com/signup)

- Activate Account: After registering, users must activate their account by confirming their e-mail address.

- Once activated, you can begin accessing and retrieving data using the API.

---

## Usage Notes

- Add the word `Bearer` before the access token in the `Authorization` header for all API requests (except `/token` endpoint):
  ```
  Authorization: Bearer <access_token>
  ```
- If your token expires, you will receive a 403 Not Authenticated error. Request a new token and retry.
- Never store your credentials in plain text in production code.

---

## Authentication API

**Endpoint:** `POST /token`   
**Description:** Generates an access token to call API endpoints. Endpoints require a token in the `Authorization` header as `Bearer <token>`.  Tokens are valid for **one hour**.

**Request Body Example:**
```
username=your_username
password=your_password
```

**Example: cURL**
```sh
curl -X POST https://api.constellr.com/token \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

**Example: Python**
```python
import requests

url = "https://api.constellr.com/token"
data = {
    "username": "your_username",
    "password": "your_password"
}
resp = requests.post(url, json=data)
token = resp.json().get("access_token")
print(token)
```

**Example: TypeScript (Fetch)**
```ts
const url = "https://api.constellr.com/token";

fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    username: "your_username",
    password: "your_password",
  }),
})
  .then((res) => res.json())
  .then((data) => {
    console.log(data.access_token);
  });
```

**Success Response (200):**
```json
{
  "access_token": "string"
}
```

**Error Responses:**

- **401:** Invalid credentials, User not confirmed, or password reset required.


---


## Orders API

The `/orders` endpoint allows you to create, list, and retrieve orders for your organization. All operations require authentication via a Bearer token.

### 1. Create Orders in Batch

**Endpoint:** `POST /orders/batch`  
**Description:** Create multiple new orders for your organization in a single request.

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
      "product_name": "LSTPrecision",
      "comment": "Order for field 42"
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
import json

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
            "product_name": "LSTPrecision",
            "comment": "Order for field 42"
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())

```


**Example: TypeScript  (Fetch)**
```ts
const url = "https://api.constellr.com/orders/batch";
const token = "<access_token>";

const payload = {
  use_case: "Yield Prediction",
  comment: "Urgent order for Q3 analysis",
  orders: [
    {
      area_of_interest_id: "1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
      start_date: "2025-09-27T10:30:08.004000Z",
      end_date: "2025-10-18T10:30:08.004000Z",
      frequency: "single-image",
      product_name: "LSTPrecision",
      comment: "Order for field 42",
    },
  ],
};

fetch(url, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${token}`,
    "Content-Type": "application/json",
    "accept": "application/json",
  },
  body: JSON.stringify(payload),
})
  .then((res) => res.json())
  .then((data) => console.log(data))
  .catch((err) => console.error("Error creating orders:", err));

```

**Response (201):**
```json
[
  {
    "area_of_interest_id": "1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
    "start_date": "2025-09-27T10:30:08.004000Z",
    "end_date": "2025-10-18T10:30:08.004000Z",
    "frequency": "single-image",
    "product_name": "LSTPrecision",
    "comment": "Order for field 42",
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "created": "2025-08-27T11:54:24.206072Z",
    "state": "initial_state"
  }
]
```

**Error Responses:**

- **400:** Invalid order request period.

- **404:** Invalid product or area of interest.

- **422:** Request parameters validation error.

- **502:** Order creation error.

---

### 2. List All Orders

**Endpoint:** `GET /orders`  
**Description:** List all orders for your organization with pagination and sorting.

**Query Parameters:**

- `limit` (optional, default: 10): Maximum number of orders to return.

- `offset` (optional, default: 0): Number of orders to skip.

- `sort` (optional, default: `-created`): Sort order.


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

**Example: TypeScript  (Fetch)**
```ts
const token = "<access_token>";
const params = new URLSearchParams({
  limit: "10",
  offset: "0",
  sort: "-created", // '+' asc or '-' desc
});

const res = await fetch(`https://api.constellr.com/orders?${params.toString()}`, {
  headers: { Authorization: `Bearer ${token}` },
});

if (!res.ok) {
  throw new Error(`Request failed: ${res.status} ${res.statusText}`);
}

const data = await res.json();
console.log(data.count, data.items.length);
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
      "product_name": "LSTPrecision",
      "comment": "Order for field 42",
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "created": "2025-08-27T11:54:24.206072Z",
      "state": "initial_state"
    }
  ]
}
```
**Error Responses:**

- **422:** Request parameters validation error.

- **502:** Order retrieval error.

---

### 3. Get Order by ID

**Endpoint:** `GET /orders/{order_id}`  
**Description:** Retrieve a specific order by its unique ID.


**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/orders/123e4567-e89b-12d3-a456-426614174000" \
  -H "Authorization: Bearer <access_token>"
```

**Response (200):**
```json
{
  "area_of_interest_id": "1c53eaa-9b26-4c3d-8998-bfc8e9ac1770",
  "start_date": "2025-09-27T10:30:08.004000Z",
  "end_date": "2025-10-18T10:30:08.004000Z",
  "frequency": "single-image",
  "product_name": "LSTPrecision",
  "comment": "Order for field 42",
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "created": "2025-08-27T11:54:24.206072Z",
  "state": "initial_state"
}
```
**Error Responses:**

- **404:** Order not found.

- **422:** Request parameters validation error.

- **502:** Order retrieval error.

---

### 4. Get Available Order Use Cases

**Endpoint:** `GET /orders/meta/use-cases`  
**Description:**  Returns a list of available order use cases supported by the API.  

**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/orders/meta/use-cases" \
  -H "Authorization: Bearer <access_token>"
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


---

## Areas of Interest API

The `/areas-of-interest` endpoint allows you to create, list, and retrieve Areas of Interest (AOIs) for your organization. AOIs define geographic regions used in data orders. All operations require authentication via a Bearer token.

### 1. Create an Area of Interest

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

**Example: TypeScript  (Fetch)**
```ts
const url = "https://api.constellr.com/areas-of-interest";
const token = "<access_token>";

const payload = {
  name: "Test AOI",
  description: "Test area",
  geometry: {
    type: "Polygon",
    coordinates: [
      [
        [8.68483, 49.885416],
        [8.684889, 49.876422],
        [8.670971, 49.876383],
        [8.67091, 49.885378],
        [8.68483, 49.885416],
      ],
    ],
  },
};

fetch(url, {
  method: "POST",
  headers: {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify(payload),
})
  .then((res) => res.json())
  .then((data) => console.log(data))
  .catch((err) => console.error("Error creating AOI:", err));
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

- **422:** Request parameters validation error.


---

### 2. Get an Area of Interest by ID

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

- **404:** Area of interest not found.

- **422:** Request parameters validation error.

---

### 3. List Areas of Interest

**Endpoint:**  `GET /areas-of-interest`  
**Description:** Lists all AOIs for your organization with pagination and sorting.

**Query Parameters**

- `limit` (optional, default: 10): Maximum number of items to return.

- `offset` (optional, default: 0): Zero-based index of the first item to return.

- `sort` (optional, default: `-created`): Property to sort by. Use `+` or `-` as a prefix for ascending or descending order.

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

**Example: TypeScript  (Fetch)**
```ts
const token = "<access_token>";
const params = new URLSearchParams({
  limit: "10",
  offset: "0",
  sort: "-created",
});

const res = await fetch(`https://api.constellr.com/areas-of-interest?${params.toString()}`, {
  headers: { Authorization: `Bearer ${token}` },
});

if (!res.ok) {
  throw new Error(`Request failed: ${res.status} ${res.statusText}`);
}

const data = await res.json();
console.log("Total AOIs:", data.count);
data.items.forEach((item: any) => console.log(item.id, item.name));
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

- **422:** Request parameters validation error.

---

### 4. Get Geometry Info from AOI

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

**Example: TypeScript  (Fetch)**

```ts
const url = "https://api.constellr.com/areas-of-interest/geometry-info";
const token = "<access_token>";

const payload = {
  type: "Feature",
  geometry: {
    type: "Polygon",
    coordinates: [
      [
        [11.053963, 51.690862],
        [11.976814, 51.690862],
        [11.976814, 51.059955],
        [10.944099, 51.073763],
        [11.053963, 51.690862],
      ],
    ],
  },
};

const res = await fetch(url, {
  method: "POST",
  headers: {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify(payload),
});

if (!res.ok) {
  throw new Error(`Request failed: ${res.status} ${res.statusText}`);
}

const data = await res.json();
console.log("bbox_width:", data.bbox_width);
console.log("bbox_height:", data.bbox_height);
console.log("area:", data.area);
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

- **422:** Request parameters validation error eg. invalid GeoJSON.


---

## Products API

The `/products` endpoint provides access to the list of available constellr products. Use it to explore product details before creating data orders. All operations require authentication via a Bearer token.

### 1. List Available Products

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

**Error Responses:**

- **502:** Products retrieval error.

---


## STAC API

A STAC (SpatioTemporal Asset Catalog) API is ideal when you need to programmatically search, filter, and access large volumes of Earth Observation data. It provides a standardized way to query and retrieve metadata and assets, making it suitable for automated workflows and integration with other tools. It naturally extends a static STAC catalogue to allow for dynamic search based on additional filters. In contrast, a web application is more user-friendly for interactive browsing, visualizing, and manually selecting data products. Use a STAC API for efficient, scalable data access in automated systems, and a web application for a more intuitive, hands-on experience. All operations require authentication via a Bearer token.

### 1. Get STAC Landing Page

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

---

### 2. Get Conformance Classes

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


---

### 3. List Available Collections

**Endpoint:**  `GET /stac/collections`  
**Description:** Fetches the available STAC collections for your organization.

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

**Example: TypeScript (Fetch)**
```ts
const url = "https://api.constellr.com/stac/collections";
const token = "<access_token>";

const params = new URLSearchParams({
  limit: "5",
  offset: "0",
  bbox: "-122.1,5.1,35.4,53.6",
});

fetch(`${url}?${params.toString()}`, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${token}`,
  },
})
  .then((res) => {
    if (!res.ok) {
      throw new Error(`Request failed: ${res.status} ${res.statusText}`);
    }
    return res.json();
  })
  .then((data) => {
    for (const collection of data.collections) {
      console.log(`${collection.id} - ${collection.title}`);
    }
  })
  .catch((err) => {
    console.error("Error fetching collections:", err);
  });
```
**Query Parameters (optional):**

- `limit`: Limits the number of results per page.

- `offset`: Number of items to skip before starting to collect the result set.

- `bbox`: Only return items intersecting this bounding box.

- `datetime`: Only return items with a temporal property intersecting this value.

- `sortby`: Array of property names to sort by, prefixed by `+` or `-`.

- `filter`: CQL filter expression for filtering items.

- `filter-lang`: The language used for the `filter` value (e.g., `cql2-json`).

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

- **422:** Request parameters validation error.

---

### 4. Get a Single Collection

**Endpoint:**  `GET /stac/collections/{collection_id}`  
**Description:** Fetches a single STAC collection by its ID.


**Example: cURL**
```sh
curl -X GET "https://api.constellr.com/stac/collections/lstfusion" \
  -H "Authorization: Bearer <access_token>"
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

- **404:** Collection with ID lstfusion not found.

- **422:** Request parameters validation error.

---

### 5. Get a Single Item by Collection and Item ID

**Endpoint:**  `GET /stac/collections/{collection_id}/items/{item_id}`  
**Description:** Fetches a single STAC item by collection and item ID.


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


**Example: TypeScript (Fetch)**
```ts
const collectionId = "lstfusion";
const itemId = "item_id";
const url = `https://api.constellr.com/stac/collections/${collectionId}/items/${itemId}`;
const token = "<access_token>";

fetch(url, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${token}`,
  },
})
  .then((res) => {
    if (!res.ok) {
      throw new Error(`Request failed: ${res.status} ${res.statusText}`);
    }
    return res.json();
  })
  .then((data) => {
    console.log(`${data.id} - ${data.collection}`);
  })
  .catch((err) => {
    console.error("Error fetching item:", err);
  });
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

- **404:** Item with ID item_id in collection lstfusion not found.

- **502:**  Failed to retrieve item.

- **422:** Request parameters validation error.

---

### 6. Search STAC Collections

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

**Example: TypeScript (Fetch)**
```ts
const url = "https://api.constellr.com/stac/search";
const token = "<access_token>";

const payload = {
  collections: ["lstfusion"],
  bbox: [8.3, 49.6, 9.0, 50.1],
  datetime: "2025-08-18T11:00:00Z/..",
};

const res = await fetch(url, {
  method: "POST",
  headers: {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify(payload),
});

if (!res.ok) {
  throw new Error(`Request failed: ${res.status} ${res.statusText}`);
}

const data = await res.json();
console.log("numberMatched:", data.numberMatched);
console.log("numberReturned:", data.numberReturned);
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

- **400:** Invalid filter or collection not allowed.

- **404:** No data orders found for the organization.

- **422:** Request parameters validation error.

- **502:** Failed to perform search.

---