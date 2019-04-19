from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')


@app.route("/about")
def about():
	return render_template('about.html')


@app.route("/createAccount", methods=['GET', 'POST'])
def createAccount():
	return render_template('createAccount.html')


@app.route("/login")
def login():
	return render_template('login.html')


@app.route("/contact-us")
def contact():
	return render_template('contact.html')


if __name__ == '__main__':
	app.run(debug=True)	
