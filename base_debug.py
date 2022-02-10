from flask import Flask, redirect, url_for, render_template, request, session, flash

global bool_DEBUG

test_app = Flask(__name__, template_folder = 'temp')
test_app.config['EXPLAIN_TEMPLATE_LOADING'] = True
#app.secret_key = "adskjbsk"

@test_app.route('/', methods=["POST", "GET"])
def home():
	return render_template("index.html")


@test_app.route('/app_form', methods=["POST", "GET"])
def forms():
	if request.method == "POST":
	 	check_debug = request.form["check_debug"]
	 	if check_debug == 'on':
	 		bool_DEBUG = 1
	 	return redirect(url_for("home"))
	return render_template("values_sub.html")

# @test_app.route('/debug_on', methods=["POST", "GET"])
# def debug_on():
# 	pass


if __name__ == "__main__":
	test_app.run(host='127.0.0.1',port=4455,debug = None)
