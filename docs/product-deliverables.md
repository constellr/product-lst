# **Product deliverables** {style="color: #123774;margin-bottom: 5px;"}
Constellr's product deliverables include several layers, which are outlined below.


| Product Deliverables               |                       |
|---                                    |----:                  |
| Images files               | TIR and VNIR for your area of interest - cloud optimized geotiff format              |
| Quicklooks for thermal and optical data                       | geotiff format         |
| Metadata file                             | json and xml format, STAC & INSPIRE compliant             |
| Cloud Mask               | geotiff format : pixel values: 0=clear pixel, 1=contamined pixel (both cloud and shadow pixels)      |
| Quality data layer                     |  geotiff format              |
| Thumbnails for thermal and optical data                  |  .jpg format              |

<h2 style= "color: #123774;">Metadata conventions</h2>

The metadata file provided with the constellr products contains various pieces of information that you can retrieve below:


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
| min_lst                    | Minimum LVT value (in Kelvin)                                                                               |
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


Data delivery of al data points through constellr's end-user platform via [**UI download**](https://constellr.github.io/product-lst/UI-documentation/) or [**API**](https://constellr.github.io/product-lst/API-documentation/).

In case you are curious to leverage any of our data layers for your analysis, please refer to the table summarizing the [**technical specifications**](https://constellr.github.io/product-lst/Technical-specification/) for each of our products.