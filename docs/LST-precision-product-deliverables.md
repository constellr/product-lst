# LSTprecision Data Bundle Description
Constellr's product deliverables include several layers, which are outlined below.

## Data Layers


**Core product data layers** 

| Layers | Description | File Format |
|--------|-------------|-------------|
| lst.tiff | LST data | Cloud optimized geotiff |
| lst_quicklook.tiff | Temperature quicklook | Cloud optimized geotiff |
| lst_thumbnail.jpg | LST Thumbnail | jpg |
| metadata.json | [Metadata description](https://constellr.github.io/product-lst/LST-precision-metadata/) | json |
| scl_mask_30m.tiff | Scene Classification Layer at 30m resolution | Cloud optimized geotiff |


**Option 1: VNIR layers** 

These files are available for free for all daytime imgaes. 

| Layers | Description | File Format |
|--------|-------------|-------------|
| rgb_quicklook.tiff | True color (RGB) quicklook | Cloud optimized geotiff |
| rgb_thumbnail.jpg | RGB Thumbnail | jpg |
| scl_mask_xxm.tiff | Scene Classification Layer at 10m and 20m spatial resolution | Cloud optimized geotiff |
| vnirXX.tiff[^custom-label] |VNIR Surface Reflection for bands 02 - 09 ( see individual band's resolution on [Our Technology](https://constellr.github.io/product-lst/our-technology/)| Cloud optimized geotiff |
| vnirXX_qa.tiff | Quality Assessment Layer for each VNIR band at band's spatial resolution | Cloud optimized geotiff |

**Option 2: Shaprening layer** 

| Layers | Description | File Format |
|--------|-------------|-------------|
| lst_sharpened_10m.tiff | LST data at 10m resolution| Cloud optimized geotiff |
| scl_mask_10m.tiff |Scene Classification Layer at 10m spatial resolution| Cloud optimized geotiff |

<!-- **Option 3: Emissivity layer** 

| Layers | Description | File Format |
|--------|-------------|-------------|
| emi_XX.tiff | Emissivity layers for TIR bands 1-3| Cloud optimized geotiff | -->

## Data Layer Description

<h3>LSTprecision Layer</h3>
LSTprecision's unprecedented temperature sensitivity allows for reliable absolute temperature analysis at 30m - day and night. It is derived from the high-resolution measurements acquired by the SkyBee satellite instruments of [constellr’s HiVe constellation](https://constellr.github.io/product-lst/our-technology/). Following an [advanced calibration and validation (cal/val) procedure](https://constellr.github.io/product-lst/LST-precision-cal-val-procedure/), ensuring highly accurate and well georeferenced radiance data, a sequence of processing steps is applied to generate the full LSTprecision product bundle:

  1. **Cloud and Scene Classification:** 
  A deep learning algorithm relying on a U-net convolutional neural network (CNN), classifies pixels into four cloud-related classes: clear sky, thick cloud, thin cloud, and cloud shadow. Additional masks are also generated to distinguish land and water and to detect terrain cast-shadows. 

  2. **Atmospheric Correction Inputs:** 
  Two key atmospheric parameters are retrieved from the data: 
      - Aerosol Optical Thickness (AOT) using the Dense Dark Vegetation (DDV) method. 
      - Total Column Water Vapor (TCWV) via the Atmospheric Pre-corrected Differential Absorption (APDA) technique.  

        We make use of  high quality and well-established datasets [ERA5](https://doi.org/10.24381/cds.bd0915c6) and [CAMS_forecast](https://doi.org/10.24381/04a0b097) datasets to complement our imagery. We seamlessly leverage the best available source to deliver robust, reliable parameter coverage and consistently high-quality results. 

  3. **Surface Reflectance (SR) Retrieval:** 
  Surface Reflectance is derived from the ten [VNIR bands](https://constellr.github.io/product-lst/our-technology/) using as input the generated masks and atmospheric amounts. The constellr SR algorithm includes corrections for adjacency effects, providing SR with high accuracy for any type of scene, including vegetation, or buildings and infrastructure suitable for a large range of applications.  

  4. **Land Surface Temperature (LST) Retrieval:** 
  The thermal retrieval is based on a library-constrained Temperature–Emissivity Separation (TES) approach. Instead of relying only on VNIR-derived first-guess emissivities, the algorithm evaluates candidate emissivity spectra from a spectral library that has been adapted to the sensor’s thermal bands. For each pixel, the observed thermal radiances are atmospherically corrected and compared against the candidate emissivity spectra to identify the most physically plausible emissivity-temperature combination. Candidate solutions are ranked primarily by inter-band temperature consistency, and the final emissivity is derived from the best-supported subset of candidates. This joint retrieval of LST and emissivity provides a more physically meaningful representation of surface thermal behaviour, particularly over heterogeneous and mixed land-cover types, and supports improved robustness of the final LST product.    

  LST and VNIR surface reflectance are thus Level 2 (L2) products that have gone through various preprocessing levels (see Figure below). Therefore, they represent geophysical values that are scientifically useful and that can be processed into meaningful Earth-surface variables.  

  During night, VNIR data are not available. Therefore, the LSTprecision Level 2 product is made exclusively of the LST layer complemented with cloud and quality masks.   

  ![LSTprecision workflow](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/PUG/LSTprecision_processing_steps_L0_L2.jpg){ width=80% }
  <figcaption>The processing steps from raw data acquisition by Skybee satellites to LSTprecision L2 product. The LSTprecision L2 product consists of the core product as well as the optional add-on layers as outlined in the [Product Offer](https://constellr.github.io/product-lst/Constellr-product-offer/)</figcaption>

<h3>VNIR Surface Reflectance Layers</h3>
Daytime imagery comes with 8 VNIR bands for free. This enables the generation of true-color imagery and the calculation of key spectral indices providing complementary information for more robust temperature analyses.  

Surface reflectance (SR) is delivered at 10m and 20m spatial resolution (see [Our Technology](https://constellr.github.io/product-lst/our-technology/) for each band's resolution). The physical values of reflectance (unitless scaled between 0 and 1) can be obtained by applying the offset and scale factors, as specified in the table below, following:

${SR} = DN * scale factor + offset$

This has been introduced to allow the quantization of floating point numbers up to 1/100% in a 16 bit integer number. The offset value is non-zero to ensure that slightly negative values are not clipped. 
The product is based on the L1B/C product and shows the same geotiff structure as the L1B/C radiance files.

<h3>Quality Assessment Layers</h3>
Quality masks are provided for each of the VNIR and TIR bands as uint8 data at the native spatial resolution of the corresponding band. Those masks report among others the presence of saturated pixels, nodata pixels, or possibly pixels for which the quality could not be tested. 

<h3>Scene Classification Layers</h3>

<h3>Sharpening Layer</h3>
The sharpening layer has a 10m spatial resolution that can provide insights with a 10x improvement in sharpness over today's LST standard.  
The sharpening algorithm creates a 10m resolution LST data layer using as input the nominal HiVE 30m LST data. It is based on the Residual-in-Residual Dense Block (RRDB) network trained using the external HyTEST Land Surface Temperature data sets. It operates without need for any auxiliary guiding bands, relying solely on thermal information. The model is optimized to ensure maintaining pixel accuracy, structural consistency, and edge preservation.  
Consequently, the 10m sharpened layer provides super-resolved LST products that preserve both the absolute thermal values and the spatial patterns necessary for downstream applications.

<!-- <h3>Emissivity Layer</h3>
These layers provide the derived Emissivity (EMIS) values for each of the three thermal bands used in the LST algorithm, as described in Step 4 of the LSTprecision derivation.  

The layers are provided as uint16 Digital Numbers at the spatial resolution of the TIR bands, i.e. 30m. The physical emissivity values (unitless) can be obtained from the DNs by applying offset and scale factors specified in the table below as

${EMIS} = DN* scale factor + offset$

<h3>TIR bands</h3>
TBC -->



| Variable | Data Type | Scale Factor | Offset | Unit | Fill in |
|---|---|---|---|---|---|
|ST|uint16|0.01|0|K|65535|
<!-- |EMIS|uint16|0.0001|0|1|65535| -->
|SR|uint16|0.0001|-0.1|1|65535|
<figcaption>Raster Properties for ST and SR</figcaption>

## Naming Convention

Files, as described above, will be downloaded via a .zip file from the data store. The .zip file will have the following naming convention:

!!! note "Naming convention"
    **<span style="color:blue;">[Acquisition time]</span>** _ **<span style="color:orangered;">[Product]</span>** _ **<span style="color:green;">[data order ID]</span>**

    *Example*  
    **<span style="color:blue;">20240512T095854Z</span>** _ **<span style="color:orangered;">LSTprecision</span>** _ **<span style="color:green;">cae562b6-04a2-48cf-a044-eb61064e4c9b</span>**


[^custom-label]: Band 01 and 10 are excluded, as they do not represent surface information.
<!-- [^2]: The creation of the tcwv.tiff file is not possible if a scene is covered entirely by water or clouds. In this case, no tcwv.tiff file will be available and the SR will rely on modelled data. 
[^3]: The availability of the aot.tiff files for a scene depends on the presence of dark and vegetated pixels in the corresponding scene. If such pixels are not available, the AOT.tiff file will be missing and the SR will rely on modelled data.  -->

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


<br>
<p style="text-align: right; font-size: 0.8rem; color: #777;">
  Last update: June, 2026
</p>