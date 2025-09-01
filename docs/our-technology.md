# **Our Technology** 

## HiVE microsatellites
*Delivering insights never seen before.*  

Our state-of-the-art microsatellite constellation is the **Hi**gh-Precision **V**ersatile **E**cosphere (HiVE) monitoring mission. It is a constellation of microsatellites, the SkyBees. These SkyBees are in the 120 kg class, flying in constellation in a similar sun-synchronous orbital plane. The SkyBees orbit Earth at an altitude between 510 km and 590 km with a goal lifetime of 5 years for each satellite. Overpass time is 10:30 am for SkyBee-1 and 1:30 pm is planned for SkyBee-2. Respective night time aquisitions are shifted for 12 hours. 
 
 
HiVE's aim is to delivers Land Surface Temperature data (LST) at a 1-day global temporal resolution, 30 m spatial resolution in the thermal infrared, and better than 2K absolute temperature accuracy. HiVE aims at providing near-real-time temperature mapping across the planet. If it is visible from space, be it snow, crops, rooftops, or forest canopies, we can track its temperature. The comprehensive thermal intelligence we record acts as both a real-time data source and a continuously updated input for calibrating broader data environments. 

![HiVE Journey](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/Our-technology/Hive-journey.png)
<figcaption>Figure 1: HiVE journey, the past and future of constellr's satellites. </figcaption>

## Mission Snapshot
The HiVE mission is owned and operated by constellr and is deployed in orbit via ride-share procured from a third-party launch provider. The ground segment features multiple ground stations, mission planning, tasking, and constellation management functions, as well as User Request I/O and data processing and storage functions. The uniqueness of HiVE is in providing a quantum leap in payload cost efficiency, leveraging our patented virtual calibration technology. Employing thermally stabilized optical systems, cryo-cooled sensors, and a cooperative approach with existing space infrastructure, allows for measurement accuracy comparable to large satellites on a microsatellite platform. 

![Workflow](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/Our-technology/Work-process-flow.png)
<figcaption>Figure 2: Planning and processing workflow.</figcaption>

## Payload Overview
HiVE’s payload is composed of three main elements: a Thermal Infrared (TIR) Instrument, a Visible and Near Infrared (VNIR) Instrument, and a Data Processing Unit (DPU). A Thermal Control System that includes a Heater Control Unit, a Focus Motor Control Unit, and a radiator, is also part of the payload. The total payload mass is 29.17 kg, margins at subsystem and component levels included. 
 
The payload is designed as a push-frame imaging system, meaning that multiple spectral bands are consecutively recorded in a push-broom configuration while the field of view of the remote sensing instrument sweeps over the surface of Earth.  
 
The payload is designed such that it can operate either in mapping mode, where continuous stripes are recorded, or in targeting mode, where specific targets are pre-selected and then recorded within the field-of-regard of the satellite. 

## TIR & VNIR instruments
*The TIR instrument is HiVE's payload core.*  

The Radiance retrieved by the TIR imager will be transformed to orthorectified Land Surface Temperature using the additional information from the VNIR imager (e.g. geometric information to built the geometric model, Aerosol and Water Vapor information to support the estimation of the atmospheric model and the NDVI to derive a first guess for the emissivity calculations). It achieves a 28.9 m Ground Sampling Distance (GSD) and a 17.5 km swath width at an altitude of 510km. The TIR bands and their central wavelengths, i.e. the wavelength at which the signal is strongest, as well as their respective bandwidth are displayed in Table 1.   

| Filter Number | Central Wavelength [µm] | Bandwidth [nm] |
| ------------- | ----------------------- | --------- |
| 01 | 8.6 | 300 |
| 02 | 9.2 | 300 |
| 03 | 10.6 | 500 |
| 04 | 11.75 | 500 |  
<figcaption>Table 1: Spectral bands in the TIR range.</figcaption>

At a nominal altitude of 510km, the **VNIR camera** has a swath width of 21km with a ground sampling distance of 5m. Thus, the camera covers the complete swath of the TIR instrument and can be used for georeferencing. The data binned on board to, dependent on the band, 10m, 20m or 60m. The segmented spectral bandpass filters provide custom spectral channels aligned with those of the Sentinel-2 satellites. The spectral composition of the bands and their spatial resolution how they are delivered in the final orthorectified products is given in Table 2.

| Filter Number | Central Wavelength [µm] | Bandwidth [nm] | Targeted GSD [m] |
| ------------- | ----------------------- | --------- | ---------------- |
| 01 | 443 | 20 | 60 |
| 02 | 490 | 65 | 10 |
| 03 | 560 | 35 | 10 |
| 04 | 665 | 30 | 10 |
| 05 | 705 | 15 | 20 |
| 06 | 740 | 15 | 20 |
| 07 | 783 | 20 | 20 |
| 08 | 842 | 115 | 10 |
| 09 | 865 | 20 | 20 |
| 10 | 945 | 20 | 60 |
<figcaption>Table 2: VNIR band configuration.</figcaption>

Thus, together, the VNIR and TIR instruments provide 4 thermal and 10 visible and near infrared bands to enable precise geolocation, atmospheric correction, and cloud detection. For an overview of the sensor specifications, see also Figure 3.

![SensorInfo](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/Our-technology/SensorInfo.png)
<figcaption>Figure 3: Overview of the TIR and VNIR sensors.</figcaption>

## Cryocooler Sensor
The cryocooled infrared sensors are at the heart of delivering high-quality, high-resolution thermal data from space. Operating at temperatures around 70 Kelvin (-200°C), these sensors significantly reduce sensor noise, improve signal-to-noise ratios, and ensure minimal thermal drift over time. By cooling the Mercury-Cadmium-Telluride (MCT) detectors to such low temperatures, constellr’s satellites are capable of detecting subtle variations (<0.1K) in thermal energy that are invisible to other commercial thermal EO satellites. 

Cryocooling technology enables constellr’s HiVE satellites to maintain temperature accuracy within 1–2 Kelvin, while offering a 30 m spatial resolution. This level of sensitivity and precision is crucial for applications such as monitoring crop health, managing urban heat islands, and assessing industrial energy efficiency, and civil security. The use of cryocooled sensors ensures that data remains consistent, accurate, and actionable over time.  

## Data Quality and Validation
The HiVE data quality is assessed by defined high standards for all Cal/Val activities. The HiVE Cal/ Val activities are supported by ESA within the ESA programs InCubed and Copernicus Contributing Mission (CCM).  

## Acquisition Scenarios
The HiVE constellation is primarily planned as a tasking-based mission with off-nadir pointing capabilities up to ±30°. For 2025, this enables an average revisit time of 1.5 days with the first two satellites, and reaching sub-daily revisit with three satellites (2026+). 

<!-- ## Key Innovation
constellr’s key innovation is a patented architecture to enable high-quality infrared imaging on microsatellites. So far, this was only possible with bus-sized systems costing hundreds of millions of Euros. Using our pioneering technology, we can reduce the cost of the satellites by a factor of around 30 at comparable performance levels.  

In summary, HiVE’s features allow to ensures absolute temperature accuracy and reliability of the data for high precision analysis. The full constellation of satellites ensures daily coverage for target regions by 2027. Its sunsynchronous orbit ensures comparability of data over time, making it well-suited for trend analysis. Finally, with its day and night imagery, it enabling critical insights for optimal decision-making by 2026.  -->

To learn more about our different products visit our [Product Portfolio](https://constellr.github.io/product-lst/Constellr-product-offer/)

----------

## Capability Statement
This document is intented to always provide you the latest version of our capability statement. Download [here](https://constdataext.blob.core.windows.net/constellr-public/Capability_Statement/Capability_statement_constellr_PUBLIC.pdf).



