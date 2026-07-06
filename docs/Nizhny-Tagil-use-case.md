<h1 <span style="color: #202A78;margin-bottom: 5px;">Monitoring of patterns over industrial assets</span></h1>  

<br>

## Detecting sludge deposits in Nizhny Tagil - a thermal indicator of industrial activity

<div style="display: flex; align-items: flex-start; justify-content: flex-start; gap: 20px;">
<div style="flex: 1;">
    <img src="https://public-data-213979744349.s3.eu-central-1.amazonaws.com/NizhnyTagil_Use_Case_Story/NizhnyTagil_Location.png" alt="Thermal Overview" style="max-width: 400px; height: auto;">
    <figcaption>Figure 1: Location of Nizhny Tagil</figcaption>
</div>
<div style="flex: 2;">
    <p>
    Nizhny Tagil, Sverdlovsk Oblast, is a major industrial city in the Ural region with a focus on metallurgy, heavy machinery, chemical production, and energy-related facilities. Key industrial assets include steel and alloy plants, mechanical workshops, chemical installations, sludge and waste processing units, and high-temperature thermal processes like furnaces and smelters. 
    
    However, open-source information on facility operations, production levels, or waste management practices is extremely limited, particularly for defense-related or dual-use installations. Hence, the objective of this study is to leverage thermal satellite data to:  
    - Delineate spatial thermal hotspots within the industrial complex; 
    - Identify abnormal or episodic heat signatures linked to production and processing activity; 
    - Detect persistent heat sources indicative of continuously operating infrastracture. 
    </p>
</div>
</div> 

Attention is given to the **sludge processing unit**, which exhibits dominant and sustained thermal signatures with very high LST values of more than 75°C. Persistent thermal hotspots correspond to continuous operations in smelting, furnace activity, and sludge treatment, while intermittent anomalies likely reflect batch production or maintenance. Open-source information on operational schedules and production volumes is very limited. Thermal satellite data provide a practical means to map heat signatures, identify anomalies, and assess industrial activity across the city.

**Hotspot delineation** is achieved by mapping areas with consistently elevated thermal signatures relative to background conditions. **Segmentation techniques and threshold-based analysis** allow the differentiation of dominant heat sources from smaller or transient anomalies. Temporal comparison across multiple observations highlights trends in operational intensity, supporting the identification of abnormal or unusually strong thermal events. This methodology provides a systematic means to assess industrial activity, quantify the spatial extent of high-temperature operations, and identify priority areas for monitoring, despite the absence of open-source operational data.


<div style="display: flex; align-items: flex-start; justify-content: flex-start; gap: 20px;">
<div style="flex: 2;">
    <p>
        Thermal analysis of industrial areas in Nizhny Tagil reveals multiple heat anomalies associated with metallurgical and steel production processes. Elevated land surface temperature (LST) signatures are concentrated around furnace halls, smelting units, and slag handling areas where high-temperature operations occur. These installations generate persistent thermal hotspots due to continuous furnace activity and molten metal processing. Observed LST values frequently exceed surrounding background temperatures by a substantial margin, reflecting the energy-intensive nature of steelmaking operations. Heat signatures appear as spatially concentrated anomalies that correspond to industrial infrastructure footprints, including production halls, material handling zones, and residual storage areas.
    </p>
</div>
<div style="flex: 1;">
    <img src="https://public-data-213979744349.s3.eu-central-1.amazonaws.com/NizhnyTagil_Use_Case_Story/NizhnyTagil_Hotspot_Delineation.png" alt="Thermal Overview" style="max-width: 400px; height: auto;">
    <figcaption>Figure 2: Image segmentation and hotspot detection allow for automated delination and localization of heat sources associated with the idnustrial production at this site.</figcaption>
</div>
</div> 



<div style="display: flex; align-items: flex-start; justify-content: flex-start; gap: 20px;">
<div style="flex: 1;">
    <img src="https://public-data-213979744349.s3.eu-central-1.amazonaws.com/NizhnyTagil_Use_Case_Story/NizhnyTagil_Deposit_Timeseries.png" alt="Thermal Overview" style="max-width: 400px; height: auto;">
    <figcaption>Figure 3: A time series of LSTprecision imagery on different dates between January and February 2026, overlaid on a high-resolution basemap, reveals different slug deposit locations.</figcaption>
</div>
<div style="flex: 2;">
    <p>
        Analysis of successive LST acquisitions over the industrial zone of Nizhny Tagil reveals a persistent thermal anomaly associated with a sludge and residual material deposit adjacent to metallurgical processing facilities (Figure 3). Across multiple satellite observations, the anomaly consistently exceeds 70 °C, with peak LST values reaching approximately 110 °C. These elevated temperatures indicate sustained heat retention and ongoing thermal activity within the deposit.
    </p>
</div>
</div>

Spatially, the exact position of the highest-temperature pixels shifts between successive acquisitions. This variability likely reflects redistribution or deposition of hot material, localized cooling and reheating processes, or operational changes in slag and sludge handling. Despite these positional shifts, the anomaly remains confined to the same processing area, indicating continuous activity rather than isolated thermal events. The persistence and magnitude of the thermal signal strongly suggest that the hotspot is associated with metallurgical by-products, including slag, sludge, and other steel production residues that retain substantial heat after processing. Continuous deposition and handling of these materials can maintain elevated temperatures over extended periods, producing stable yet spatially dynamic thermal signatures detectable in LST imagery. 

>Note: LST retrieval depends on assumed surface emissivity. Industrial sludge deposits typically exhibit relatively high emissivity values due to their mixed mineral and moisture content, while exposed metallic surfaces may display lower emissivity and stronger reflectance. These differences can influence retrieved temperature values and should be considered when interpreting absolute LST measurements over mixed industrial materials.


> Interested in Industrial Use Cases? Check out an example datasets for Nizhny Tagil in our [Open Data Programme](https://constellr.github.io/product-lst/open-data-programme).