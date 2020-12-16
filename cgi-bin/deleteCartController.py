import cgi
import model


form = cgi.FieldStorage()
p_id = form.getvalue('p_id')


model.deleteProduct(p_id)
import mainPage.py
