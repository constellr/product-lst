# Calibration and Validation approach for LSTprecision 
<br>
The first-generation SkyBee satellites are equipped with two onboard cameras covering the [Visible/Near-Infrared (VNIR) and Thermal Infrared (TIR) spectral ranges](https://constellr.github.io/product-lst/Technical-specification/). Measurements are acquired in ten VNIR bands—comparable to those of Sentinel-2—and four TIR bands between 8 and 12 µm, similar to those planned for the upcoming LSTM and TRISHNA missions. The detectors produce non-interpretable Digital Numbers (DNs), which are converted into accurate, georeferenced radiance measurements through a dedicated calibration and validation (Cal/Val) framework, enabling the retrieval of reliable land surface temperature and surface reflectance  products. The entire calibration and validation chain behind LSTprecision has been independently reviewed as part of an ESA Copernicus mission quality assessment. This confirms that constellr’s processing, auxiliary data usage, and validation approach meet the expectations applied to leading European Earth observation missions and guarantees high level of accuracy from the radiometric and geometric point of views.
 
This Cal/Val framework is designed to characterize the detector response to incoming signals and correct for undesired effects. Key aspects include:  

- Absolute radiometric response, dynamic range, non-uniformity, noise levels, and temporal stability; 
- Detection of damaged pixels; 
- False signals (e.g., stray light or instrument self-emission in TIR); 
- Geometric parameters such as optical alignment, distortion, and Modulation Transfer Function (MTF).  

Cal/Val procedures begin pre-launch, with comprehensive laboratory calibrations in controlled environments. For example, these use a variety of calibrated reference instruments, such as blackbodies for thermal calibration and uniform light sources in the VNIR, to assess the detector responses, optical alignment, and radiometric accuracy. 
 
Post-launch, instrument performance may evolve due to launch effects or aging. Therefore, regular in-orbit calibration procedures are applied during commissioning and routine operations in order to monitor and, when necessary, update the instrument’s performance. These methodologies span a wide range of techniques. 
 
**Geometric orthorectification** follows a two-step approach. First, a systematic correction is applied, which relies on the orbit ephemeris, attitude information and pre-computed calibration parameters. The calibration parameters are computed and continuously updated by analysing images acquired over highly structured areas, such as agricultural regions with regular patterns (e.g., the Dakotas, USA), or over sharp, well-defined features such as coastlines or bridges. These types of scenes serve as reliable references for detecting geometric distortions and verifying spatial accuracy. Together, this first step is assumed to correct the products to an error level of approx. 200 m. 

The second step is a precision modelling for which reference images and a digital elevation model are used to further improve geometric accuracy to a sub pixel level. While the first step is performed for all image products, the second can only be performed successfully in areas where the imaged surface shows sufficient structures to automatically derive a set of correlation points distributed well enough over the whole image take so that an improved geometric model can be created.  

The result of constellr's geometric orthorectification process, i.e. an image's geometric accuracy, is continuously monitored and evaluated by constellr. In Figure 1 and 2 the box and whisker plots present, separately for each of the two cameras (VNIR and TIR), the monthly statistical distribution of the assessed product geometric accuracy after the precision correction has been applied. In these plots, the green lines correspond to the median accuracy, the boxes are formed by the percentiles 25 and 75, and the whiskers represent the remaining 50% of the images after filtering out possible outliers (dots).  
 
In general, these plots show that the median CE95 values are below the 1 pixel accuracy threshold over the operational time for both the TIR camera (30 m GSD) and the VNIR camera (10 m GSD).  
 
Those plots will be updated monthly with the most recent images.  

![Geometric Accuracy 1](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/PUG/monthly_ce95_TIR02_precision+9.png){ width=70% }
<figcaption> Figure 1: TIR CE95 distribution over all precision corrected products </figcaption>

![Geometric Accuracy 2](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/PUG/monthly_ce95_VNIR04_precision+6.png){ width=70% }
<figcaption> Figure 2: VNIR CE95 distribution over all precision corrected products </figcaption>

*Note*: The statistical baseline of this evaluation is all image products which have successfully processed into precision status. The outliers are mostly images where the precision model falsely assumed a good enough correlation point distribution or a high enough number of correlation points. During image QC such images are sorted out and will not be delivered to customers.  
 
**Statistical analyses** are employed to detect dead or bad detector pixels or to correct for possible non-uniformities of the detector. Those are complemented by measurements obtained through specific spacecraft manoeuvres such as 90°-yaw manoeuvre over homogeneous sites or pointing towards the cold deep space support respectively the characterization of detector non-uniformity and dark signal. 
 
**Operational radiometric calibration** in the VNIR range is performed using a vicarious calibration approach. This consists in aligning HiVE top-of-the atmosphere (TOA) radiances with those simultaneously provided by well-characterized, instrumented ground reference sites (e.g. RadCalNet). In the TIR domain, the radiometric calibration relies on a patented cross-calibration approach. It leverages the highly accurate land surface temperature estimates provided by independent geostationary sensors with a high temporal but low spatial resolution. These temperatures are converted to simulated TOA radiances using auxiliary data and radiative transfer modelling. The comparison of the simulated and measured radiances enables the regular update of calibration parameters, ensuring continued accuracy of the thermal measurements.  

In addition to the calibration procedures, the end-user LSTprecision products are regularly assessed using a set of well-established validation methods and protocols, such as the CEOS Best Practices Protocols for Global Surface Albedo and Land Surface Temperature Product Validation [^custom-label]. These protocols provide a harmonized framework for quantitative accuracy assessment, ensuring traceability and consistency across validation efforts.  
 
In addition to the end-user products — namely, surface reflectance and land surface temperature, some supporting geophysical variables are also regularly evaluated. Specifically, it also includes the assessment of the geolocation accuracy, the instruments Modulation Transfer Function (MTF), atmospheric information (AOT and TCWV), and cloud mask quality which are produced as interim products supporting the L2 processing based on VNIR data.  
 
Those validation exercises rely on reference ground-based measurements and independent satellite data coming from different networks or sources as listed in the table below. 

|  | Ground-based | Reference Satellite |Others|
|--|--------------|---------------------|------|
| **Geolocation** | -- | -- | Sentinel-2 GRI |
| **MTF** | -- | -- | Reference Targets |
| **SR** | Radcalnet / (Hypernets) |Sentinel-2 | -- |
| **LST** | Copernicus LAW <br> SURFRAD <br> KIT stations <br> JPL stations <br>  USCRN stations | SEVIRI <br> GOES <br> HIMAWARI | -- |
| **AOT/TCWV** | Aeronet | -- | -- |
<figcaption>Reference data or sites used for assessing the LSTprecision product quality.</figcaption>

<!-- Surface temperatures measured by SkyBee-1 and SkyBee-2 are being compared to the data points from these reference sites, to ensure that the mean deviation will be close to only 1 degree. Such a high accuracy, although challenging to reach, offers opportunities for a large range of use cases based on the detection of thermal anomalies.

<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="https://public-data-213979744349.s3.eu-central-1.amazonaws.com/PUG/PennState_referencesite.png" style="width:45%;">
  <img src="https://public-data-213979744349.s3.eu-central-1.amazonaws.com/PUG/LaCrau_referencesite.png" style="width:45%;">
</div>
<figcaption style="text-align:center;">Example locations of reference sites.</figcaption> -->

The comparison of the surface temperatures measured by SkyBee-1 and Skybee-2 with reference ground data in the near neighbourhood of key validation sites demonstrates the high accuracy of the [LSTprecision product](https://constellr.github.io/product-lst/LST-precision/) both during the day and at night, as shown in Figure 3. Each data point collected over those reference sites during this early phase of the mission matches nicely the reference measurements with a mean deviation being close to only 1 degree. Such a high accuracy, though challenging to reach, offers opportunities for a large range of use cases based on the detection of thermal anomalies.

![LST plot SB01](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/PUG/SBA01_TESlib_Correlation_insitu_starttime20250905_endtime20260616_forKnowledgeCenter+1.png){ width=70% }
<figcaption>Figure 3: Comparison of surface temperatures measured from space by SkyBee-01 with high-quality reference ground data over a few key validation sites. The satellite time series span the period 15th September 2025 to 15th June 2026. We gratefully acknowledge the <a href= https://gml.noaa.gov/grad/surfrad/ >SURFRAD</a>, <a href= https://calval.jpl.nasa.gov/ >JPL data portals</a>, USCRN data portals, and the <a href= https://law.acri-st.fr/home >Copernicus LAW portal</a> as well as the colleagues from KIT-IMKASF for providing the in-situ data.</figcaption>

![LST plot SB02](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/PUG/SBA02_TESlib_Correlation_insitu_starttime20260117_endtime20260616_forKnowledgeCenter+1.png){ width=70% }
<figcaption> Figure 3: Comparison of surface temperatures measured from space by SkyBee-02 with high-quality reference ground data over a few key validation sites. The satellite time series span the period 17th January 2026 to 15th June 2026. We gratefully acknowledge the <a href= https://gml.noaa.gov/grad/surfrad/ >SURFRAD</a>, <a href= https://calval.jpl.nasa.gov/ >JPL data portals</a>, USCRN, and the <a href= https://law.acri-st.fr/home >Copernicus LAW portal</a> as well as the colleagues from KIT-IMKASF for providing the in-situ data.</figcaption>

The cloud and cloud masking algorithm uses the VNIR data as an input. Here the similarity to Sentinel-2 data is exploited. The HiVE cloud algorithm was extensively validated on S2 reference data, for example on the data published in the Cloud Mask Intercomparison eXercise (CMIX)[^2] and is currently partaking in the follow up CMIX II comparison. Here the absolute labelling acuracy as well as class specific accuracies are evaluated. Furthermore, the cloud mask results are visually inspected for HiVE data and will be compared to selected manually labelled cloud masks.

<br>

<p style="text-align: right; font-size: 0.8rem; color: #777;">
  Last update: June, 2026
</p>



## Footnotes
[^custom-label]: Land Product Validation Subgroup (Working Group On Calibration And Validation Committee On Earth Observation Satellites), “Land Surface Temperature Product Validation Best Practice Protocol,” 2017, doi: 10.5067/DOC/CEOSWGCV/LPV/LST.001. 
Land Product Validation Subgroup (Working Group On Calibration And Validation Committee On Earth Observation Satellites), “Global Surface Albedo Product Validation Best Practice Protocol,” 2018, doi: 10.5067/DOC/CEOSWGCV/LPV/ALBEDO.001. 
[^2]: Skakun et al., "Cloud Mask Intercomparison eXercise (CMIX): An evaluation of cloud masking algorithms for Landsat 8 and Sentinel-2", 2022, doi: https://doi.org/10.1016/j.rse.2022.112990 