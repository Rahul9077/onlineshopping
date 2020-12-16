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
  <a class="nav-link " href="AdminLogin.py" tabindex="-1" aria-disabled="true">ADMIN</a>
""")
print("""
<div class="container">
    <h1 class="text-center"></h1>
    <hr>
    <div class="row">
""")

print("""
<div class="card" style="width: 18rem;margin: auto;">
  <img src="/image/image.png" class="card-img-top" alt="...">
  <div class="card-body">
    <a href="registerPage.py" class="btn btn-primary">REGISTER</a>
    <a href="loginPage.py" class="btn btn-primary">LOGIN</a>
    <hr>
    <a class="nav-link " href="mainPage.py" tabindex="-1" aria-disabled="true">Skip Login</a>
  </div>
</div>
""")

base.footer()
print("""
</body>
</html>
""")