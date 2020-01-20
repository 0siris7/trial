from flask import *
from db import *
user=Blueprint("user",__name__)

@user.route('/userhome',methods=['post','get'])
def userhome():
	return render_template('userhome.html')