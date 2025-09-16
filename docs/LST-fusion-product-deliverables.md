# **LSTfusion Data Bundle**
Constellr's product deliverables include several layers, which are outlined below.

## Data layers

For the LSTfusion product, each data layer is available for a given data and hour, which is indicate in its file name using the ISO 8601 date-time convention. Hence, the date is indicated at UTC time as follows: yyyymmddThhZ.

| Layers | Description | File Format |
|--------|-------------|-------------|
| metadata_yyyymmddThhZ.json | [Metadata description](https://constellr.github.io/product-lst/LST-fusion-metadata/) | json |
| lst_yyyymmddThhZ.tiff | LST data | Cloud optimized geotiff |
| lst_composite_yyyymmddThhZ.tiff | Temperature quicklook | Cloud optimized geotiff |
| lst_thumbnail_yyyymmddThhZ.jpg | LST Thumbnail | jpg |
| lst_std_yyyymmddThhZ.tiff | Spatial Standard Deviation | Cloud optimized geotiff |


## Naming Convention

- Naming is performed at the point of download  
- In the EUP UI, the full name is not shown as the hierarchy is available in the UI structure.
    - For the example below, we show 'Cloudmask' in the appropriate folder

Files downloaded from the data store follows the following naming convention:

!!! note "Naming convention"
    **[Acquisition time]** _ **<span style="color:orangered;">[Product]</span>** _ **<span style="color:green;">[AOI Name]</span>** _ **[data order ID]** _ **[file name]**

    *Example*  
    **20240512T095854Z** _ **<span style="color:orangered;">LSTfusion</span>** _ **<span style="color:green;">Paris</span>** _ **cae562b6-04a2-48cf-a044-eb61064e4c9b** _ **cloudmask**


<!-- 
| Product Deliverables               |                       |
|---                                    |----:                  |
| Images files               | TIR and VNIR for your area of interest - cloud optimized geotiff format              |
| Quicklooks for thermal and optical data                       | geotiff format         |
| Metadata file                             | json and xml format, STAC & INSPIRE compliant             |
| Cloud Mask               | geotiff format : pixel values: 0=clear pixel, 1=contamined pixel (both cloud and shadow pixels)      |
| Quality data layer                     |  geotiff format              |
| Thumbnails for thermal and optical data                  |  .jpg format              |

<h2>Metadata conventions</h2>

The metadata file provided with the constellr products contains various pieces of information. Find an explanatory table per product below:

[Metadata description for **LSTfusion**]()  
[Metadata description for **LSTprecision**](https://constellr.github.io/product-lst/LST-precision-metadata/)  
[Metadata description for **LSTzoom**]()

---
Data delivery of all data points through constellr's end-user platform via [**UI download**](https://constellr.github.io/product-lst/UI-documentation/) or [**API**](https://constellr.github.io/product-lst/API-documentation/).

In case you are curious to leverage any of our data layers for your analysis, please refer to the table summarizing the [**technical specifications**](https://constellr.github.io/product-lst/Technical-specification/) for each of our products. -->



<!-- 
| Metadata field             | Definition                                                                                                 |
|----------------------------|-------------------------------------------------------------------------------------------------------------|
| area_of_interest_id        | Internal aoi id                                                                                             |
| area_of_interest_name      | Internal aoi name                                                                                           |
| organization_id            | Internal organization id                                                                                    |
| bbox                       | bbox coordinates of the Area of Interest                                                                    |
| l1_item_href               | Landsat l1 data source                                                                                      |
| l2_item_href               | Landsat l2 data source                                                                                      |
| scene_datetime             | Image acquisition datetime                                                                                  |
| processing_datetime        | Start of constellr processing image datetime                                                                |
| cloud_ratio_aoi            | Percentage of cloud cover over the aoi                                                                      |
| na_ratio_aoi               | Percentage of nan values over the aoi                                                                       |
| min_lst                    | Minimum LST value (in Kelvin)                                                                               |
| max_lst                    | Maximum LST value (in Kelvin)                                                                               |
| median_lst                 | Median LST value (in Kelvin)                                                                                |
| sun_elevation              | Sun's elevation angle for a given geographical bounding box and time                                        |
| proj:epsg                  | Reference projection in epsg                                                                                |
| proj:shape                 | The shape of the spatial object in terms of the width and height, or the dimensions of the ara covered      |
| proj:transform             | The transformation matrix that is used to transform coordinates between different spatial reference systems |
| sat_source                 | Public data source used for satellite sensors                                                               |
| atm_source                 | Public data source used for atmospheric data                                                                |
| requested_area_of_interest | Coordinates of the AOI requested (Polygon)                                                                  |
| geometry                   | Coordinates of the Polygon returned                                                                         |
 -->