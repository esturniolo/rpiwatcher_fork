from flask import Flask, render_template
import glob
import time
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


@app.route("/", methods=['GET'])
def home():
	greetings = "P&aacute;gina home sin ninguna boludez"
	return render_template('index.jade',greetings=greetings)	

@app.route("/list/", methods=['GET'])
def listPictures():
	list = glob.glob("static/img/cam/*.jpg")
	listPic = []
	for file in list:
		listPic.append("<img src='/" + file + "'>")
	return render_template('listPictures.jade', listPic=listPic)

@app.route("/current/",methods=['GET'])
def current():
	return render_template('current.jade')

@app.route("/sumavalores/",methods=['GET'])
def sumavalores():
	return render_template('sumavalores.jade')


if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")
