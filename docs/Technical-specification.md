# **Technical Specifications**
## Overview Product Specifications [^custom-label] {style="margin-bottom: 5px;"}

| Characteristics                      | **LSTprecision**                                                                                                                      | **LSTzoom**                                                              | LSTfusion                                                                    |[**LST30**](https://constellr.github.io/product-lst/lst30/)                             |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------|
| **Spatial Resolution [^2]**                   | 30m                                                                                                                               | 5m                                                                  | 30m                                                                          | 30m                               |
| **Swath**                                | 17.5km                                                                                                                            | 17.5km                                                               | Various                                                                      | 110km                             |
| **Scene Size**                           | 15km x 15km                                                                                                                   | 15km x 15km                                                      | 110km x 110km                                                                | 110km x 110km                     |
| **Frequency [^3]**                            | 2025: 1.5 - 3 days <br> 2026: sub-daily                                                                               | 2025: every 1.5-3 days <br> 2026: sub-daily                  | 2025: every 8 days <br> 2026: daily <br> 2027: hourly and forecast                                   | Up to every 8 days                |
| **Coverage**                             | worldwide tasking, up to 1.000.000 km² daily imaging capacity                                                                                                                 | worldwide tasking, up to 1.000.000 km² daily imaging capacity                                                    | Q2 2025: EU, corn belt <br> Q3 2025: India <br> Q4 2025: Worldwide                     | worldwide                         |
| **Local acquisition time [^4]**               | 2025 Q3: 01:30h, 10:30h & 13:30h <br> 2026: 01:30h, 10:30h, 13:30h, 22:30h                                                              | 2025 Q3: 01:30h, 10:30h & 13:30h <br> 2026: 01:30h, 10:30h, 13:30h, 22:30h | 2025: Data delivery for 10:30h UTC <br> 2027: hourly at mid-hour                                                 | 10:30h                            |10:30h
| **Type of images**                       | Day and night imagery                                                                                     | Day and night imagery                        | Day and night imagery                                | day imagery                       |
| **Availability**                         | 2025-ongoing                                                                                                                      | 2025-ongoing                                                         | 2014-ongoing[^5]                                                                 | 2014-ongoing                      |
| **Product Launch Date [^6]**                         | 2025 Q3                                                                                                                           | 2025 Q3                                                              |   2025 Q3                                                                    |                   |
| **Acquisition Angle**                    | up to 30°                                                                                                                         | up to 30°                                                            | various, anisotropy correction planned                                               |                                   |
| **Temperature accuracy [^7]**                 | <1-2K @ 0.03K NEDT                                                                                                                  | <3K                                                                  | <5K                                                                     | <3K                               |
| **Latency [^8]**                              | 2025: <3 days <br> 2026: <24 hrs <br> 2027: <12 hrs                                                                                         | 2025: <3 days <br> 2026: <24 hrs <br> 2027: <12 hrs                            | 2025: < 3 days <br> 2026: NRT (tbd) <br> 2027: forecasting (tbd)                       | < 3 days                          |
| **Calibration and Validation**           | In-situ data validation following CEOS standards.  Patented cross calibration of HiVE with highly accurate calibrated public missions. | In-situ data validation following CEOS standards. Patented cross calibration of HiVE with highly accurate calibrated public missions. |In-situ data validation following CEOS standards. Patented cross calibration of HiVE with highly accurate calibrated public missions.                                                                              | CalVal approach of input datasets |



## Capability Statement
This document is intented to always provide you the latest version of our capability statement. Download [here](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/capability-statement/Capability_statement_KC.pdf)

## Footnotes
[^custom-label]: Performances are only warranted for daytime observations of land surfaces (for islands only if larger than 100 km2) between 50°S and 55°N. All numbers are cloud coverage dependent.
  
[^2]: Defined as resampled pixel size of Land Surface Temperature (LST) products. For LSTprecision and LSTzoom native nadir looking Ground Sampling Distance (GSD) at 510km altitude is 27.3 m for Thermal Infrared data, while GSD for LSTfusion varies with different input data sources. GSD defined as a pixel projection on ground. For LSTzoom higher resolution VNIR bands are used for sharpening to 10m.

[^3]: For LSTprecision and LSTzoom frequency relates to the geometric revisit time, defined as the mean number of observation opportunities over a period of 3 months. In 2025 < 4 days is equatorial, < 3 days at ± 40o+ latitudes and < 2 days between ± 60o and ± 80o latitude. For LSTfusion frequency defines the regularity with which data output is delivered.

[^4]: Defined in UTC at equator with ensured observation time consistency of maximum 1h difference between local time of two acquisitions of a same area or adjusted accordingly. Subject to final orbits and constellation geometry. Applicable only to day-time observations.​

[^5]: Because LSTfusion and LST30 combine data from multiple satellites they can deliver Land Surface Temperature maps starting from 2014 using archived imagery.

[^6]: constellr's first satellite Sky-Bee1 of the HiVE constellation was launched 15.01.2025 and SkyBee's data is the sole input data for LSTprecision and LSTzoom. LSTfusion and LST30 are based on input data from multiple satellites.  

[^7]: Defined as absolute temperature error. Value defined at Mid-Latitude Summer atmosphere, ground temperature of 295K, ground cover with emissivity 0.98. High atmospheric water vapour may lead to local deviations in temperature accuracy. The Noise Equivalent Temperature Difference (NETD) is defined as the minimum resolvable temperature difference. 

[^8]: Defined as the time between image acquisition by a satellite and delivery of LST data corresponding to the acquisition. 2σ (95%) over 1000 deliveries.​
​

