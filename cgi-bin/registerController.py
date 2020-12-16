import cgi
import model
import base

form = cgi.FieldStorage()

name = form.getvalue('name')
mobile = form.getvalue('mobile')
email = form.getvalue('email')
password = form.getvalue('password')



user = model.register(name,mobile, email, password)

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

base.footer()
print("""
</body>
</html>
""")