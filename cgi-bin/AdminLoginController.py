import cgi
import model


form = cgi.FieldStorage()
password = form.getvalue("password")

data = model.loginAdmin(password)
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

if data == 'success':
    import adminPannel

else:
    print("""
    <h3 style="color: aqua;">incorrect password ! try again</h3>
    """)
    import AdminLogin

print("""
</body>
</html>
""")
