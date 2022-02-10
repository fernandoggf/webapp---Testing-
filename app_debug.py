from flask import Flask, redirect, url_for, render_template


app = Flask(__name__, template_folder = 'temp')



app.config['EXPLAIN_TEMPLATE_LOADING'] = True



@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title="HomePage")


@app.route('/values_sub', methods=["POST", "GET"])
def values_sub():
	return render_template("values_sub.html", title="Debug Values")



if __name__ == "__main__":
	app.run(host='127.0.0.1',port=4450,debug = None)
