from flask import Flask, redirect, url_for, render_template, flash, Response
from forms import values_debug
from debug_1 import * 

app = Flask(__name__, template_folder = 'temp')



app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.config['SECRET_KEY'] = 'sfsf31ddqDEWD23'



@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title="HomePage")


@app.route("/values_sub", methods=["GET", "POST"])
def values_sub():
	form = values_debug()
	if form.validate_on_submit() & form.debug.data ==True:
		__status = init_script_debug(1, "http://127.0.0.1:4450/ ")
		return Response(__status, mimetype='text/html'), render_template("home_debug_on.html", title="Debug On")
	return render_template("values_sub.html", title="Debug Values", form=form)



if __name__ == "__main__":
	app.run(host='127.0.0.1',port=4450,debug = None)