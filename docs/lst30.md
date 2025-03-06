<h1>Constellr LST30</h1>

Constellr LST30 consists of homogenized rasters of Land Surface Temperature (LST) data. These are their characteristics:

- All thermal datasets are spectrally harmonised using a single in-house algorithm to retrieve LST.
  
- The data are delivered as if they were coming from a single satellite constellation.
  
- The geometry is aligned in all images: all images of an are of interest will show a perfect pixel alignment, regardless of the source. 
  
- Each pixel holds a temperature value in degree Kelvin. 
  
- Pixels that do not contain temperature values hold a ‘nodata’ value. Some zones may show empty pixels in several or all images, due to issues in the data processing from the public providers.

## Data Sources

Constellr LST30 leverages data from different missions:

-   Lisr, constellr property
-   Landsat 8 and 9 from USGS
-   Era5 and CAMS from CDSAPI
-   MODIS (soon)
-   Sentinel 3 (soon)

*Legal notice: Contains modified Copernicus Sentinel data, Landsat 8 and 9 images (U.S. Geological, Survey), Copernicus Climate Change Service information, Copernicus Service information, modified Modis data (courtesy of the NASA - LP DAAC) and modified Ecostress data (courtesy of the NASA - JPL).*  

## Specification

Have a look at our Technical specifications documentation <a href="https://constellr.github.io/product-lst/Technical-specification/" style="color: black;">**Here**</a>


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



=======
## Data Sources {style="color: #123774;margin-bottom: 5px;"}

Constellr LST30 leverages data from different missions:

-   Lisr, constellr property
-   Landsat 8 and 9 from USGS
-   Era5 and CAMS from Copernicus/ECMWF
-   MODIS (soon)
-   Sentinel 3 (soon)

*Legal notice: LST30 is comprised of harmonized LST data that are retrieved  by constellr’s in-house technology. It utilizes proprietary data, as well as raw thermal data acquired by the Landsat missions (courtesy of USGS/ NASA), Ecostress (courtasy of NASA), and climatic data (courtesy of Copernicus/ECMWF).*
