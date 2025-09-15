
# **End User Platform - UI Documentation**


This page will guide you through the steps to create an account, access it, and browse through the assets list page.
<!-- > **Note:** If your organisation is registered with constellr, you can create an account for free. -->

## **Login**
You can access the End User Platform via the [sign in](https://app.constellr.com/signin) page, using your email and password.  

<h3>First time user?</h3>

You will need to create an account via the [sign up](https://app.constellr.com/signin) page.

> **Note**
> To create an account your organization must be registered with constellr and you must use your company email.  
> In case you need support, please contact: [support-csm@constellr.com](mailto:support-csm@constellr.com)



**Step 1 - Create an account**

You’ll be prompted with a form where you need to provide your e-mail address and password. To create an account, you’ll need to read and accept the terms and conditions. 

**Step 2 - Verify your account**

To finish creating your account, you will need to enter a verification code which you will receive via e-mail during the sign up process. In the application, you will be prompted to enter the verification code. This code is only valid for 24 hours.  

Once the code is entered, the account will be activated, and you can proceed to sign in and access your account.  

## **Navigating the End User Platform**
   
There are three sections to the platform, which you can access from the sidebar on the left:  

- **My Data**: Access your data and track your orders.  
- **New order**: Place a new order. 
- **AOI Library**: Create and manage your Areas of Interest. 

<h3>My Data</h3>
This is the central place for tracking your data orders and downloading your data.  

**Tracking Orders**  
A table shows an overview of all orders you have placed, including their status, area of interest, product, and monitoring period. At the top of the page, you can search and filter your orders to quickly find the data you need.  

![MyDataList](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/UI_documentation/MyDataList.png){ width=80% }

Each row in the table represents one data order with the following information:  

- **Data Order ID**: The unique identifier for the order.  
- **State**: You can use this to track where the order is in it’s lifecycle: 
    - *Pending Validation* – waiting for validation by constellr CSMs. 
    - *In Progress* – the order is active and the system is working to acquire and deliver images to you.  
    - *Closing* – this status is triggered when the monitoring period is over. The system is no longer trying to acquire new images. However, we are waiting for any last images taken by the satellite to be downlinked, processed and quality controlled before the order closes.  
    - *Closed* – the order is complete and all of your data has been delivered.   
- **Area of Interest**: The AOI being imaged for this order. 
- **Frequency**: How often data is delivered to you (e.g. *Single Image, Weekly, Monthly*). This is a *target* frequency rather than a guaranteed frequency. The real frequency of deliveries may vary based on when acquisitions can take place, cloud coverage, satellite availability etc.  
- **Product**: The selected product type for the order (*LSTPrecision, LSTZoom, LSTFusion*). 
- **Monitoring Period**: The time window for which data is collected.  

**Downloading Data**  
You can access your data by clicking on the Data Order ID. Here, you can see every delivery for that order.  

Each delivery is named according to when the image was acquired by the satellite. You can expand each delivery to see the files inside of it, and download each delivery by using the download icon at the bottom.  

![MyDataExample](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/UI_documentation/MyDataExample.png){ width=80% }

<h3>New Order</h3>
To place a new order, you can navigate to the [New Order](https://app.constellr.com/new-order) tab. Here, you can simply fill in the order details as prompted. You can submit multiple orders at a time by clicking the  ‘Add Order’ button before submission. You can also duplicate or remove an order by clicking on the three dots on the top right of each order box.   

Upon successful submission, you will receive a confirmation message. Your order will also be visible in the table on the My Data tab.  

![NewOrder](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/UI_documentation/NewOrder.png){ width=80% }

<h3>AOI Library</h3>
This page is under construction and provides limited functionality for the moment.  

From the [AOI Library](https://app.constellr.com/aoi-library) tab, you can manage the AOIs that you have defined. You can see the name, creation date and size. You can also download the GeoJSON by clicking the three dots on the upper right of each AOI.  

From this page, you can create new AOIs that can be reused when creating orders. You can either draw an AOI or upload polygon coordinates. Each AOI in your account must have a unique name.  

![AOILibrary](https://public-data-213979744349.s3.eu-central-1.amazonaws.com/UI_documentation/AOILibrary.png){ width=80% }
