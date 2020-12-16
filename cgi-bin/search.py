import cgi
import base
import json
import pymysql
connection = pymysql.connect(host='localhost',user='root',database='onlineshopping',
                             port = 3306, autocommit = True)
cursor = connection.cursor()

form = cgi.FieldStorage()
search = form.getvalue('q')

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
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
query = "select * from products"
cursor.execute(query)
data = cursor.fetchall()
rowcount = cursor.rowcount

print("""
<div class="container">
    <h1 class="text-center">Products</h1>
    <hr>
    <div class="row">
""")
for i in range(rowcount):
    search = search.lower()
    if search in data[i][1].lower() or search == data[i][5].lower() or search == data[i][4].lower():
        print("""
        <div class="col-md-4">
        <div class="card text-white bg-dark mb-3" style="width: 18rem;margin-bottom:20px; padding:10px;">
          <img src="{}" class="card-img-top" alt="img" height=400>
          <div class="card-body">
            <h5 class="card-title">{}</h5>
            <p class="card-text">Price : {}</p>
            <a href="cart.py?p_id={}" class="btn btn-primary">Add to Cart</a>
            <a href="productDetails.py?p_id={}" class="btn btn-primary">View Details</a>
          </div>
        </div>
        </div>
        """.format(data[i][3], data[i][1], data[i][2],data[i][0],data[i][0]))

print("""
</div>
</div>
""")

base.footer()