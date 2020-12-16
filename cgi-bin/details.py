import base
import cgi
import model

data = model.getCartData()
product = data[0][2]
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

print("""
<div class="container">
    <h1 class="text-center"></h1>
    <hr>
    <div class="row">
""")

print("""
<div class="card mb-3" style="
    margin: auto;">
  <img src="/image/image.png" class="card-img-top" alt="...">
  <div class="card-body">
     <form action="detailcontroller.py" method="post" enctype='multipart/form-data'>
     <input type="hidden" value={} name="product">
     <div class="form-group">
        <label for="name">Enter Name</label>
         <input type="text" name="name" class="form-control">
      </div>
      
      <div class="form-group">
        <label for="mobile">Enter address</label>
        <input type="text" class="form-control" id="address" name="address" placeholder="address">
      </div>
      <div class="form-group">
      <label for="email">Enter pincode</label>
         <input type="text" name="pin" class="form-control">
      </div>
     <div class="form-group">
         <label for="exampleInputPassword1">Enter landmark</label>
         <input type="text" class="form-control" name="landmark" id="password" placeholder="landmark">
     </div>

      <button type="submit" class="btn btn-primary">Make Payment</button>
    </form>


""".format(product))


base.footer()

print("""
</body>
</html>
""")


