<h1 <span style="color: #202A78;margin-bottom: 5px;">Providing new insights into building occupancy and urban resilience in Japan using themal data</span></h1>  

## Introduction

[Japan](https://www.japantimes.co.jp/news/2024/05/01/japan/japan-vacant-homes-record-high/) is confronting a significant vacant housing crisis, with approximately 9 million empty homes nationwide, accounting for 13.6% of all residences. This issue is particularly pronounced in Sapporo, where nearly one in five dwellings is unoccupied. The rise in vacant homes adversely affects property values, increases crime rates, leads to poor sanitation, and contributes to housing market stagnation. Notably, central Sapporo exhibits severe clusters of vacancies, indicating a disequilibrium in the housing market rather than mere urban decline. 

According to news sources, demographic projections indicate that by 2035, approximately [34.6% of Sapporo's residents will be elderly](https://indianexpress.com/article/world/japan-faces-population-crisis-cities-to-witness-decline-by-2035-amid-ageing-society-9838462/). This demographic shift is expected to exacerbate the housing vacancy issue, as an aging population may lead to more unoccupied homes, further challenging urban planning and economic stability. 

To address these challenges, Sapporo has implemented [measures](https://www.city.sapporo.jp/kikaku/miraisousei/3rd/documents/planenglish.pdf) for unoccupied houses starting in fiscal year 2015 and formulated the Sapporo Unoccupied House Plan to promote appropriate management and utilization of these properties. 

The city formulated the [Sapporo Future Creation Plan](https://www.city.sapporo.jp/kikaku/miraisousei/3rd/documents/planenglish.pdf), which outlines priority measures to counteract population decline and promote economic revitalization. A key strategy involves developing a compact city structure by enhancing public transportation and promoting residential areas around subway stations, aiming to make urban living more attractive and reduce vacancies. Additionally, Sapporo emphasizes community engagement, encouraging resident-led initiatives in urban development to foster vibrant neighborhoods and address the issue of vacant properties.  

By implementing these strategies, Sapporo aims to revitalize its urban environment, effectively manage vacant housing, and ensure sustainable development in the face of demographic changes.  

However, current methods of identifying and addressing vacancy are often slow and reactive. constellr tested the ability of **thermal data** to reveal where vacancies are and why they matter. Thus, we applied our thermal monitoring capabilities to Sapporo. The results offer new insights into how **thermal footprints** can help cities tackle vacancy challenges and inform smarter urban planning. 

![Sapporo](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/sapporo-use-case/Sapporo-4.png)
<figcaption>Figure 1: A single LST image can capture the whole of Sapporo and provide thermal insights for buildings and industrial objects</figcaption>

## Land Surface Temperature (LST) in the urban context
LST measures the heat emitted from Earth’s surface - whether from a building, a street, or a park. Using constellr’s satellite-based data products, LST is able to capture these data with precision and with large coverage to monitor cities in an integrated manner.  It empowers the way we understand how cities store and release heat, which directly connects to how buildings are used - or left vacant. 

## The Sapporo Analysis: ML classification using LST data 
Inspired by the 2022 study “Vacancy Dwellings Spatial Distribution, The Determinants and Policy Implications in the City of Sapporo, Japan” by [Van et al.(2022)](https://www.mdpi.com/2071-1050/14/19/12427),constellr conducted an analysis of over 450,000 building footprints in Sapporo. By integrating LST data with population datasets from the [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/), our team sought to uncover patterns of building occupancy and vacancy through thermal signatures. 

A machine learning classification model was trained on LST data and population density information, which created a predictive model capable of classifying dwelling vacancies with an accuracy of 85 percent. In addition, including the morphological settlement zone features collected by Van et al. (2022) improved classification performance by up to 10 percent. This level of accuracy provides a powerful tool for urban planners and policymakers, enabling more informed decision-making about resource allocation, housing policy, and infrastructure management. 

## Thermal footprints as a proxy for vacancy: Key Findings 

The analysis revealed two key findings to predict housing vacancy using LST data.

*Finding 1: There are distinct thermal patterns across different seasons between occupied and vacant buildings.*  

Sapporo experiences cold winters, with December-January-February being the coldest months. Temperatures commonly fall below 0°C and cause snowfall. On the contrary, the summer months July-August-September can be hot and rainy, with temperatures exceeding 30°C. While these external drivers influence the building temperature, vacant and occupied buildings show clear differences, as visible in Figure 2a. 

In winter, vacant buildings were on average 3 to 4°C colder than their occupied counterparts, likely due to the absence of heating. In summer, these same buildings often registered higher temperatures, a consequence of the lack of air conditioning or ventilation systems. While occupied buildings range between 28 - 35°C, vacant buildings are much hotter, with temperatures between 35 and 41°C .These findings align with expectations, yet the granularity of the data enables a much more precise understanding of building-level dynamics across the urban landscape. 

![Winter-Summer](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/sapporo-use-case/Sapporo_Winter_Summer_comparison.png)
<figcaption>Figure 2a: Winter & Summer thermal footprint for buildings in Sapporo with high and low vacancy respectively. Each point represents one building.</figcaption>  

![Winter-Summer-LST](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/sapporo-use-case/Sapporo_Winter_Summer2.png)
<figcaption>Figure 2b: Winter & Summer thermal footprint for buildings in Sapporo, revealing LST hot- and coldspots. </figcaption>  

MORE RESULTS

## Implications for Urban Planning and Policy 
High-resolution thermal data offers several advantages for addressing urban vacancy and its associated challenges. First, it enables large-scale, city-wide monitoring of building occupancy without the need for costly field surveys. A single thermal imaging acquisition can cover an area of over 400 square kilometers, providing consistent, repeatable insights across entire metropolitan areas. 

From a policy perspective, the ability to accurately predict building vacancy allows municipalities to better allocate resources for maintenance, security, and redevelopment. Vacant buildings can be prioritized for reinvestment or adaptive reuse initiatives, potentially revitalizing neighborhoods and stimulating local economies. 

Thermal data also has significant implications for energy policy and climate resilience. Understanding how vacant and occupied buildings consume and emit energy across seasons supports the design of targeted energy efficiency programs. In regions where energy demand for cooling is projected to double by 2050, such insights are critical for sustainable urban development. 

![Final Output](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/sapporo-use-case/Sapporo_Classification.png)
<figcaption>Figure 4: Final output showing thermal footprints at the building level in 2020, with a trained machine learning model classifying dwelling vacancy. This ready-to-use dataset supports urban-specific case studies and decision-making.</figcaption>

## The Broader Context: Urban Heat Islands and Climate Adaptation 

The relationship between vacancy, land surface temperature, and urban heat islands is increasingly relevant in the context of climate change. As cities experience more frequent and intense heatwaves, understanding how built environments store and release heat becomes essential for public health and climate adaptation planning. 

Sapporo’s experience is not unique. Cities around the world, from New York to Mumbai are grappling with the challenges of urban vacancy and rising temperatures. High-resolution thermal data provides a scalable, actionable solution for addressing these issues, enabling better planning and more resilient urban environments.

## Conclusion 

The case of Sapporo demonstrates the potential of thermal intelligence to reshape how we approach urban vacancy and sustainability challenges. By integrating Land Surface Temperature data with population and settlement metrics, constellr offers a new tool for policymakers and urban planners to make data-driven decisions that enhance liveability, energy efficiency, and climate resilience. 

As constellr’s HiVE constellation continues to expand, offering near-continuous global thermal monitoring, the opportunities for applying thermal intelligence to urban challenges will only grow. Cities seeking to adapt to climate change, optimize resource use, and revitalize underutilized spaces will increasingly rely on data-driven insights like these. 

<br>
<h2 style="margin-top: 10px; margin-bottom: 10px; ">Download demo data</h2>
The demonstration data provides you with one geojson file of Sapporo's buildings sourced from Open Street Map (OSM). The attribute table contains information on LST for different years per building as well as the final probability of classification as vacant or non-vacant. The README.xlsx file provides information on the different fields of the attribute table.
In addition, two example LSTs are provided, one for summer and one for winter. They can be used to visualize the differences in temperatures across the city for winter and summer.

[OSM Buildings Vacancy Classification](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/sapporo-use-case/osm_residential_building_classification.geojson)
[README](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/sapporo-use-case/README.xlsx)
[Summer LST: 07.07.2019](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/sapporo-use-case/20190707T011956_LST30.tiff)
[Winter LST: 22.02.2019](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/sapporo-use-case/20190222T011333_LST30.tiff)