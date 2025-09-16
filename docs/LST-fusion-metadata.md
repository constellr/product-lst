# LSTfusion Metadata

This page describes the metadata file used for L2A products. 


<style>
  table { border-collapse: collapse; width: 100%; table-layout: fixed; }
  th, td { border: 1px solid #aaa; padding: 6px; text-align: left; word-wrap: break-word; }
  th { background-color: #f2f2f2; }

  /* Adjust column widths */
  th:nth-child(1), td:nth-child(1) { width: 25%; } 
  th:nth-child(2), td:nth-child(2) { width: 20%; } 

  /* Hierarchy styling */
  .level-1 { font-weight: bold; }
  .level-2 { font-style: normal; color: #000; }
  .level-3 { font-style: italic; color: #333; }
  .level-4 { font-style: italic; color: #555; }
  .level-5 { font-style: italic; color: #777; }
</style>

<table>
  <tr>
    <th>Key</th>
    <th>Content Type</th>
    <th>Description</th>
  </tr>

  <!-- product-level keys -->
  <tr><td class="level-1">product_type</td><td>string</td><td>"L2"</td></tr>
  <tr><td class="level-1">product_name</td><td>string</td><td>"LSTfusion"</td></tr>
  <tr><td class="level-1">link</td><td>string</td><td><a href= "https://constellr.github.io/product-lst/Technical-specification/">URL with complementary documentation and data access info</a></td></tr>
  <tr><td class="level-1">source</td><td>string</td><td> "constellr" </td></tr>
  <tr><td class="level-1">acquisition_time</td><td>string</td><td>Date and time of the acquisition, ISO 8601 format at UTC time</td></tr>
  <tr><td class="level-1">sources</td><td>string</td><td> satellite sensors used, e.g. CLMS, MODIS_AQUA, MODIS_TERRA, VIIRS_NOAA20, VIIRS_NPP </td></tr>
  <tr><td class="level-1">&nbsp;&nbsp;&nbsp;&nbsp;resolutions</td><td>number array</td><td>Spatial resolution for this band</td></tr>
  <tr><td class="level-1">&nbsp;&nbsp;&nbsp;&nbsp;resolution_unit</td><td>string</td><td>"m"</td></tr>
  <tr><td class="level-1">&nbsp;&nbsp;bbox_WGS84</td><td>number array</td><td>Bounding box in Lon/Lat (WGS84), RFC 7946 format</td></tr>
  <tr><td class="level-1">&nbsp;&nbsp;bbox_utm</td><td>number array</td><td>Bounding box in UTM reference system, RFC 7946 format</td></tr>
  <tr><td class="level-1">&nbsp;&nbsp;utm_crs</td><td>string</td><td>EPSG code of the UTM Coordinate Reference System used for the dataset</td></tr>
  <tr><td class="level-1">processing_start_time</td><td>string</td><td>ISO-8601 string indicating start time of imagery processing</td></tr>
  <tr><td class="level-1">processing_end_time</td><td>string</td><td>ISO-8601 string indicating end time of imagery processing</td></tr>
  <tr><td class="level-1">&nbsp;&nbsp;request_aoi</td><td>object</td><td></td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;&nbsp;&nbsp;type</td><td>string</td><td>Polygon</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;&nbsp;&nbsp;coordinates</td><td>number array</td><td>Default GeoJSON footprint geometry</td></tr  
  <tr><td class="level-1">&nbsp;&nbsp;request_start_datetime</td><td>string</td><td>ISO-8601 start time of imagery request</td></tr>
  <tr><td class="level-1">&nbsp;&nbsp;request_end_datetime</td><td>string</td><td>ISO-8601 end time of imagery request</td></tr>
  
</table> 
