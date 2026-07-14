"""
Download all assets associated with a Constellr order using the STAC Search API.

The script searches for STAC items belonging to a specified order. Optional
spatial and temporal filters can be applied to further restrict the results.
The script automatically follows paginated search results and downloads all
assets associated with each returned item into a local directory.

Directory structure for the downloaded assets::
    downloads/
        <acquisition_datetime>_<feature_id>/
            asset_1.tif
            asset_2.json
            ...

Before running:
    - Set `API_KEY` to your Constellr API key.
    - Set `ORDER_ID` to the order to download.
    - Optionally customize the search payload (for example, `datetime`,
      `bbox`, `collections`, or `limit`) to further restrict the results.
"""

import os
import re
import requests

# Configuration and authentication
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.constellr.com"
ORDER_ID = "YOUR_ORDER_ID"
DOWNLOAD_DIR = "downloads"

headers = {"X-Api-Key": API_KEY, "Content-Type": "application/json"}

# Define the payload structure for the STAC Search API.
body = {
    # Maximum number of items returned per request.
    "limit": 10,

    # STAC collection(s) to search.
    "collections": [
        "lstprecision",
    ],

    # Base filter: search within a specific Constellr order.
    "filter": {
        "op": "eq",
        "args": [
            {
                "property": "order:id",
            },
            ORDER_ID,
        ],
    },

    # Optional temporal filter.
    #
    # Exact acquisition time:
    # "datetime": "2026-07-08T23:58:15.445339Z",
    #
    # Time range:
    # "datetime": "2026-06-01T00:00:00Z/2026-07-15T23:59:59Z",
    #
    # After a specific date:
    # "datetime": "2026-06-01T00:00:00Z/..",


    # Optional spatial filter using a bounding box.
    #
    # Format:
    # [minimum_longitude, minimum_latitude, maximum_longitude, maximum_latitude]
    #
    # Example: Antwerp, Belgium area
    # "bbox": [4.22, 51.16, 4.66, 51.45],


    # Optional spatial filter using geometry intersection.
    #
    # Replace the base filter above with this filter to return
    # items whose footprint intersects the provided GeoJSON geometry.
    #
    # Example: Point intersection (Antwerp, Belgium)
    #
    # "filter": {
    #     "op": "and",
    #     "args": [
    #         {
    #             "op": "eq",
    #             "args": [
    #                 {
    #                     "property": "order:id",
    #                 },
    #                 ORDER_ID,
    #             ],
    #         },
    #         {
    #             "op": "s_intersects",
    #             "args": [
    #                 {
    #                     "property": "geometry",
    #                 },
    #                 {
    #                     "type": "Point",
    #                     "coordinates": [
    #                         4.40026,
    #                         51.22047,
    #                     ],
    #                 },
    #             ],
    #         },
    #     ],
    # },


    # Sort results by acquisition time (newest first).
    "sortby": [
        {
            "field": "datetime",
            "direction": "desc",
        }
    ],
}

# Ensure the root download directory exists locally before proceeding.
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def extract_file_name_from_s3_url(file_url: str) -> str:
    """
    Parses a signed S3 URL to extract a clean local filename.

    Removes complex query/signature parameters attached to the URL, isolates
    the base file name from the path, and replaces any unexpected whitespace
    characters with safe underscores.
    """
    # Strip off the query string parameters (e.g., AWS signatures, expiration tokens)
    clean_url = file_url.split("?")[0]

    # Extract the actual file name from the final segment of the URL path
    path_segments = [seg for seg in clean_url.split("/") if seg]
    file_name = path_segments[-1]

    # Sanitize the file name by replacing any whitespace sequences with underscores
    return re.sub(r"\s+", "_", file_name)


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

            # Derive a clean file destination name using the S3 URL parsing utility
            filename_from_url = extract_file_name_from_s3_url(url)
            filename = os.path.join(item_dir, filename_from_url)

            # Initialize a streamed HTTP GET request to optimize memory consumption when downloading large files.
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(filename, "wb") as f:
                    # Write the file directly to disk in small, manageable binary blocks (8KB chunks)
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"Downloaded {filename}")

    # Handle server-side pagination: Look for the 'next' relationship tag in the link block.
    # If a 'next' page link exists, update the query body context to request the next batch of data.
    next_link = next((l for l in data.get("links", []) if l["rel"] == "next"), None)
    body = next_link["body"] if next_link else None
