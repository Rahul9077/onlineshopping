import base
import cgi

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
     <form action="registerController.py" method="post" enctype='multipart/form-data'>
     <div class="form-group">
        <label for="name">Enter Name</label>
         <input type="text" name="name" class="form-control">
      </div>
      <div class="form-group">
        <label for="mobile">Enter mobile no</label>
        <input type="text" class="form-control" id="mobile" name="mobile" placeholder="Enter Mobile No">
        <small id="emailHelp" class="form-text text-muted">We'll never share your mobile number with anyone else.</small>
      </div>
      <div class="form-group">
      <label for="email">Enter Email</label>
         <input type="text" name="email" class="form-control">
      </div>
     <div class="form-group">
         <label for="exampleInputPassword1">Password</label>
         <input type="password" class="form-control" name="password" id="password" placeholder="Password">
     </div>
     
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
""")


base.footer()
print("""
</body>
</html>
""")