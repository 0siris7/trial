from flask import *
from db import *
from admin import admin
public=Blueprint("public",__name__)
@public.route('/',methods=['post','get'])
def home():
	return render_template("publichome.html")
@public.route('/login',methods=['post','get'])
def login():
	if 'submit'in request.form:
		uname=request.form['uname']
		pwd=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,pwd)
		print(q)
		res=select(q)
		if res:
			if res[0]['type']=="admin":
				return redirect(url_for('admin.adminhome'))

			else:
				return redirect(url_for('user.userhome'))
	return render_template("login.html")


@admin.route('/adminform', methods = ['get', 'post'])
def register():
	if 'register' in request.form:
		return render_template("registerhome.html")


