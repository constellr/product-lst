<h1>Constellr LST30</h1>  

<br>

Prior to the launch of HiVE’s satellites, constellr has been preparing for HiVE’s data since 2022. constellr developed sapproaches to derive LST from thermal data including LisR, to assess and validate the use of LST data for various [use-cases](https://constellr.github.io/product-lst/demo/), and finally to understand the impact that HiVE would bring to each solution. Thus, constellr developed its first product, LST30, that consists of homogenized rasters of LST acquired from various thermal public missions along with available proprietary data. LST30 is comprised of harmonized LST data that are retrieved by constellr’s in-house technology. It utilizes proprietary data (LisR), as well as raw thermal data acquired by the Landsat 8 and 9 missions (courtesy of U.S. Geological Survey), Ecostress (courtesy of NASA - JPL), and climatic data (courtesy of the Copernicus Climate Change Service/ECMWF). Yet, the data are delivered as if they were coming from a single satellite constellation with perfect pixel alignment in all images, regardless of the source.    

Leveraging thermal data of LST30 has been a success, where the potential of LST has been highlighted for enhancing smart agriculture, monitoring urban heat islands, and optimizing infrastructure resilience. By validating the reliability and applicability of the data, cosntellr has ensured the effective integration of spaceborne LST in diverse, real-world scenarios, driving impact across multiple sectors.  

**Key Technical Characteristics of LST30:**  

| Characteristics | LST30 |
| --------------- | ----- |
| Spatial resolution | 30m |
| Spatial coverage | Worldwide|
| Scence size | 110km x 110km |
| Temporal resolution | 8 days |
| Temporal archive | 2014 - ongoing|
| Bands | LST <br> Cloud Mask |  

For more details and a comparison with our other products, have a look at our Technical specifications documentation <a href="https://constellr.github.io/product-lst/Technical-specification/" style="color: black;">**here**</a>.  

**Various layers are provided and follow this compact naming convention:**

| Filename part | Meaning |
| ------------- | ------- |
| YYYYMMDDTHHMMSS | Time of sensing LST in isoformat. <br> Time is based on Universal Time Coordinated (UTC), also known as Greenwhich Mean Time (GMT). |
| aa | Indicates what the file contains: <ul><li> **LST_AOI.tif**: LST raster <br> pixel value: Kelvin Degree or 'nodata' in case of issues in the data processing from the public providers </li><li>**CLOUDS_AOI.tif**: Cloud mask raster <br> pixel values: 0=clear pixel, 1=contamined pixel <br> cloud mask is made of cloud and shadow pixels</li><li> **.json**: Metadata json </li></ul> |