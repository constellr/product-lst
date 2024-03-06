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
| Frequency(days)                       | 8                     |
| Coverage                              | Worldwide             |
| Used data sources                     | Public mission        |
| Latency time after data acquisition   | 12h                   |  
| Period of availability                | June 2018 - ongoing   |
| Thematic accuracy                     |  1.5-3K               |
| Spatial accuracy                      | <1 pixel              |


## Output File format

- One LST raster: *_LST_AOI.tif
    pixel value: Kelvin Degree
- One cloud mask: *_CLOUDS_AOI.tif
    pixel values: 0=no cloud, 1=cloud
- One metadata json: *.json