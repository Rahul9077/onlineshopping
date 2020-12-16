print("""
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
         <style>
        body {
            background-image : url("http://cdn.osxdaily.com/wp-content/uploads/2011/10/NSTexturedFullScreenBackgroundColor.png");
        }
        h1 {
            color : #fff;
        }
    </style>
        <title>Hello, world!</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
    """)
print("""
<div class="container">
    <h1 class="text-center">LOGIN</h1>
    <div class="row">
""")
print("""
<div class="card mb-3" style="
    margin: auto;">
  <img src="/image/image.png" class="card-img-top" alt="...">
  <div class="card-body">
      <form action="AdminLoginController.py" method="post" enctype='multipart/form-data'>
 
  <div class="form-group">
    <label for="password">Password</label>
    <input type="password" class="form-control" id="password" name="password" placeholder="Password">
  </div>

  <button type="submit" class="btn btn-primary">Submit</button>
</form>
  </div>
</div>
""")

print("""
</body>
</html>""")