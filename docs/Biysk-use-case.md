<h1 <span style="color: #202A78;margin-bottom: 5px;">Activity state assessment in data sparce environments</span></h1>  

<br>

## Detecting industrial activity of the data sparce Biysk Industrial Complex in Russia

<div style="display: flex; align-items: flex-start; justify-content: flex-start; gap: 20px;">
<div style="flex: 1;">
    <img src="https://public-data-213979744349.s3.eu-central-1.amazonaws.com/Biysk_Use_Case_Story/Byisk_Location.png" alt="Thermal Overview" style="max-width: 400px; height: auto;">
    <figcaption>Figure 1: Location of Biysk</figcaption>
</div>
<div style="flex: 2;">
    <p>
    Biysk is a historically significant center for defense, chemical and heavy manufacturing. It is located in southern Siberia on the banks of the Biya River, near its confluence with the Katun River. Key facilities include the Biysk tank factory, chemical plants, machine engineering facilities, a steel plant, and sludge processing units. The sites operate high-temperature processes including furnaces, combustion systems, chemical reactors, deposit areas, and cooling water discharge. 

    However, open-source information on facility operations, production levels, or waste management practices is extremely limited, particularly for defense-related or dual-use installations. Hence, thermal satellite data can be leveraged to:  
    - Delineate spatial thermal hotspots within the industrial complex; 
    - Identify abnormal or episodic heat signatures linked to production and processing activity; 
    - Detect persistent heat sources indicative of continuously operating infrastracture. 
    </p>
</div>
</div> 

Attention is given to the **Oleum Factory of Explosives**, which is a large chemical complex producing TNT, RDX, and other high-energy explosives, currently undergoing expansion to increase explosive output capacity. Another major industrial installation is the Biysk‑1 Power Station, a coal-fired combined heat and power facility with more than 500 MW of capacity that supplies electricity and district heating to the city.  

Thermal satellite observations, particularly Land Surface Temperature (LST) data, provide a valuable tool for monitoring the operational status and environmental footprint of these facilities. Industrial plants, power stations, and chemical complexes often generate persistent thermal anomalies that are detectable in satellite time series. In winter, the discharge of heated cooling water from the coal-fired power plant into the Biya River produces distinct thermal plumes that remain visible even when the surrounding river surface freezes, providing a clear indicator of continuous plant operation. In this analysis we combine time-series thermal observations with multi-step normalization to separate operational heat signals from environmental variability. Absolute temperature measurements are first adjusted for regional conditions (e.g. weather, seasonality) and then referenced against local background surfaces, enabling the isolation of persistent excess heat associated with industrial activity. This approach supports robust detection of continuous operations and comparison across time and sites. 

<div style="display: flex; align-items: flex-start; justify-content: flex-start; gap: 20px;">
<div style="flex: 2;">
    <p> 
    The LST image highlights a cluster of major industrial assets in Biysk, each marked by distinct thermal signatures. The coal-fired power plant appears as the dominant heat source, with a clear warm-water discharge plume extending into the river. The Oleum Factory of Explosives shows a persistent thermal anomaly, consistent with continuous industrial operation over time. Additional hotspots correspond to the fiberglass plant, the machine-engineering and chemical facilities, and nearby coal storage or deposit areas linked to fuel handling. Together, these features demonstrate how LST imagery can distinguish both fixed industrial infrastructure and associated thermal impacts on the surrounding environment.
    </p>
</div>
<div style="flex: 1;">
    <img src="https://public-data-213979744349.s3.eu-central-1.amazonaws.com/Biysk_Use_Case_Story/Biysk_Hotspot.png" alt="Thermal Overview" style="max-width: 400px; height: auto;">
    <figcaption>Figure 2: Sharpened LST, 15.02.2026, daytime, indicating hotspots from several industrial assets.</figcaption>
</div>
</div> 

<div style="display: flex; align-items: flex-start; justify-content: flex-start; gap: 20px;">
<div style="flex: 1;">
    <img src="https://public-data-213979744349.s3.eu-central-1.amazonaws.com/Biysk_Use_Case_Story/Biysk_Chart.png" alt="Thermal Overview" style="max-width: 400px; height: auto;">
    <figcaption>Figure 3: Shaprened LST time series over the Biysk Oleum Factory.</figcaption>
</div>
<div style="flex: 2;">
    <p> 
    The chart (Figure 3) presents a Land Surface Temperature (LST) time series for the Biysk Oleum Factory, showing a consistently elevated thermal signal through time. The raw LST series captures the absolute surface temperature of the facility, but it is strongly influenced by seasonal and meteorological variability. To isolate the industrial heat contribution, the series is normalized first against ambient air temperature, reducing the effect of regional weather fluctuations. A second normalization uses cold reference pixels, such as open fields, vegetation, and other non-urban surfaces, to provide a local background baseline.  
    </p>
</div>
</div> 

This approach highlights the factory’s excess thermal signal relative to its surroundings, making persistent operational activity easier to detect. Compared with the raw LST record, the normalized series provides a clearer view of long-term stability and anomalous heat output from the site. The persistence of this thermal excess suggests that the Oleum Factory remains regularly active rather than intermittently idle. Overall, the chart demonstrates how combining raw and normalized LST metrics improves confidence in identifying continuous industrial operation from satellite observations. 

<div style="display: flex; align-items: flex-start; justify-content: flex-start; gap: 20px;">
<div style="flex: 2;">
    <p> 
    The image series (Figure 4) presents eight satellite-derived sharpened LST scenes showing the thermal discharge from the coal-fired power plant into the Biya River in Biysk. Each frame captures a distinct warm plume extending from the plant’s cooling water outlet into the colder river system. The thermal contrast becomes particularly pronounced during winter, when surrounding air and water temperatures drop significantly. Under these colder conditions, the heated effluent from the plant creates a clearly visible thermal anomaly that stands out in the LST imagery.  This persistent open-water pattern provides a strong visual indicator of continuous thermal discharge from the facility. The plume’s spatial extent and intensity also vary depending on ambient temperatures and river flow conditions. 
    </p>
</div>
<div style="flex: 1;">
    <img src="https://public-data-213979744349.s3.eu-central-1.amazonaws.com/Biysk_Use_Case_Story/Biysk_LST_Timeseries.png" alt="Thermal Overview" style="max-width: 400px; height: auto;">
    <figcaption>Figure 4: Sharpened LST time series, over the Biysk Oleum Factory and coal plant. Time is given UTC; local time is equivalent to UTC+7.</figcaption>
</div>
</div> 

Such observations are useful for monitoring the operational status of the coal power plant, as the presence of warm discharge implies active cooling cycles. The power plant plays a key role in supplying electricity and heat to Biysk’s industrial complex. In particular, the nearby Oleum explosives factory requires substantial and reliable energy input for chemical production processes. Therefore, the recurring thermal plume in the river indirectly reflects the functioning of both the power station and the broader industrial infrastructure it supports. 

> Interested in Industrial Use Cases? Check out an example datasets for Biysk in our [Open Data Programme](https://constellr.github.io/product-lst/open-data-programme).

