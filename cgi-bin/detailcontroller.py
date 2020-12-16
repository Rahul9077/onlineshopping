import cgi
import base
import model

form = cgi.FieldStorage()
name = form.getvalue('name')
address=form.getvalue('address')
pin = form.getvalue('pin')
landmark = form.getvalue('landmark')
product = form.getvalue('product')
model.details(name,address,pin,landmark,product)

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
    <h1 class="text-center" style="color:black;">Payment Successful</h1>
    <hr>
    <div class="row">   
""")
print("""
<a href="mainPage.py" class="btn btn-primary" align = center>Continue Shopping</a>
 """)


print("""
</body>
</html>
""")
