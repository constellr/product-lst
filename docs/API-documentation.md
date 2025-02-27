# **Constellr API Documentation**
 
## Using a STAC API {style="margin-bottom: 5px;"}

A STAC (SpatioTemporal Asset Catalog) API is ideal when you need to programmatically search, filter, and access large volumes of Earth Observation data. It provides a standardized way to query and retrieve metadata and assets, making it suitable for automated workflows and integration with other tools. It naturally extends a static STAC catalogue to allow for dynamic search based on additional filters. In contrast, a web application is more user-friendly for interactive browsing, visualizing, and manually selecting data products. Use a STAC API for efficient, scalable data access in automated systems, and a web application for a more intuitive, hands-on experience.

## Accessing constellr's API 

This guide outlines how to authenticate, search, and download your data using the constellr API. For a detailed overview of the latest API, including live examples, refer to the [interactive Swagger documentation](https://api.constellr.com/docs) or access the OpenAPI JSON File.

<h3>Initial Preparation</h3>

- Create an Account: Users should create their accounts via Constellr's end-user platform, which can be found at [https://app.constellr.com/signup](https://app.constellr.com/signup)

- Activate Account: After registering, users must activate their account by confirming their e-mail address.

Once activated, you can begin accessing and retrieving data using the API.

<h3>API Usage</h3>

**1- Request a temporary token**

Use the /token endpoint to obtain a temporary access token which is currently set to expire after 24 hours. This token is required to access most endpoints.

- Tokens are temporary and may expire during your session.

- In case of token expiration, your API requests will fail with an authentication error. Be sure to handle this error in your scripts by requesting a new token.

For details on token usage and example requests, visit the [API documentation](https://api.constellr.com/docs) .

**2- Search or Browse your ordered data**

Use the /assets endpoint to search for your ordered data.

- STAC Basics: The Constellr API uses the STAC model to structure spatial data.
  
- Catalogs: Collections of metadata or spatial assets.
  
- Collections: Groups of related catalogs with additional metadata.
  
- Items: Individual data entries within collections, typically tied to specific spatial or temporal locations.
  
- Assets: Files associated with an item (e.g., images, metadata, masks).


Unlike static STAC catalogs, the /assets endpoint allows dynamic filtering of assets. You can apply filters to quickly locate relevant assets (for example all assets in a specific order), bypassing the need to manually navigate through catalog structures. Please check the latest API documentation for the exact list of filter options which are currently available. Please do not hesitate to approach us via your customer support contact or email to support-csm@constellr.com if you need additional options.

**3- Download your selected assets**

Once you’ve retrieved a list of relevant assets using the /assets endpoint, download them via the /assets/{asset_name} endpoint.

- Retrieve the asset identifiers from the list.
  
- Send a request for each file you wish to download.
  
- You can download files sequentially or in parallel, depending on your workflow.

For concrete request examples and response formats, refer to the latest API documentation.

## Useful Code Snippets

In the code snippets, you would need to replace hardcoded credentials with actual credentials. Please note that you should never store your credentials in plain text in any piece of code.

<h3>Authentication: Generate Access Token</h3>

Endpoint
`POST /token`

Description
Generate an access token to call API endpoints. Most endpoints require a token in the Authorization header as Bearer <token>. The token is valid for 24 hours.

Request
```
{
  "username": "string",
  
  "password": "string"
}
```

Response (200)
```
{
  "access_token": "string"
}
```
Example: cURL
```
curl -X POST https://api.constellr.com/token \
-H "Content-Type: application/json" \
-d '{"username": "your_username", "password": "your_password"}'
```
Example: Python
```
import requests

url = 'https://api.constellr.com/token'
data = {
    "username": "your_username",
    "password": "your_password"
}
response = requests.post(url, json=data)
token = response.json().get('access_token')
```

Example: TypeScript (Fetch)

```
const url = "https://api.constellr.com/token";
```
```
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
  .then((response) => response.json())
  .then((data) => {
    const token = data.access_token;
    console.log(token);
  });
```

<h3>Get Assets</h3>


Endpoint
`GET /assets`

Description

Fetch a list of available assets. This requires a valid access token in the Authorization header.

Query Parameters
  
- lastModifiedBefore (optional): Filter assets modified before a specific date.
  
- lastModifiedAfter (optional): Filter assets modified after a specific date.
  
- limit (optional, default: 10): The number of assets to retrieve.
  
- continuation_token (optional): Token for pagination.
  
Response (200)
```
{
  "Contents": [
    {
      "Key": "example_file.txt",
      "LastModified": "2023-03-01T12:00:00Z",
      "Size": 1024
    }
  ]
}
```

Example: cURL
```
curl -X GET "https://api.constellr.com/assets" \
-H "Authorization: Bearer <access_token>"
```

Example: Python
```
url = 'https://api.constellr.com/assets'
headers = {
    'Authorization': f'Bearer {token}'
}
response = requests.get(url, headers=headers)
assets = response.json().get('Contents', [])
```
Example: TypeScript (Fetch)
```
const url = "https://api.constellr.com/assets";
const token = "your_access_token";

fetch(url, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${token}`,
  },
})
  .then((response) => response.json())
  .then((data) => {
    const assets = data.Contents;
    console.log(assets);
  });
```

<h3>Download Assets</h3>


Endpoint
`GET /assets/{asset_name}`

Description
Download a specific asset file by its name. The access token is required.

Path Parameter
- asset_name (required): The name of the file to download.
  
Example: cURL
```
curl -X GET "https://api.constellr.com/assets/example_file.txt" \
-H "Authorization: Bearer <access_token>" \
-o "example_file.txt"
```

Example: Python
```
asset_name = 'example_file.txt'
url = f'https://api.constellr.com/assets/{asset_name}'
response = requests.get(url, headers=headers)
with open(asset_name, 'wb') as file:
    file.write(response.content)
```
Example: TypeScript (Fetch)
```
import * as fs from "fs";
import * as path from "path";

// Function to download an asset from the API
async function downloadAsset(
  assetName: string,
  accessToken: string
): Promise<void> {
  const url = `https://api.constellr.com/assets/${assetName}`;

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    // Check if the response is okay (status code 200-299)
    if (!response.ok) {
      throw new Error(`Error: ${response.status} ${response.statusText}`);
    }

    // Set the path where you want to save the file
    const filePath = path.resolve(__dirname, assetName);

    // Create a writable stream to save the file
    const fileStream = fs.createWriteStream(filePath);

    // Use a readable stream from the response body and pipe it to the writable stream
    response.body?.pipe(fileStream);

    // Return a promise that resolves when the file is fully written
    return new Promise((resolve, reject) => {
      fileStream.on("finish", resolve); // Resolve the promise when done
      fileStream.on("error", reject); // Reject the promise on error
    });
  } catch (error) {
    console.error("Error downloading the asset:", error);
    throw error; // Rethrow error for higher-level handling if needed
  }
}

// Usage example
const assetName = "example_file.txt";
const accessToken = "your_access_token"; // Replace with your actual access token

downloadAsset(assetName, accessToken)
  .then(() => {
    console.log(`Successfully downloaded ${assetName}`);
  })
  .catch((error) => {
    console.error(`Failed to download ${assetName}:`, error);
  });
```

## Sample scripts

<h3>Python Script: Download Assets sequentially</h3>

```
import requests

# 1. Generate Access Token
def get_token(username, password):
    url = 'https://api.constellr.com/token'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json().get('access_token')

# 2. Fetch Assets List
def get_assets(token):
    url = 'https://api.constellr.com/assets'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json().get('Contents', [])

# 3. Download Asset
def download_asset(token, asset):
    url = f"https://api.constellr.com/assets/{asset['Key']}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    with open(asset['Key'], 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {asset['Key']}")

# Main function to coordinate the process
def main(username, password):
    token = get_token(username, password)
    assets = get_assets(token)

    # Sequentially download each asset
    for asset in assets:
        download_asset(token, asset)

if __name__ == '__main__':
    username = 'your_username'
    password = 'your_password'
    main(username, password)
```

<h3>Python Script: Download Assets in Parallel</h3>

Below is a Python script that:

1- Generates a token.

2- Fetches the list of assets.

3- Downloads the assets in parallel.

Note that while using Python's ThreadPoolExecutor is a viable option for parallelizing downloads in some settings, there are numerous alternative options available which may be more suitable in various standard use cases. If you need support parallelizing data acquisition or other operations, please feel free to reach out to the Software Team.

```
import requests
from concurrent.futures import ThreadPoolExecutor

# 1. Generate Access Token
def get_token(username, password):
    url = 'https://api.constellr.com/token'
    data = {'username': username, 'password': password}
    response = requests.post(url, json=data)
    return response.json().get('access_token')

# 2. Fetch Assets List
def get_assets(token):
    url = 'https://api.constellr.com/assets'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    return response.json().get('Contents', [])

# 3. Download Asset
def download_asset(token, asset):
    url = f"https://api.constellr.com/assets/{asset['Key']}"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    with open(asset['Key'], 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {asset['Key']}")

# 4. Parallel Download
def download_assets_in_parallel(token, assets):
    with ThreadPoolExecutor() as executor:
        executor.map(lambda asset: download_asset(token, asset), assets)

# Main function to coordinate the process
def main(username, password):
    token = get_token(username, password)
    assets = get_assets(token)
    download_assets_in_parallel(token, assets)

if __name__ == '__main__':
    username = 'your_username'
    password = 'your_password'
    main(username, password)
```

This script will generate a token, retrieve the list of assets, and download them in parallel using ThreadPoolExecutor. Make sure to replace your_username and your_password with your credentials.

