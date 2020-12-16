import base
import cgi
import model
import pymysql

form = cgi.FieldStorage()
print(form)
item = form.getvalue('p_id')


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
        h1 {
            color : #fff;
        }
    </style>
</head>
<body>
""")


base.header()
try:
    data = model.mycart(item)
    model.writeMyCart(data)
except BaseException as ex:
    pass

data2 = model.getCartData()

print("""
<div class="container">
    <h1 class="text-center">My CART</h1>
    <hr>
    <div class="row">
""")


totalcart=0
for j in range(len(data2)):
    totalcart = totalcart + int(data2[j][4])
    print("""
    <div class="col-md-4">
    <div class="card text-white bg-dark mb-3" style="width: 18rem;margin-bottom:20px; padding:10px;">
        <img src="{}" class="card-img-top" alt="img" height=400>
        <div class="card-body">
        <h5 class="card-title">{}</h5>
        <p class="card-text">Price : {}</p>
        <a href="deleteCartController.py?p_id={}" class="btn btn-primary">Delete</a>
        <a href="productDetails.py?p_id={}" class="btn btn-primary">View Details</a>
        </div>
    </div>
    </div>""".format(data2[j][-1], data2[j][2], data2[j][4], data2[j][0],data2[j][0]))

#print("<h3>total cart = {}</h3>".format(totalcart))
#print("<h3>no of products = {}</h3>".format(len(data2)))
print("""
<div class="card text-black bg-primary mb-3" style="width: 18rem;margin-bottom:20px; padding:10px;">
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Number of Products=</li>
    <li class="list-group-item">Cart Price={}</li>
    
    <form action="CouponController.py?q={}" method="post">
  <div class="form-group">
    <label for="coupon">Coupons:</label>
    <input type="text" class="form-control" id="coupon" name="coupon" placeholder="apply coupon">
  </div>
 <button type="submit" class="btn btn-primary">Apply</button>
  
</form>
 

    <li class="list-group-item">Discount=</li>
    <li class="list-group-item">Total Price={}</li>
  </ul>
  <div>
<a href = "details.py" class = "btn btn-primary">Buy Now</a>
</div>
</div>
""".format(totalcart,totalcart,totalcart))

base.footer()
print("""
</body>
</html>
""")