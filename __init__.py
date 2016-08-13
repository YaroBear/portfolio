mport os
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from forms import ContactForm

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/contact/', methods = ['POST', 'GET'])
def contact():
	form = ContactForm()
	if request.method == "POST":
		if form.validate() == False:
			flash("All fields required:")
			return render_template("main.html", form = form)
		else:
			name = request.form['senderName']
			email = request.form['senderEmail']
			phone = request.form['senderPhone']
			message = request.form['senderMessage']
			msg = Message("Hello", sender = app.config['MAIL_USERNAME'], recipients = ['berejnoi.yaroslav@gmail.com'])
			msg.body = "From: "+name+" / "+email+" / "+phone+" \n\n "+message+""
			mail.send(msg)
			return "Sent"

@app.route('/', methods = ["GET", "POST"])
def homepage():
	form = ContactForm()
	return render_template("main.html", form = form)

@app.route('/random-quote-machine')
def quotemachine():
	return render_template("quotemachine.html")

@app.route('/weather-app')
def weatherApp():
	return render_template("weatherApp.html")





if __name__ == "__main__":
    app.run(debug = False)
