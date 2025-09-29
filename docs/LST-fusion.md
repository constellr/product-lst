# **LSTfusion** 
<br>

??? note "What is LSTfusion?"
      LSTfusion is an advanced land surface temperature (LST) fusion product, integrating multiple satellite observations across different resolutions and times into a seamless, high-resolution (30m) and temporally harmonized dataset, offered daily at 11am local solar time.     

 
??? note "When should you use LSTfusion?"
    - *Get the full picture, every day:* Seamless, spatially and temporally consistent temperature data at 30m resolution, delivered daily at 11am local time.   
    - *No gaps, no blind spots:* Clouds or missing inputs will not stop your analysis. Fusion technology fills gaps to create uninterrupted, reliable datasets.  
    - *Benchmark and compare with confidence:* track long-term trends across regions, surfaces, or objects with detailed thermal profiles and accumulated temperature curves.   
    - *Scale from local to national:* Perform regional and national comparisons, then zoom in with HiVE or other high-resolution imagery for detailed asset-level insights.   
  
    Prefer highly accurate temperature benchmarks over time? → [Explore LSTprecision](link)  
    Want to visually detect fine-grained variations locally? → [Explore LSTzoom](link)   

??? note "How is LSTfusion created?"
    LSTfusion is the result of combining dynamic diurnal cycle modelling, spatial upscaling techniques, and data assimilation using Kalman filtering. This powerful integration allows us to generate high-resolution, temporally consistent LST data, even when satellite observations are incomplete or missing. It represents a significant achievement, built on advanced research and deep domain expertise.  
    
    LSTfusion uses a combination of the highest quality thermal datasets as input:   
    
    - **Moderate-resolution sensors:** MODIS , VIIRS (Level 2 swath LST product).  
    - **High-resolution sensors:** Landsat 8/9 LST is derived using constellr’s in-house algorithm, combining dynamic emissivity maps with advanced atmospheric correction to deliver sharper, more accurate, and contextually relevant temperature details.  
    - **Geostationary datasets:** CLMS (Copernicus L3 LST at 5km based on e.g. SEVIRI, GOES, Himawari).  

    The key processing components in LSTfusion include:  
    
    **Diurnal Temperature Cycle (DTC) Modelling**  
    
    The DTC model simulates temperature changes throughout the day using a curve based on Gaussian and reciprocal functions. It is applied in two modes:  
    
    - Low-resolution: using hourly CLMS data  
    - Moderate-resolution: combining MODIS and VIIRS data  

    The model provides a complete hourly LST prediction even where direct observations are missing.  

    **Resolution Enhancement (Upsampling)**  
    
    DTC parameters are enhanced to 30 m resolution by leveraging the correlation between vegetation cover and LST. Vegetation cover is determined by the Normalized Difference Vegetation Index (NDVI) at 30m resolution that utilizes red and near infra-red bands to best capture vegetation features. The following steps are followed:  
    
    - A local polynomial model is fitted between low-resolution DTC and high-resolution NDVI. 
    - This relationship is used to infer high-resolution DTC fields. 
    - Results are fused spatially to preserve continuity and accuracy. 

    **Data Assimilation**  
    
    Finally, we integrate all data sources using a Kalman filter-based assimilation system that blends model predictions with high-res observations from the Landsat data, i.e. of the highest resolution:  
    
    - Tracks LST and its rate of change per pixel.  
    - Adjusts uncertainty dynamically based on observation quality and availability.  
    - Produces robust, spatially coherent thermal maps.  

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
    LSTfusion delivers real, physically meaningful temperature values—not just relative digital numbers. Each data point represents an actual estimate of land surface temperature, expressed in degrees Kelvin, and ready for direct use in scientific analysis, modeling, and decision-making.  
    
    We target an accuracy better than 5°K, and under clear-sky conditions, performance is often even better. While certain factors such as persistent cloud cover, snow, or complex topography can affect precision, we have built in safeguards. Each LSTfusion image provided to you also is accompanied by a quality layer that lets you assess confidence in the data at every pixel.  

    ![Graph](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/PUG/PUG_Graph.png){ width=60% }
    <figcaption>Scatter plot comparing LSTfusion output with Russell Ranch ground observations.</figcaption> 

    We are also actively validating the product against ground-based measurements and satellite references to ensure you can rely on it not just for visualization, but for real, quantitative insight. 

??? note "What to look forward to in future developments?"
      
    We have lots of plans to make LSTfusion even more powerful  
    
    - to become an hourly dataset to help you follow everything you need throughout the day  
    - to provide forecasts so you can better plan your activities  
    - to include further thermal datasets from our proprietary data of the HiVE constellation for the highest detail  
    - to include Sentinel-3 data and future missions such TRISHNA, LSTM and posssibly SBG (to remain as the state-of-the-art)  

??? note "What is included in the product bundle?"




<br>
<p style="text-align: right; font-size: 0.8rem; color: #777;">
  Last update: September, 2025
</p>

