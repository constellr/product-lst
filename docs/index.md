# constellr Knowledge Center
 


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Centered Horizontally</title>
<style>
        body {
            background-color: #f0f0f0; /* Optional background */
            margin: 0;
            padding: 0;
        }
        .wrapper {
            text-align: center; /* Center children horizontally */
            margin-top: 100px; /* Adjust vertical spacing as needed */
        }
        .image-container {
            position: relative;
            display: inline-block; /* Keeps it as a block within text-align */
            width: 600px; /* Adjust width */
            height: 400px; /* Adjust height */
        }
        .image-container img {
            position: absolute;
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0;
            transition: opacity 1s ease-in-out;
        }
        .image-container img.active {
            opacity: 1;
        }
</style>
</head>
<body>
<div class="wrapper">
<div class="image-container">
<img src="images/index/BareSoil.png" alt="First Image" class="active">
<img src="images/index/LST.png" alt="Second Image">
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






## Company Description


constellr is developing an unparalleled thermal intelligence atlas of our planet. The atlas is a constantly updated view of the surface temperature across the globe, providing real-time high-precision insights into the water & carbon cycles it shapes.  

The atlas leverages constellr's proprietary advanced satellite technology and data fusion combined with biophysical modelling and AI-powered analytics to transform how we understand and manage the Earth’s resources.  

Find more about [constellr](https://www.constellr.com/) 


## About the Knowledge Center
This space is a centralized source of technical information regarding constellr's datasets and products. It empowers customers and partners to engage with constellr's thermal products more effectively.  

Through this knowledge center, find information about metadata and formats as well as obtain demo datasets for use cases that interest you. It is a dynamic space and is continuously updated with the most relevant information.  

## Discover the Knowledge Center


 
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
    }

    /* Material Icons font-size */
    .material-icons {
      font-size: 24px;
      vertical-align: middle;
    }
   

   
  </style>
</head>
<body>

<div class="container py-4">
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title"><span class="material-icons">map</span> <strong>Constellation Journey and Specs</strong></h5>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title"><span class="material-icons">satellite</span> <a href="https://constellr.github.io/product-lst/Constellr-product-offer/" style="color: black;">Product Portfolio</a></h5>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title"><span class="material-icons">science</span> <a href="https://constellr.github.io/product-lst/use-cases/" style="color: black;">Use Cases</a></h5>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title"><span class="material-icons">book_education</span> <a href="https://constellr.github.io/product-lst/demo/" style="color: black;">Explorer Lab</a></h5>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title"><span class="material-icons">settings</span> <a href="https://constellr.github.io/product-lst/UI-documentation/" style="color: black;">Data Delivery and API</a></h5>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title"><span class="material-icons">help_outline</span> <strong>FAQ</strong></h5>
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



<div class="connect">
    <h3>Connect with Us</h3>

    <!-- Email Contact -->
    <p>
        <a href="mailto:support-csm@constellr.com">
            <span class="material-icons">email</span> Email Us
        </a>
    </p>

    <!-- LinkedIn -->
    <p>
        <a href="https://www.linkedin.com/company/constellr/posts/?feedView=all">
            <span class="material-icons">link</span> LinkedIn
        </a>
    </p>

    <!-- Website -->
    <p>
        <a href="https://www.constellr.com/" target="_blank">
            <span class="material-icons">language</span> constellr Website
        </a>
    </p>
</div>
