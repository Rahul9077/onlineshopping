import cgi
import base
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                             database='onlineshopping', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()
p_id = form.getvalue('p_id')

print("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>!INDI MART!</title>
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
print("""
<div class="container">
    <h1 class="text-center" style="color:black;">Payment Successful</h1>
    <hr>
    <div class="row">   
""")

#query = 'select * from products where p_id={}'.format(p_id)
#cursor.execute(query)
#data = cursor.fetchall()



print("""
<a href="mainPage.py" class="btn btn-primary" align = center>Continue Shopping</a>
 """)


print("""
</div>
</div>
""")

base.footer()