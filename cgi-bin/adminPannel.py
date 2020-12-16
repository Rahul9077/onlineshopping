import cgi
import model
import base

data = model.orders()

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
     <a class="nav-link " href="index.py" tabindex="-1" aria-disabled="true">LOG OUT</a> <h1 class="text-center">ADMIN PANNEL</h1>
    
    <hr>
    <div class="row">
""")
print("""
<table border = "0 solid black" style="width:100%; color: aqua;">
  <tr>
    <th style ="font-size: xx-large;">Name</th>
    <th style ="font-size: xx-large;">Address</th>
    <th style ="font-size: xx-large;">Pincode</th>
    <th style ="font-size: xx-large;">Landmark</th>
    <th style ="font-size: xx-large;">Product</th>
  </tr>
""")
for i in range(len(data)):
    print(f"""
    <tr>
    <td style ="font-size: x-large;">{data[i][0]}</td>
    <td style ="font-size: x-large;">{data[i][1]}</td>
    <td style ="font-size: x-large;">{data[i][2]}</td>
    <td style ="font-size: x-large;">{data[i][3]}</td>
    <td style ="font-size: x-large;">{data[i][4]}</td>
    </tr>
    
    """)
print("""
</table>
""")
base.footer()
print("""
</body>
</html>
""")