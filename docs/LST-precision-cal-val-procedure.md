# Cal/Val approach for LSTprecision 
<br>
The first-generation SkyBee satellites are equipped with two onboard cameras covering the [Visible/Near-Infrared (VNIR) and Thermal Infrared (TIR) spectral ranges](https://constellr.github.io/product-lst/Technical-specification/). Measurements are acquired in ten VNIR bands—comparable to those of Sentinel-2—and four TIR bands between 8 and 12 µm, similar to those planned for the upcoming LSTM and TRISHNA missions. The detectors produce non-interpretable Digital Numbers (DNs), which are converted into accurate, georeferenced radiance measurements through a dedicated calibration and validation (Cal/Val) framework, enabling the retrieval of reliable land surface temperature and surface reflectance  products. 
 
This Cal/Val framework is designed to characterize the detector response to incoming signals and correct for undesired effects. Key aspects include:  

- Absolute radiometric response, dynamic range, non-uniformity, noise levels, and temporal stability; 
- Detection of damaged pixels; 
- False signals (e.g., stray light or instrument self-emission in TIR); 
- Geometric parameters such as optical alignment, distortion, and Modulation Transfer Function (MTF).  

Cal/Val procedures begin pre-launch, with comprehensive laboratory calibrations in controlled environments. For example, these use a variety of calibrated reference instruments, such as blackbodies for thermal calibration and uniform light sources in the VNIR, to assess the detector responses, optical alignment, and radiometric accuracy. 
 
Post-launch, instrument performance may evolve due to launch effects or aging. Therefore, regular in-orbit calibration procedures are applied during commissioning and routine operations in order to monitor and, when necessary, update the instrument’s performance. These methodologies span a wide range of techniques. 
 
Geometric performance and associated calibration parameters are generally updated by analysing images acquired over highly structured areas—such as agricultural regions with regular patterns (e.g., the Dakotas, USA) — or over sharp, well-defined features such as coastlines or bridges. These types of scenes serve as reliable references for detecting geometric distortions and verifying spatial accuracy. 
 
Statistical analyses are employed to detect dead or bad detector pixels or to correct for possible non-uniformities of the detector. Those are complemented by measurements obtained through specific spacecraft manoeuvres such as 90°-yaw manoeuvre over homogeneous sites or pointing towards the cold deep space support respectively the characterization of detector non-uniformity and dark signal. 
 
Operational radiometric calibration in the VNIR range is performed using a vicarious calibration approach. This consists in aligning HiVE top-of-the atmosphere (TOA) radiances with those simultaneously provided by well-characterized, instrumented ground reference sites (e.g. RadCalNet). In the TIR domain, the radiometric calibration relies on a patented cross-calibration approach. It leverages the highly accurate land surface temperature estimates provided by independent geostationary sensors with a high temporal but low spatial resolution These temperatures are converted to simulated TOA radiances using auxiliary data and radiative transfer modelling. The comparison of the simulated and measured radiances enables the regular update of calibration parameters, ensuring continued accuracy of the thermal measurements.  

In addition to the calibration procedures, the end-user LSTprecision products are regularly assessed using a set of well-established validation methods and protocols, such as the CEOS Best Practices Protocols for Global Surface Albedo and Land Surface Temperature Product Validation [^custom-label]. These protocols provide a harmonized framework for quantitative accuracy assessment, ensuring traceability and consistency across validation efforts.  
 
In addition to the end-user products — namely, surface reflectance and land surface temperature, some supporting geophysical variables are also regularly evaluated. Specifically, it also includes the assessment of the geolocation accuracy, the instruments Modulation Transfer Function (MTF), atmospheric information (AOT and TCWV), and cloud mask quality which are produced as a interim products supporting the L2 processing based on VNIR data.  
 
Those validation exercises rely on reference ground-based measurements and independent satellite data coming from different networks or sources as listed in the table below. 

|  | Ground-based | Reference Satellite |
|--|--------------|---------------------|
| **Geolocation** | - | - |
| **MTF** |  |  |
| **SR** | Radcalnet / (Hypernets) |Sentinel-2 |
| **LST** | Copernicus LAW <br> SURFRAD <br> KIT stations <br> JPL stations | SEVIRI <br> GOES <br> HIMAWARI |
| **AOT/TCWV** | Aeronet |  |
<figcaption>Reference data or sites used for assessing the LSTprecision product quality.</figcaption>

The cloud and cloud masking algorithm uses the VNIR data as an input. Here the similarity to Sentinel-2 data is exploited: The HiVE cloud algorithm was extensively validated on S2 reference data, for example on the data published in the [Cloud Mask Intercomparison eXercise (CMIX)](https://www.sciencedirect.com/science/article/pii/S0034425722001043) and is currently partaking in the follow up CMIX II comparison. Here the absolute labelling acuracy as well as class specific accuracies are evaluated. Furthermore, the cloud mask results are visually inspected for HiVE data and will be compared to selected manually labelled cloud masks.


## Footnotes
[^custom-label]: Land Product Validation Subgroup (Working Group On Calibration And Validation Committee On Earth Observation Satellites), “Land Surface Temperature Product Validation Best Practice Protocol,” 2017, doi: 10.5067/DOC/CEOSWGCV/LPV/LST.001. 
Land Product Validation Subgroup (Working Group On Calibration And Validation Committee On Earth Observation Satellites), “Global Surface Albedo Product Validation Best Practice Protocol,” 2018, doi: 10.5067/DOC/CEOSWGCV/LPV/ALBEDO.001. 