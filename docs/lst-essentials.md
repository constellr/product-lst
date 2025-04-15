<h1 style="margin-bottom: 5px; "><strong>LST - The Essentials</strong></h1>

## LST and its importance

The temperature of the Earth's land surface represents how hot the ground would feel if you touched it in a specific location. Such temperature is quantified using thermal and optical sensors such as those of constellr. From a satellite’s perspective, the "surface" could be anything visible from space—snow, grass, rooftops, or forest canopies (See Figure 1). So, LST differs from air temperature measured by local stations, by soil sensors, or reported weather data and forecasts. 

Scientists monitor Land surface temperature because it affects and is affected by weather and climate patterns. They track how rising greenhouse gases influence LST and how changes in LST impact glaciers, ice sheets, permafrost, and vegetation. Farmers often rely on spectral vegetation indices to assess irrigation needs and monitor crop water stress. However, they can also use LST maps to evaluate crop water requirements during summer heat and to identify areas at risk of frost damage in winter. City planners utilize LST data to assess urban heat islands and leverage insights for infrastructure planning.

![LST monthly composite](link)
<figcaption>Figure 1: Daytime LST monthly composite map, constellr (leveraging a fusion of public data) </figcaption>

The 2030 Agenda for Sustainable Development, adopted by all United Nations Member States in 2015, offers a shared blueprint for peace and prosperity for people and the planet, now and into the future. At its core are the 17 Sustainable Development Goals (SDGs), which are an urgent call to action for all countries, both developed and developing, to engage in a global partnership. Temperature monitoring is crucial for 12 of them.   

![SDGs](Link)
<figcaption>Figure 2: 12 of 17 SDG Goals United Nations, 2024 shown around an image depicting LST Surface temperature of agricultural fields in Saudi Arabia where blue highlights the round fields with lower temperature. </figcaption>

Through consistently delivering data over time, it is possible to make more intelligent decisions for the environment and businesses. Surface Temperature data empowers actionable intelligence for the sustainable management of agricultural and infrastructure assets, for example monitoring agricultural fields at scale or gathering precise data on Urban Heat Islands.  

## constellr's acquisition process
<h3>What spaceborne instruments capture</h3>
Constellr’s core technology is based on its spaceborne acquisitions by the High-precision Versatile Ecosphere (HiVE) monitoring constellation of micro satellites, the SkyBees. A SkyBee has onboard sensors that acquire high quality thermal and optical imagery. Thus, each SkyBee is equipped with [cutting-edge sensors](https://constellr.github.io/product-lst/our-technology/) capable of capturing detailed thermal data and data from the visible and near-infrared (VNIR) part of the spectrum.

IMAGE TO BE CREATED/ADDED
<figcaption>Figure 3: </figcaption>

To understand this fully, lets dig a bit deeper into the electromagnetic spectrum, which essentially represents all the different forms “light” can appear in (see Figure 3). Light from a physical understanding is a wave, and depending on the wavelength, it carries more or less energy. Short wavelengths are ultraviolet (UV) waves carry a lot of energy; therefore, they can damage our cells at excessive exposure. They are followed by the “visible light”, i.e. wavelengths that we perceive in different colors. This is followed by the longer infrared wavelengths. The infrared spectrum is very wide and can be divided into the Near Infrared (NIR), Mid Infrared, and Far Infrared. The NIR is an important component of vegetation analysis, as healthy plants reflect a lot of NIR. In comparison, Mid and Far Infrared radiation can give us a sensation of warmth when they reach our skin and are therefore also termed thermal radiation. Furthermore, every object or material with a temperature above absolute zero (0 Kelvin or -273.15°C) will emit some thermal radiation in the form of infrared waves. This can be captured day and night with the appropriate sensors. 

Thus, a SkyBee satellite of the HiVE constellation carries one sensor that detects Far Infrared thermal radiation emitted from the Earth’s surface and another detects visible and NIR (VNIR) reflected radiation from the same surface, simultaneously. With the captured information, constellr provides Land Surface Temperature (LST), a crucial parameter for climate studies, agriculture, urban planning, and environmental monitoring. 

For more information on our sensors and technology see [Our Technology page](https://constellr.github.io/product-lst/our-technology/)

<h3>The characteristics of constellr's spaceborne instruments</h3>
A SkyBee satellite of the HiVe constellation carries one sensor that detects Far Infrared thermal radiation emitted from the Earth’s surface and another that detects visible and NIR reflected radiation from the same surface, simultaneously (see Figure 4).

![Sensor specifics](Link)
<figcaption>Figure 4: </figcaption>
 
When you snap a photo with a standard phone camera, you can instantly view a clear image. However, this is not the case with a scientifically graded thermal imager, such as HiVE’s. For example, take a look at the raw imagery near Toulouse airport from our HiVE thermal imager(simulated). The airport and the nearby river features are hardly distinguishable until post-processing is applied (see Figure 5).

![Un-processed Images](Link)
<figcaption>Figure 5: Example of raw HIVE thermal image on the left (simulated) vs processed image on the right </figcaption>

The VNIR sensor on constellr’s satellites is similar to the [Sentinel-2 mission](https://sentiwiki.copernicus.eu/web/s2-mission), capturing data in the visible and near-infrared spectrum. VNIR data provides crucial contextual information, helping to interpret thermal data accurately by identifying specific features on the ground, such as rivers, vegetation, and urban areas. This is essential for ensuring that temperature measurements are precisely linked to specific locations on Earth.  

On the other hand, Thermal Infrared (TIR) sensors capture the heat emitted by objects on the Earth's surface. This data is critical for detecting temperature variations and identifying hotspots. Constellr captures long-wave thermal data emitted by objects on the Earth’s surface. However, raw thermal images can be challenging to interpret without the contextual information provided by VNIR data.  VNIR data plays a pivotal role in enhancing the usability of thermal images. Without VNIR support, interpreting thermal data can be challenging, as features that appear similar in temperature might look very different in VNIR imagery. This contrast helps analysts pinpoint the exact location and nature of heat anomalies, providing a more accurate understanding of urban heat patterns.  

For example, comparing a standard RGB image with a VNIR-enhanced image near Toulouse airport shows how VNIR data can highlight differences in vegetation, water bodies, and built-up areas. This differentiation is crucial for accurate thermal analysis, ensuring that hotspots are correctly located and identified (see Figure 6). 

![RGB vs NIR Images](Link)
<figcaption>Figure 6: Toulouse airport runwazs and their surroundings viewed as a real color image vs false color image with near-infrared</figcaption>

<h3>LST retrieval process</h3>
Constellr’s thermal instruments detect infrared, they turn it into an electrical signal, which shows how hot the surface is. This signal's strength is proportional to the heat emitted by the surface observed by the satellite (see Figure 7).  

![LST retrieval process](Link)
<figcaption>Figure 7: LST retrieval process</figcaption>

The captured signal follows a journey of a series of steps:  

1. The data reaches constellr’s ground segment then are processed using constellr’s land surface temperature retrieval algorithm.  
2. There are various datasets used to retrieve LST including atmospheric conditions during data acquisition, the land cover type as captured by constellr’s optical sensors, as well as topographical data.  
3. The processed data is further transformed into heatmaps, where each pixel represents a specific temperature. One can visualize temperature distribution across areas by attributing colors to various temperature levels, making it easy to identify patterns like hot spots or cooler zones.  
4. Constellr then makes its data available for customers on through the [End User Platform](Link to end user platform)