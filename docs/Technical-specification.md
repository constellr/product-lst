# **Technical Specifications**
## Overview Product Specifications [^custom-label] {style="margin-bottom: 5px;"}

| Characteristics | [**LSTprecision**](https://constellr.github.io/product-lst/Constellr-product-offer/) |
|------------------------|--------------------------------|
| **Spatial Resolution [^2]** | 30m     | 
| **Swath**   | 17.5km    | 
| **Scene Size**   | 15km x 15km  |
| **Frequency [^3]**   | sub-daily   | 
| **Coverage**| worldwide tasking, up to 1.000.000 km² daily imaging capacity | 
| **Local acquisition time [^4]**  | 01:30 am/pm <br> 10:30 am/pm   | 
| **Type of images** | day and night imagery  | 
| **Availability**   | 2025 Q3-ongoing  |
| **Acquisition Angle**    | up to 30° | not applicable | 
| **Temperature accuracy [^5]**  | <1-2K with 0.03K NEDT |
| **Spatial accuracy**          | <1 px |
| **Data  availability**      | 2025 - ongoing | 
| **Data access**           | API or download | 
| **Latency [^6]**     | 2026: <12 hrs <br> 2027: <5 hrs    | 
| **Reactivity**     | <3 days <br> H2 2026: <12 hrs <br> 2027: <6 hrs  |  
| **Total request time**     | Sum of the above + revisit time. | 
| **Calibration and Validation**           | In-situ data validation following CEOS standards.  Patented cross calibration of HiVE with highly accurate calibrated public missions. |





## Capability Statement
This document is intented to always provide you the latest version of our capability statement. Download [here](https://constdataext.blob.core.windows.net/constellr-public/Capability_Statement/Capability_statement_constellr_PUBLIC.pdf).  

## Footnotes
[^custom-label]: Performances are only warranted for daytime observations of land surfaces (for islands only if larger than 100 km²) between 50°S and 55°N. All numbers are cloud coverage dependent.
  
[^2]: Defined as resampled pixel size of Land Surface Temperature (LST) products. For LSTprecision and LSTzoom native nadir looking Ground Sampling Distance (GSD) at 510km altitude is 27.3 m for Thermal Infrared data, while GSD for LSTfusion varies with different input data sources. GSD defined as a pixel projection on ground. For LSTzoom higher resolution VNIR bands are used for sharpening to 10m.

[^3]: For LSTprecision and LSTzoom frequency relates to the geometric revisit time, defined as the mean number of observation opportunities over a period of 3 months. In 2025 < 4 days is equatorial, < 3 days at ± 40°+ latitudes and < 2 days between ± 60° and ± 80° latitude. For LSTfusion frequency defines the regularity with which data output is delivered.

[^4]: Defined as solar local time, which is time based on the Sun’s actual position in the sky at your location, without considering time zones or daylight saving shifts.  

[^5]: Defined as absolute temperature error. Value defined at Mid-Latitude Summer atmosphere, ground temperature of 295K, ground cover with emissivity 0.98. High atmospheric water vapour may lead to local deviations in temperature accuracy. The Noise Equivalent Temperature Difference (NETD) is defined as the minimum resolvable temperature difference.   

[^6]: Defined as the time between image acquisition by a satellite and delivery of LST data corresponding to the acquisition. 2σ (95%) over 1000 deliveries.​
​
