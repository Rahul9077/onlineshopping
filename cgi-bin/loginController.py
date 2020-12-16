import cgi
import model


form = cgi.FieldStorage()
email = form.getvalue("email")
password = form.getvalue("password")

data = model.loginUser(email, password)
import mainPage