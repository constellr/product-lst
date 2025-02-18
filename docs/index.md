<h1 style="margin-bottom: 5px; color: #123774;"><strong>The Knowledge Center</strong></h1>
<h2 style="margin-top: 0; margin-bottom: 5px; color: #24398F;"><em>Everything you need to know about constellr's LST data</em></h2>

<br>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Centered Horizontally</title>

<!-- Font Awesome for Icons like LinkedIn -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">

<!-- Custom Stylesheet -->
<link href="stylesheets/extra.css" rel="stylesheet">
</head>


<body>
<div class="wrapper" style= 'margin-top: 0; margin-bottom: 0;'>
<div class="image-container">
<img src="images/index/freiburg_2023-06-25_tobi_aoi_basemap.png" alt="First Image" class="active">
<img src="images/index/freiburg_2023-06-25_tobi_aoi_lst_overlay.png" alt="Second Image">
</div>
</div>
 
    <script>
        const images = document.querySelectorAll('.image-container img');
        let currentIndex = 0;
 
        setInterval(() => {
            images[currentIndex].classList.remove('active');
            currentIndex = (currentIndex + 1) % images.length;
            images[currentIndex].classList.add('active');
        }, 3000); // Switch every 3 seconds
</script>
</body>
</html>



<h2 style= "color: #123774;">Company Description</h2>

constellr is developing an unparalleled <strong>thermal intelligence atlas of our planet</strong>. The atlas is a constantly updated view of the surface temperature across the globe, providing real-time high-precision insights into the water & carbon cycles it shapes.  

The atlas leverages constellr's proprietary advanced satellite technology and data fusion combined with biophysical modelling and AI-powered analytics to transform how we understand and manage the Earth’s resources.  

Find out more on [constellr](https://www.constellr.com/).

<h2 style= "color: #123774;">About the Knowledge Center</h2>

This space is a centralized source of technical information regarding constellr's datasets and products. It empowers customers and partners to engage with constellr's thermal products more effectively.  

Through this knowledge center, find information about metadata and formats as well as obtain demo datasets for use cases that interest you. It is a dynamic space and is continuously updated with the most relevant information.  

<h2 style= "color: #123774;">Discover the Knowledge Center</h2>
 
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cards Grid</title>

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">

  <!-- Material Icons CDN -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

  <style>
    /* Additional Custom Styles */
    .card {
      height: 100%; /* Ensure all cards have the same height */
      display: flex;
      flex-direction: column;
      background-color: #160A42; /* Blue background */
      color: #EE9219EA; /* Red text */
      border: none; /* Optional: removes default border */
      transition: background-color 0.3s ease-in-out; /* Smooth transition */
    }

    /* Change background color on hover */
    .card:hover {
      background-color: #21125a; /* Slightly lighter blue */
    }

    .card-body {
      display: flex;
      flex-direction: column;
      align-items: center; /* Center horizontally */
      justify-content: center; /* Center vertically */
      text-align: center; /* Ensures inline text elements are centered */
      height: 100%; /* Ensures full height for vertical centering */
    }

    .card-title {
      color: #EE9219EA !important;
      display: flex;
      align-items: center;
      justify-content: center; /* Center horizontally */
      gap: 8px; /* Space between icon and text */
      margin: 0;
      text-align: center; /* Ensure text alignment */
    }


    /* Ensure links inside the card title are also red */
    .card-title a {
      color: #EE9219EA !important;
    }
    /* Material Icons font-size */
    .material-icons {
      font-size: 32px;
      vertical-align: middle;
      color: #EE9219EA; /* Red */
      line-height: 1; /* Fix vertical centering issues */
    }
   

   
</style>
</head>
<body>
<div class="container py-4">
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">
            <span class="material-icons" >map</span> <a href="https://constellr.github.io/product-lst/our-technology/" style="color: black;">Our Technology</a>
          </h5>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">
            <span class="material-icons" >science</span> <a href="https://constellr.github.io/product-lst/thermal-insights/" style="color: black;">Use Cases</a>
          </h5>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">
            <span class="material-icons">satellite_alt</span> <a href="https://constellr.github.io/product-lst/Constellr-product-offer/" style="color: black;">Product Portfolio</a>
          </h5>
        </div>
      </div>
    </div>


    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">
            <span class="material-icons" >search</span> 
            <a href="https://constellr.github.io/product-lst/demo/" style="color: black;" >Explorer Lab</a>
          </h5>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">
            <span class="material-icons">settings</span> <a href="https://constellr.github.io/product-lst/UI-documentation/" style="color: black;">End User Platform documentation</a></h5>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">
            <span class="material-icons" >help_outline</span> <strong>FAQ</strong></h5>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Bootstrap JS & Popper.js -->
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>

</body>
</html>


