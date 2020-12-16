import base
#import json
import pymysql
mobile = 'mobile'
#DATABASE CONNECTION
connection = pymysql.connect(host='localhost',user='root',database='onlineshopping',
                             port = 3306, autocommit = True)
cursor = connection.cursor()




print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>!INDI MART!</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <style>
        body {
            background-image : url("http://cdn.osxdaily.com/wp-content/uploads/2011/10/NSTexturedFullScreenBackgroundColor.png");
        } 
            color : #fff;
        }
    </style>
</head>
<body>
""")
base.header()
base.slide()

# CONNECTION QUERY

query = "select * from product"
cursor.execute(query)
data = cursor.fetchall()
rowcount = cursor.rowcount

#CAROUSEL
print("""
<div class="container">
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="http://thirdeyecomputers.com.np/FileUploads/back/Carausal/slider11.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="https://1.bp.blogspot.com/-onKYvQ-NfYA/WXXLv3hM7cI/AAAAAAAAAgY/CDpEJUA1QoUDqjfn4aNLc9k1O_0GR77uQCLcBGAs/s1600/Banner-Smart-2-1920x600.jpg" class="d-block w-100" alt="...">
    </div>
    
    <div class="carousel-item">
      <img src="https://static.roland.com/assets/promos/jpg/cat-marquee_rh-300.jpg" class="d-block w-100" alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>

""")

#CONTAINER FOR PRODUCTS
print("""
<div class="container">
    <h1 class="text-center"></h1>
    <hr>
    <div class="row">
""")

#PRODUCT CARD
for i in range(rowcount):
    print("""
    <div class="col-md-3">
    <div class="card text-white bg-dark mb-3" style="width: 18rem;margin-bottom:20px; ">
      <img src="{}" class="card-img-top" alt="img" height=400>
      <div class="card-body">        
        <h5 class="card-title">{}</h5>
        <p class="card-text">Price : {}</p>
        <a href="cart.py?p_id={}" class="btn btn-primary">Add to Cart</a>
        <a href="productDetails.py?p_id={}" class="btn btn-primary">View Details</a>
      </div>
    </div>
    </div>
    """.format(data[i][-1], data[i][2], data[i][4], data[i][0],data[i][0]))

print("""
</div>
</div>
""")

base.footer()