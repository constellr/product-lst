# **Land Surface Temperature (LST) data retrieval process**

As shown below, constellr monitors areas of interests as indicated by their customers. It then receives and processes the data from the HiVE constellation, to make the high/quality LST imagery available on a user platform for its customers. 

![Process flow](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/Explorer-lab/Work-process-flow.png){ width=60% }
<figcaption>LST data retrieval process.</figcaption>

The captured signal follows a journey of a series of steps:  

1. The data reaches constellr’s ground segment then are processed using constellr’s land surface temperature retrieval algorithm.  
2. There are various datasets used to retrieve LST including atmospheric conditions during data acquisition, the land cover type as captured by constellr’s optical sensors, as well as topographical data.  
3. The processed data is further transformed into heatmaps, where each pixel represents a specific temperature. One can visualize temperature distribution across areas by attributing colors to various temperature levels, making it easy to identify patterns like hot spots or cooler zones.  
4. Constellr then makes its data available for customers on through the End User Platform.


---

<div class="article-nav">
  <a class="prev" href="https://constellr.github.io/product-lst/EL-space-instruments-capture">← Previous Article</a>
  <a class="next" href="https://constellr.github.io/product-lst/EL-processing-thermal-data">Next Article →</a>
</div>