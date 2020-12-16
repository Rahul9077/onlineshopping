import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                             database='onlineshopping', autocommit=True)

cursor = connection.cursor()

class User():
    def __init__(self,name,mobile, email, password):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.password = password


    def __str__(self):
        return self.name + "," + self.mobile + "," + self.email + "," + self.password

def mycart(p_id):
    query="select * from product where p_id=%s"
    cursor.execute(query,(p_id))
    data = cursor.fetchall()
    return data

def writeMyCart(data):
    query2="insert into cart values (%s, %s, %s, %s, %s,%s)"
    cursor.execute(query2, (data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5]))

def getCartData():
    query = "select * from cart"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def deleteProduct(p_id):
    query = "delete from cart where p_id=%s "
    cursor.execute(query,p_id)


def register(name,mobile,email,password):
    try:
        user = User(name,mobile,email,password)
        # users.append(user)
        query = "insert into user values (%s, %s, %s, %s)"
        cursor.execute(query, (user.name, user.mobile, user.email, user.password))
        return user
    except pymysql.IntegrityError:
        return "Email ID Already Exist"

def loginUser(email,password):
    query = "select * from user where email=%s and password = %s"
    cursor.execute(query, (email, password))
    # data_length = cursor.rowcount
    data = cursor.fetchall()
    if len(data) < 1:
        return "User do not exist"
    else:
        return data
def spool_10():
    pass

def coupons(coupon,totalcart):
    c='spool'
    if coupon == c:
        discount=(totalcart*10)/100
        totalcart=totalcart-(totalcart*10)/100
        return totalcart,discount
    else:
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

        totalcart = 0
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
            </div>""".format(data2[j][-1], data2[j][2], data2[j][4], data2[j][0], data2[j][0]))

        # print("<h3>total cart = {}</h3>".format(totalcart))
        # print("<h3>no of products = {}</h3>".format(len(data2)))
        print("""
        <div class="card text-black bg-primary mb-3" style="width: 18rem;margin-bottom:20px; padding:10px;">
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Number of Products=</li>
            <li class="list-group-item">Cart Price={}</li>
            <li class="list-group-item">Invalid Coupon Code</li>

            <form action="CouponController.py?q={}" method="post">
          <div class="form-group">
            <label for="coupon">Coupons:</label>
            <input type="text" class="form-control" id="coupon" name="coupon" placeholder="apply coupon">
          </div>
         <button type="submit" class="btn btn-primary">Apply</button>

        </form>


            <li class="list-group-item">Discount=</li>
            <li class="list-group-item">Total Price=</li>
          </ul>
          <div>
        <a href = "details.py" class = "btn btn-primary">Buy Now</a>
        </div>
        </div>
        """.format(totalcart, totalcart))

        base.footer()
        print("""
        </body>
        </html>
        """)
def details(name,address,pin,landmark,product):
    query = "insert into adminp values (%s, %s, %s, %s ,%s)"
    cursor.execute(query, (name, address, pin, landmark, product))

def orders():
    query = "select * from adminp"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def p():
    query = 'select * from product where p_id=%s'
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def loginAdmin(pwd):
    if pwd == 'admin':
        return 'success'
    else:
        return 'unsuccessful'
