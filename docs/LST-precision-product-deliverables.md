# **LSTprecision Data Bundle**
Constellr's product deliverables include several layers, which are outlined below.

## Data layers

| Layers | Description | File Format |
|--------|-------------|-------------|
| metadata.json | [Metadata description](https://constellr.github.io/product-lst/LST-precision-metadata/) | json |
| vnir_data/vnir01.tiff - vnir10.tiff |VNIR Surface Reflection per band at 30m and 60m resolution| Cloud optimized geotiff |
| tir_data/lst.tiff | LST data | Cloud optimized geotiff |
| rgb_composite.tiff | True color (RGB) quicklook | Cloud optimized geotiff |
| lst_composite.tiff | Temperature quicklook | Cloud optimized geotiff |
| rgb_thumbnail.jpg | RGB Thumbnail | jpg |
| lst_thumbnail.jpg | LST Thumbnail | jpg |
| scl_masks_data/scl_mask_XXm.tiff | Scene Classification Layer (e.g. vegetation, water) at 30m and 60m resolution | Cloud optimized geotiff |
| vnir_data/tcwv.tiff | Total Column Water Vapour | Cloud optimized geotiff |
| vnir_data/aot.tiff | Aerosol Optical Thickness | Cloud optimized geotiff |

## Naming Convention

Files, as described above, will be downloaded via a .zip file from the data store. The .zip file will have the following naming convention:

!!! note "Naming convention"
    **<span style="color:blue;">[Acquisition time]</span>** _ **<span style="color:orangered;">[Product]</span>** _ **<span style="color:green;">[data order ID]</span>**

    *Example*  
    **<span style="color:blue;">20240512T095854Z</span>** _ **<span style="color:orangered;">LSTprecision</span>** _ **<span style="color:green;">cae562b6-04a2-48cf-a044-eb61064e4c9b</span>**




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