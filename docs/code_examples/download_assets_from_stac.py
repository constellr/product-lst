"""
Download all assets associated with a Constellr order using the STAC Search API.

The script searches for STAC items belonging to a specified order. Optional
spatial and temporal filters can be applied to further restrict the results.
The script automatically follows paginated search results and downloads all
assets associated with each returned item into a local directory.

Directory structure for the downloaded assets::
    downloads/
        <acquisition_datetime>_<feature_id>/
            LSTPRECISION_SBA02_U155VHMQ_20260708T235815Z_LST.tiff
            LSTPRECISION_SBA02_U155VHMQ_20260708T235815Z_METADATA.json
            ...

Before running:
    - Set `API_KEY` to your Constellr API key.
    - Set `ORDER_ID` to the order to download.
    - Optionally customize the search payload (for example, `datetime`,
      `bbox`, `collections`, or `limit`) to further restrict the results.
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse

import requests

# Configuration and authentication
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.constellr.com"
ORDER_ID = "YOUR_ORDER_ID"
DOWNLOAD_DIR = "downloads"

headers = {"X-Api-Key": API_KEY, "Content-Type": "application/json"}

# Define the payload structure for the STAC Search API.
# Optional filters you can add to `body` below:
#   datetime: "2026-07-08T23:58:15.445339Z"                      (exact time)
#   datetime: "2026-06-01T00:00:00Z/2026-07-15T23:59:59Z"        (range)
#   datetime: "2026-06-01T00:00:00Z/.."                          (open-ended)
#   bbox: [4.22, 51.16, 4.66, 51.45]                              ([minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude])
#   Geometry intersection:
#     Replace the `filter` in the body with:
#     {
#         "op": "and",
#         "args": [
#             {"op": "eq", "args": [{"property": "order:id"}, ORDER_ID]},
#             {"op": "s_intersects", "args": [{"property": "geometry"}, GEOJSON_GEOMETRY]},
#         ],
#     }

body = {
    "limit": 10, # max number of items to rereturn per request
    "collections": ["lstprecision"], # collection ids to search in
    "filter": {
        "op": "eq",
        "args": [{"property": "order:id"}, ORDER_ID], # order id filtering
    },
    "sortby": [{"field": "datetime", "direction": "desc"}], # sort by the acquisition datetime in descending order
}

# Ensure the root download directory exists locally before proceeding.
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def get_download_filename(response: requests.Response) -> str:
    """
    Return the filename from the Content-Disposition header, falling back to
    the last path component of the download URL.
    """
    disposition = response.headers.get("Content-Disposition")

    if disposition:
        match = re.search(r'filename="?([^"]+)"?', disposition)
        if match:
            return match.group(1)

    return Path(urlparse(response.url).path).name

# Execute the search query and loop dynamically through paginated results.
while body:
    # Query the Constellr STAC Search endpoint with the current page constraints.
    resp = requests.post(f"{BASE_URL}/stac/search", headers=headers, json=body)
    resp.raise_for_status()
    data = resp.json()

    # Process each imagery acquisition (feature) returned in the response page.
    for item in data["features"]:
        feature_id = item["id"]
        # Sanitize the ISO timestamp so it can be safely used as a folder name across platforms.
        acquired = item["properties"]["datetime"].replace(":", "-")

        # Combine the timestamp and unique feature ID to build a unique folder name.
        # This prevents directory namespace collisions if multiple features share a timestamp.
        folder_name = f"{acquired}_{feature_id}"
        item_dir = os.path.join(DOWNLOAD_DIR, folder_name)
        os.makedirs(item_dir, exist_ok=True)

        # Loop through and download all individual file assets (e.g., tiff, json metadata) linked to this item.
        for asset_name, asset in item["assets"].items():
            url = asset["href"]

            # Initialize a streamed HTTP GET request to optimize memory
            # consumption when downloading large files.
            with requests.get(url, stream=True) as r:
                r.raise_for_status()

                filepath = os.path.join(item_dir, get_download_filename(r))

                with open(filepath, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"Downloaded {filepath}")

    # Handle server-side pagination: Look for the 'next' relationship tag in the link block.
    # If a 'next' page link exists, update the query body context to request the next batch of data.
    next_link = next((l for l in data.get("links", []) if l["rel"] == "next"), None)
    body = next_link["body"] if next_link else None
