# **LST precision** 
<br>

??? note "What is LSTprecision?"
      LSTprecision delivers exceptional satellite-based land surface temperature sensitivity and details, enabling accurate absolute temperature measurements. It is designed for precise thermal data, making it ideally suited for urban, vegetation, and industrial analyses with new levels of coverage, detail, and accuracy.  LSTprecision also delivers co-registered accurate surface reflectance measurements across ten visible and near-infrared bands. This enables for example the generation of true-color imagery and the calculation of key vegetation indices providing complementary information for more robust temperature analyses.  

 
??? note "When should you use LSTprecision?"
    - *Protect high-value assets:* Get asset-level insights with accurate thermal data, not just rough indices or proxies. 
    - *Detect issues before they escalate:* Our system acts as an early-warning tool, spotting stress in environments, infrastructure, and materials before damage occurs. 
    - *Rely on unmatched temperature accuracy:* With absolute precision of <2K, you can trust your data to be consistent, comparable, and reliable over time. 
    - *See what others miss:* A sensitivity of 0.03K uncovers subtle thermal shifts, ensuring confident detection of both relative and absolute changes. 
    - *Track trends with confidence:* High-frequency revisits (as often as every 3 days in daylight) deliver rich time-series data, enabling timely identification of anomalies and long-term patterns. 

    Want even sharper local detail? → [Explore LSTzoom](Link)  
    Need broader, cloud-free daily coverage? → [Discover LSTfusion](Link) 

??? note "How is LSTprecision created?"
    LSTprecision is derived from the high-resolution measurements acquired by the SkyBee satellite instruments of constellr’s HiVe constellation (Link to our technology page). Following an advanced calibration and validation (cal/val) procedure link to Cal/Val procedure, ensuring highly accurate and well georeferenced radiance data, a sequence of processing steps is applied to generate the full LSTprecision product bundle. 

    1. **Cloud and Scene Classification:** 
    A deep learning algorithm relying on a U-net convolutional neural network (CNN)1  , classifies pixels into four cloud-related classes: clear sky, thick cloud, thin cloud, and cloud shadow. Additional masks are also generated to distinguish land and water and to detect terrain cast-shadows. 

    2. **Atmospheric Correction Inputs:** 
    Two key atmospheric parameters are retrieved from the data: 
        - Aerosol Optical Thickness (AOT) using the Dense Dark Vegetation (DDV) method. 
        - Total Column Water Vapor (TCWV) via the Atmospheric Pre-corrected Differential Absorption (APDA) technique.  
  
         We make use of  high quality and well established datasets [ERA5](https://doi.org/10.24381/cds.bd0915c6) and [CAMS_forecast](https://doi.org/10.24381/04a0b097) datasets to complement our imagery. Depending on availability, we seamlessly draw from either source, ensuring robust and reliable parameter coverage with consistently high-quality results. 

    3. **Surface Reflectance (SR) Retrieval:** 
    Surface Reflectances are derived from the ten VNIR bands (link to our technology page) using as input the generated masks and atmospheric amounts. The constellr SR algorithm includes corrections for adjacency and terrain using topographic data ([Copernicus GLO30 DEM](https://doi.org/10.5069/G9028PQB)), providing SR with high accuracy for any type of scenes, including vegetation, or buildings and infrastructure suitable for a large range of applications.  

    4. **Land Surface Temperature (LST) Retrieval:** 
    The VNIR SRs are derived from the satellite footprints and used to estimate an initial (first-guess) emissivity for each of the four thermal bands (link to technology page). Those are used as input of the constellr LST algorithm, relying on the Equivalent Temperature Approach (ETA), to derive the land surface temperature and to optimize the surface emissivity’s. The simultaneous retrieval of LST and emissivity’s enhance the overall LSTprecision product accuracy. 

    IMAGE

??? note "What are the specifications of LSTprecision?"
    |Parameter|Value|
    |---------|-----|
    |Spatial Resolution|TIR: 30m, VNIR:10m|
    |Temporal Resolution| 1.5-3 days|
    |Output Time| 10:30 or 13:30 local solar time|
    |Coverage Area|Worldwide tasking, up to 1.000.000 km² daily imaging capacity, AOI maximum size: 15x15 km² |
    |Output Format| GeoTIFF + Metadata geojson, ARD-compliant|

    For more see the [Technical Specifications](https://constellr.github.io/product-lst/Technical-specification/) page.

??? note "How accurate is LSTprecision?"
    Thanks to the robust Cal/Val approach combined with state-of-the art algorithm processors, the SkyBee data offer a high level of accuracy from the radiometric and geometric point of views. The SkyBee satellites use two cameras to capture both visible/near-infrared and thermal infrared images of Earth, similar to the capabilities of other leading observation missions (link to our technology page).  LST and SR are provided with an absolute accuracy better than 2°K and 5%, respectively, for most clear sky geophysical conditions and with a geolocation accuracy better than XXm. 

    Achieving high accuracy starts well before launch with a proper characterization of the instruments in the lab, and continues in space with a regular verification of the instrumental performances. Engineers monitor and correct for changes over time, detect faulty pixels, and adjust for geometric distortions using well-known landscapes and landmarks. Calibration draws on trusted ground reference sites for visible/near-infrared data and patented methods comparing thermal readings with reliable satellite temperature measurements, guaranteeing data remain precise and reliable throughout the mission.  Accuracy of end-user products is also regularly evaluated against ground-truth measurements at a series of reference sites part of different official networks.  Explore the details of our Cal/Val approach. 

??? note "What to look forward to in future developments?"
      
    **Night time LST imagery**  
    In Q4 2025, LSTprecision will also provide nighttime land surface temperature data—offering valuable insights for various urban, defence, and intelligence applications.  With output times at 22:30 and 01:30  local time, the temporal resolution will be improved to less than one day.  
    
    **Higher revisit frequency**   
    SkyBee-03 is already in the pipeline, with a launch scheduled for mid-2026. It will further reduce revisit times while having the high performance of our first two SkyBee instruments.  
    
    **Towards a higher spatial resolution**  
    The next generation of instruments is already in development, promising enhanced performance, such as higher native spatial resolution, to deliver even greater impact for your applications. 


??? note "What is included in the product bundle?"






