# Constellr LST

Constellr temperature product provides Land surface temperature at both high spatial and temporal
resolution.


## Specification

Constellr LST consists of homogenized rasters of Land Surface Temperature (LST) data. All thermal
datasets are spectrally harmonised using a single algorithm to retrieve LST.
The data is delivered as if it were coming from a single satellite constellation.
The geometry is aligned in all images: all images of a given AOI will show a perfect pixel alignment,
regardless of the source.
Each pixel holds a temperature value. Temperatures are presented in Kelvin degrees.
Pixels that do not contain temperature values hold a ‘nodata’ value. Some zones may show empty pixels in
several or all images, due to issues in the data processing from the public providers. The data comprises,
per scene:


| Product Specifications                |                       |
|---                                    |----:                  |
| Spatial resolution (m)                | 30                    |
| Frequency(days)                       | 8 to 16 days          |
| Coverage                              | Worldwide             |
| Period of availability                | 2018 - ongoing        |
| Thematic accuracy                     |  1.5-3K               |
| Spatial accuracy                      | <1 pixel              |


## File-naming convention

Various layers are provided and follow this compact naming convention:

YYYYMMDDTHHMMSS_aa

Where

-   YYYYMMDDTHHMMSS is the datatake sensing time of the land surface
    temperature in isoformat. Time is based on Universal Time Coordinated (UTC), also
    known as Greenwich Mean Time (GMT).
-   aa indicates what contains the file
    - **LST_AOI.tif**: LST raster
        pixel value: Kelvin Degree
    - **CLOUDS_AOI.tif**: Cloud mask raster
        pixel values: 0=clear pixel, 1=contamined pixel

        cloud mask is made of cloud and shadow pixels
    - **.json**: Metadata json



## Data Sources

Constellr LST30 leverages data from different public missions:

-   Lisr, constellr property
-   Landsat 8 and 9 from USGS
-   Era5 and CAMS from CDSAPI
-   Modis (soon)
-   Sentinel 2 (soon)

*Legal notice: Contains modified Copernicus Sentinel data, Landsat 8 and 9 images (U.S. Geological, Survey), Copernicus Climate Change Service information, Copernicus Service information, modified Modis data (courtesy of the NASA - LP DAAC) and modified Ecostress data (courtesy of the NASA - JPL).*