# **Technical Specifications**
## Overview Product Specifications [^custom-label] {style="margin-bottom: 5px;"}

| Characteristics | [**LSTprecision**](https://constellr.github.io/product-lst/Constellr-product-offer/) |
|------------------------|--------------------------------|
| **Spatial Resolution [^2]** | 30 m     | 
| **Swath**   | 17.5 km    | 
| **Maximum AOI size[^3]**   | Fits within 15x15 km bounding box |
| **Standard scene size[^4]**   | 24 km acquisition strip along track |
| **Frequency [^5]**   | Sub-daily   | 
| **Coverage**| Worldwide tasking, up to 1.000.000 km² daily imaging capacity | 
| **Local acquisition time [^6]**  | 01:30 am/pm <br> 10:30 am/pm   | 
| **Type of images** | Day and night imagery  | 
| **Acquisition Angle**    | Up to 30° | Not applicable | 
| **Temperature accuracy [^7]**  | < 1-2 K with 0.03 K NEDT |
| **Spatial accuracy**          | < 1 px |
| **Data access**           | [API](https://constellr.github.io/product-lst/API-documentation/) or [UI](https://constellr.github.io/product-lst/UI-documentation/) | 
| **Mean Time to Tasking (MTT)**           | Standard: 3 days <br> Priority offer: 24 hours[^8] | 
| **Latency [^9]**     |  Standard: 3 days <br> Priority offer: 24 hours  | 
| **Total request time**     | Sum of (MTT + Revisit Time + Latency) | 
| **Calibration and Validation**           | In-situ data validation following CEOS standards.  Patented cross calibration of HiVE with highly accurate calibrated public missions. <br> [Calibration and Validation](https://constellr.github.io/product-lst/LST-precision-cal-val-procedure/) |




<!-- 
## Capability Statement
This document is intented to always provide you the latest version of our capability statement. Download [here](https://constdataext.blob.core.windows.net/constellr-public/Capability_Statement/Capability_statement_constellr_PUBLIC.pdf).   -->

## Footnotes
[^custom-label]: Performances are only warranted for daytime observations of land surfaces (for islands only if larger than 100 km²) between 50°S and 55°N. All numbers are cloud coverage dependent.
  
[^2]: Defined as resampled pixel size of Land Surface Temperature (LST) products. For LSTprecision native nadir looking Ground Sampling Distance (GSD) at 510 km altitude is 27.3 m for Thermal Infrared data. GSD defined as a pixel projection on ground.  

[^3]: For standard orders adhering to MTT and latency SLAs.

[^4]: For standard orders. Max AOI coverage is ensured within the delivered strip.

[^5]: For LSTprecision frequency relates to the geometric revisit time, defined as the mean number of observation opportunities over a period of 3 months. In 2025 < 4 days is equatorial, < 3 days at ± 40°+ latitudes and < 2 days between ± 60° and ± 80° latitude.  

[^6]: Defined as solar local time, which is time based on the Sun’s actual position in the sky at your location, without considering time zones or daylight saving shifts.  

[^7]: Defined as absolute temperature error. Value defined at Mid-Latitude Summer atmosphere, ground temperature of 295 K, ground cover with emissivity 0.98. High atmospheric water vapour may lead to local deviations in temperature accuracy. The Noise Equivalent Temperature Difference (NETD) is defined as the minimum resolvable temperature difference.   

[^8]: Available for orders placed Monday to Friday, 9.00 am until 4.00 pm Central European Time.

[^9]: Defined as the time between image acquisition by a satellite and delivery of LST data corresponding to the acquisition. 2σ (95%) over 1000 deliveries.​
​
