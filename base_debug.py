from flask import Flask, redirect, url_for, render_template, request, session, flash



test_app = Flask(__name__, template_folder = 'temp')
test_app.config['EXPLAIN_TEMPLATE_LOADING'] = True
#app.secret_key = "adskjbsk"

@test_app.route('/' or '/home')
def home():
	return render_template("index.html")


if __name__ == "__main__":
	test_app.run(host='127.0.0.1',port=4455,debug = None)