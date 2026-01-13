# **LSTfusion** 
<br>

??? note "What is LSTfusion?"
      LSTfusion is an advanced land surface temperature (LST) fusion product, integrating multiple satellite observations across different resolutions and times into a seamless, high-resolution (30m) and temporally harmonized dataset, offered daily at 11am local solar time.     

 
??? note "When should you use LSTfusion?"
    - *Get the full picture, every day:* Seamless, spatially and temporally consistent temperature data at 30m resolution, delivered daily at 11am local time.   
    - *No gaps, no blind spots:* Clouds or missing inputs will not stop your analysis. Fusion technology fills gaps to create uninterrupted, reliable datasets.  
    - *Benchmark and compare with confidence:* track long-term trends across regions, surfaces, or objects with detailed thermal profiles and accumulated temperature curves.   
    - *Scale from local to national:* Perform regional and national comparisons, then zoom in with HiVE or other high-resolution imagery for detailed asset-level insights.   
  
Need asset-level precision for critical infrastructure? → [Explore LSTprecision](https://constellr.github.io/product-lst/LST-precision/)  
Want to visually detect fine-grained variations locally? → [Explore LSTzoom](link)

??? note "How is LSTfusion created?"
    LSTfusion is the result of combining dynamic diurnal cycle modelling, spatial upscaling techniques, and data assimilation using Kalman filtering. This powerful integration allows us to generate high-resolution, temporally consistent LST data, even when satellite observations are incomplete or missing. It represents a significant achievement, built on advanced research and deep domain expertise.  
    
    LSTfusion uses a combination of the highest quality thermal datasets as input:   
    
    - **Moderate-resolution sensors:** MODIS , VIIRS (Level 2 swath LST product).  
    - **High-resolution sensors:** Landsat 8/9 LST is derived using constellr’s in-house algorithm, combining dynamic emissivity maps with advanced atmospheric correction to deliver sharper, more accurate, and contextually relevant temperature details.  
    - **Geostationary datasets:** CLMS (Copernicus L3 LST at 5km based on e.g. SEVIRI, GOES, Himawari).  

    **The key processing components in LSTfusion include:**  
    
    1. **The VNIR Fusion**  
    This component generates a continuous high-resolution Normalized Difference Vegetation Index (NDVI) and Short-Wave Infra-red (SWIR) data by harmonizing and fusing multi-sensor VNIR observations. It combines multiple VNIR data sources into a harmonized reflectance dataset. It utilizes HLS (Harmonized Landsat + Sentinel-2) for consistent reflectance and Sentinel-2 Global Mosaic as static seasonal NDVI reference. The approach computes monthly mosaics from harmonized scenes by applying 3D temporal interpolation to reduce gaps.  
    
    2. **Diurnal Temperature Cycle (DTC) Modelling**  
    The DTC model simulates temperature changes throughout the day using a curve based on Gaussian and reciprocal functions. The model provides a complete hourly LST prediction even where direct observations are missing and is applied in two modes:  
        - Low-resolution: using hourly CLMS data  
        - Moderate-resolution: combining MODIS and VIIRS data  
    
    3. **Resolution Enhancement (Upsampling)**  
    Upsampling in LSTfusion is the process of transferring information from high-resolution predictors (e.g. NDVI, SWIR) to low- or medium-resolution LST products, producing harmonized LST outputs at 30 m scale. This component ensures spatial consistency across the pipeline, reduces oversmoothing, and prepares LST inputs for assimilation. A Ridge Regression method ingests multiple features (including NDVI + SWIR).  

    4. **Data Assimilation**  
    Data assimilation is based on a vectorized Kalman filter. Its objective is to optimally estimate the land surface temperature (LST) and its diurnal trend at high resolution by combining predictive modelling with satellite observations of varying resolutions.  
    The system operates on an hourly timestep. At each step, the filter:  
        1. Predicts the thermal state forward in time using the dynamic model.  
        2. Assimilates available observations from low-, medium- (upsampled), and high-resolution data sources (e.g., Landsat, Skybee) when possible.  
        3. Adapts uncertainties using observation-specific covariance structures and distance-based Gaussian smoothing.  
        4. Falls back to model propagation with uncertainty inflation if no valid observations are available. 

    ![LSTfusion workflow](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/PUG/lstfusion.png){ width=80% }
    <figcaption>The processing steps from raw data acquisition by Skybee satellites to LSTfusion L3 product.</figcaption>


??? note "What are the specifications of LSTfusion?"
    |Parameter|Value|
    |---------|-----|
    |Spatial Resolution|TIR: 30m |
    |Temporal Resolution| Daily |
    |Output Time| 11:00 am local solar time |
    |Coverage Area| Configurable AOI |
    |Output Format| GeoTIFF + Metadata geojson |

    For more see the [Technical Specifications](https://constellr.github.io/product-lst/Technical-specification/) page.

??? note "How accurate is LSTfusion?"
    LSTfusion delivers real, physically meaningful temperature values — not just relative digital numbers. Each data point represents an actual estimate of land surface temperature, expressed in degrees Kelvin, and ready for direct use in scientific analysis, modeling, and decision-making. We target an accuracy better than 5K, and under clear-sky conditions.  
    
    Each LSTfusion image provided to you is also accompanied by a quality layer that lets you assess confidence in the data at every pixel. We are also actively validating the product against ground-based measurements and satellite references to ensure you can rely on it not just for visualization, but for real, quantitative insight. Explore the details of our [validation approach](https://constellr.github.io/product-lst/LST-fusion-cal-val-procedure/).  


??? note "What to look forward to in future developments?"
      
    We have lots of plans to make LSTfusion even more powerful  
    
    - to become an hourly dataset to help you follow everything you need throughout the day  
    - to provide forecasts so you can better plan your activities  
    - to include further thermal datasets from our proprietary data of the HiVE constellation for the highest detail  
    - to include Sentinel-3 data and future missions such TRISHNA, LSTM and possibly SBG (to remain as the state-of-the-art)  





<br>
<p style="text-align: right; font-size: 0.8rem; color: #777;">
  Last update: January, 2026
</p>

