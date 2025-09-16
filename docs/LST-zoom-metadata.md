# LSTzoom Metadata

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
  <tr><td class="level-1">product_id</td><td>string</td><td>The name of this product</td></tr>
  <tr><td class="level-1">platform</td><td>string</td><td>The name of the spacecraft (e.g. SBA01)</td></tr>
  <tr><td class="level-1">product_type</td><td>string</td><td>"L2"</td></tr>
  <tr><td class="level-1">product_name</td><td>string</td><td>"LSTzoom"</td></tr>
  <tr><td class="level-1">processing_scenario</td><td>string</td><td>"NRT" or "RPR"</td></tr>
  <tr><td class="level-1">acquisition_id</td><td>string</td><td>Location and time of acquisition</td></tr>
  <tr><td class="level-1">acquisition_datetime</td><td>string</td><td>Date and time of the acquisition, ISO 8601 format at UTC time</td></tr>
  <tr><td class="level-1">processing_time</td><td>string</td><td>ISO-8601 string indicating start time of imagery processing</td></tr>
  <tr><td class="level-1">parent_product_key</td><td>string</td><td> </td></tr>
  <tr><td class="level-1">link</td><td>string</td><td>URL with complementary documentation and data access info</td></tr>
  <tr><td class="level-1">source</td><td>string</td><td>"constellr"</td></tr>
  <tr><td class="level-1">use_limitations</td><td>string</td><td>NA</td></tr>
  <tr><td class="level-1">atmospheric_data_source</td><td>string</td><td>"ERA5" or "CAMS_forecast"</td></tr>
  <tr><td class="level-1">elevation_data_source</td><td>string</td><td>DEM used for geometric/topographic correction (usually "COPERNICUS GLO30")</td></tr>
  <tr><td class="level-1">aerosol_model</td><td>string</td><td>"RURAL"</td></tr>
  <tr><td class="level-1">earth_sun_distance</td><td>float</td><td>Earth–Sun distance for irradiance correction factors</td></tr>
  <tr><td class="level-1">thick_cloud_percentage</td><td>float</td><td>Percentage of pixels covered by thick clouds</td></tr>
  <tr><td class="level-1">thin_cloud_percentage</td><td>float</td><td>Percentage of pixels covered by thin clouds</td></tr>
  <tr><td class="level-1">cloud_shadow_percentage</td><td>float</td><td>Percentage of pixels affected by cloud shadows</td></tr>

  <!-- mask_arrays -->
  <tr><td class="level-1">scl_masks_bands</td><td>object</td><td></td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;cloud_mask_classes</td><td>dict</td><td>Possible values of cloud mask: 0 = clear; 1 = thick; 2 = thin; 3 = shadow </td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;castshadow_mask_classes</td><td>dict</td><td>Possible values of cast-shadow mask: 0 = clear; 1 = castshadow</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;landwater_mask_classes</td><td>dict</td><td>Possible values of land/water mask: 0 = land; 1 = water</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;static_landwater_mask_classes</td><td>dict</td><td>Possible values of land/water mask: 0 = land; 1 = water</td></tr>

  <!-- sensors -->
  <tr><td class="level-1">sensors</td><td>object</td><td></td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;acquisition_starttime</td><td>string</td><td>ISO-8601 start time of imagery acquisition</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;acquisition_endtime</td><td>string</td><td>ISO-8601 end time of imagery acquisition</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;bbox</td><td>number array</td><td>Bounding box in Lon/Lat (WGS84), RFC 7946 format</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;geometry</td><td>object</td><td></td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;type</td><td>string</td><td>Polygon</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;coordinates</td><td>number array</td><td>Default GeoJSON footprint geometry</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;&nbsp;&nbsp;crs</td><td>string</td><td>Coordinate reference system</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;viewing_angles</td><td>object</td><td></td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;azimuth_mean</td><td>float</td><td>Mean viewing azimuth angle [deg]</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;zenith_mean</td><td>float</td><td>Mean viewing zenith angle [deg]</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;solar_angles</td><td>object</td><td></td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;azimuth_mean</td><td>float</td><td>Mean solar azimuth angle [deg]</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;zenith_mean</td><td>float</td><td>Mean solar zenith angle [deg]</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;surface_altitude_median</td><td>float</td><td>Mean surface elevation (m)</td></tr>
  <tr><td class="level-2">&nbsp;&nbsp;sensor</td><td>object</td><td>"VNIR" or "TIR"</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;sensor_id</td><td>string array</td><td>List of sensor identifiers</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;record_id</td><td>string array</td><td>List of record IDs forming the product</td></tr>

  <!-- bands -->
  <tr><td class="level-3">&nbsp;&nbsp;bands</td><td>dict of objects</td><td></td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;name</td><td>string</td><td>Name of band</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;eo:common_name</td><td>string</td><td>STAC-compliant band name</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;band_centre</td><td>float</td><td>Wavelength of band centre</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;band_width</td><td>float</td><td>Width of the band</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;band_wavelength_unit</td><td>string</td><td>"µm"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;resolutions</td><td>number array</td><td>Spatial resolution for this band</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;resolution_unit</td><td>string</td><td>"m"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;dimensions</td><td>integer array</td><td>Rows and columns of the image</td></tr>

  <!-- esun -->
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;esun</td><td>object</td><td></td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</td><td>float</td><td>Reference irradiance, uncorrected for Earth–Sun distance</td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</td><td>string</td><td>W/m²/µm</td></tr>

  <!-- QA + masks -->
  <!-- <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;qa_mask_id</td><td>string</td><td>Name of QA mask file for this band</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;blackfill_mask_classes</td><td>dict</td><td>Possible values of blackfill mask</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;saturated_mask_classes</td><td>dict</td><td>Possible values of saturated mask</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;untested_mask_classes</td><td>dict</td><td>Possible values of untested mask</td></tr> -->
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;saturated_percentage</td><td>float</td><td>Percentage of saturated pixels</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;nodata_percentage</td><td>float</td><td>Percentage of nodata pixels</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;nottested_percentage</td><td>float</td><td>Percentage of unverified quality pixels</td></tr>

  <!-- products -->
  <tr><td class="level-1">products</td><td>object</td><td></td></tr>

  <!-- L2_VNIR -->
  <tr><td class="level-2">&nbsp;&nbsp;VNIR</td><td>object</td><td></td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;sensor_id</td><td>string array</td><td>List of sensor identifiers</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCO3</td><td>float</td><td>Total ozone column (DU)</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCO3_unit</td><td>string</td><td>"Dobson Unit"</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCO3_source</td><td>string</td><td>"CAMS_fc" / "ERA5"</td></tr>

  <!-- AOT -->
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;AOT</td><td>object</td><td></td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOT_median</td><td>float</td><td>Median AOT value used to retrieve SRs</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOT_unit</td><td>string</td><td>"1"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOT_source</td><td>string</td><td>Source ("constellr_DDV" or "CAMS_fc")</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DDV_percentage</td><td>float</td><td>% of DDV(S) pixels (NA if source is "CAMS_fc")</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOT_file_id</td><td>string</td><td>Filename of L2A AOT product (NA if "CAMS_fc")</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOT_type</td><td>string</td><td>"uint16"; NA if "CAMS_fc"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOT_offset</td><td>float</td><td>Offset to compute AOT from readings (AOT = DN × scale_factor + offset)</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOT_scale_factor</td><td>float</td><td>Scale factor to compute AOT from readings (AOT = DN × scale_factor + offset)</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOT_nodata</td><td>integer</td><td>Fill value</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOT_format</td><td>string</td><td>"COG"; NA if "CAMS_fc"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;topographic_correction</td><td>bool</td><td>Topographic correction applied?</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;adjacency_correction</td><td>bool</td><td>Adjacency correction applied?</td></tr>

  <!-- TCWV -->
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCWV</td><td>object</td><td></td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCWV_median</td><td>float</td><td>Median TCWV used to retrieve SRs</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCWV_unit</td><td>string</td><td>"g/cm²"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCWV_source</td><td>string</td><td>Source ("constellr"/"ERA5"/"CAMS_fc")</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCWV_file_id</td><td>string</td><td>Filename (NA if "ERA5" or "CAMS_fc")</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCWV_type</td><td>string</td><td>"uint16"; NA if "ERA5" or "CAMS_fc"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCWV_offset</td><td>float</td><td>Offset to compute TCWV from readings (tcwv = DN × scale_factor + offset)</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCWV_scale_factor</td><td>float</td><td>Scale factor for TCWV from readings (tcwv = DN × scale_factor + offset); NA if "ERA5" or "CAMS_fc"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCWV_nodata</td><td>integer</td><td>Fill value</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TCWV_format</td><td>string</td><td>"COG"; NA if "ERA5" or "CAMS_fc"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;topographic_correction</td><td>bool</td><td>Topographic correction applied?</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;adjacency_correction</td><td>bool</td><td>Adjacency correction applied?</td></tr>

  <!-- SR -->
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;SR</td><td>object</td><td></td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;topographic_correction</td><td>bool</td><td>Topographic correction applied?</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;adjacency_correction</td><td>bool</td><td>Adjacency correction applied?</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SR_unit</td><td>string</td><td>"1"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SR_type</td><td>string</td><td>"uint16"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SR_offset</td><td>float</td><td>Offset to compute SR from readings (SR = DN × scale_factor + offset)</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SR_scale_factor</td><td>float</td><td>Scale factor to compute SR from readings (SR = DN × scale_factor + offset)</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SR_nodata</td><td>integer</td><td>Fill value</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SR_format</td><td>string</td><td>"COG"</td></tr>

  <!-- Bands -->
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;Bands</td><td>object</td><td></td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eo:common_name</td><td>string</td><td>STAC-compliant band name</td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SR_file_id</td><td>string</td><td>Filename of L2A SR product</td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;clipped_pixels</td><td>integer</td><td>Number of SR pixels clipped to 0 or 1</td></tr>

  <!-- L2_TIR -->
  <tr><td class="level-2">&nbsp;&nbsp;TIR</td><td>object</td><td></td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;sensor_id</td><td>string array</td><td>List of sensor identifiers</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCO3</td><td>float</td><td>Total ozone column (DU)</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCO3_unit</td><td>string</td><td>"Dobson Unit"</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCO3_source</td><td>string</td><td>"CAMS_fc" / "ERA5"</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;AOT_median</td><td>float</td><td>Median AOT used to retrieve LSTs</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;AOT_unit</td><td>string</td><td>"1"</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;AOT_source</td><td>string</td><td>"Fixed"/"constellr_DDV"/"CAMS_fc"</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;AOT_file_id</td><td>string</td><td>Filename of L2A AOT product (NA if "CAMS_fc")</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCWV_median</td><td>float</td><td>Median TCWV used to retrieve LSTs</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCWV_unit</td><td>string</td><td>"g/cm²"</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCWV_source</td><td>string</td><td>"constellr"/"CAMS_fc"/"ERA5"</td></tr>
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;TCWV_file_id</td><td>string</td><td>Filename of L2A TCWV product (NA if "ERA5" or "CAMS_fc")</td></tr>

  <!-- ST -->
  <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;ST</td><td>object</td><td></td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ST_file_id</td><td>string</td><td>Filename of L2A Surface Temperature product</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ST_type</td><td>string</td><td>"uint16"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ST_offset</td><td>float</td><td>Offset to compute ST from readings (st = DN × scale_factor + offset)</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ST_scale_factor</td><td>float</td><td>Scale factor to compute ST from readings (st = DN × scale_factor + offset)</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ST_unit</td><td>string</td><td>"K"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ST_nodata</td><td>integer</td><td>Fill in value</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ST_format</td><td>string</td><td>"COG"</td></tr>
 
  <!-- EMIS -->
  <!-- <tr><td class="level-3">&nbsp;&nbsp;&nbsp;&nbsp;EMIS</td><td>object</td><td></td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_type</td><td>string</td><td>"uint16"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_offset</td><td>float</td><td>Offset to compute emissivity from readings (emis = DN × scale_factor + offset)</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_scale_factor</td><td>float</td><td>Scale factor to compute emissivity from readings (emis = DN × scale_factor + offset)</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_unit</td><td>string</td><td>"1"</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_nodata</td><td>integer</td><td>Fill value</td></tr>
  <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_format</td><td>string</td><td>"COG"</td></tr> -->

  <!-- Bands for EMIS -->
  <!-- <tr><td class="level-4">&nbsp;&nbsp;&nbsp;&nbsp;Bands</td><td>object</td><td></td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eo:common_name</td><td>string</td><td>STAC-compliant band name</td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_file_id</td><td>string</td><td>Filename of L2A emissivity product for this band</td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_prior_vegetation</td><td>float</td><td>Prior emissivity for vegetation</td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_prior_baresoil</td><td>float</td><td>Prior emissivity for bare soil</td></tr>
  <tr><td class="level-5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EMIS_prior_water</td><td>float</td><td>Prior emissivity for water bodies</td></tr> -->

</table> 
