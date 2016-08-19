import os
import sqlite3 as sql
from flask import Flask, render_template, request, flash, redirect
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

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
	form = ContactForm()
	section = 'contact_tab' #reloaded page scrolls back down to contact form
	if request.method == "POST":
		if form.validate() == False:
			flash("All fields required:")
			return render_template("main.html", form = form, section = section)
		else:
			name = request.form['senderName']
			email = request.form['senderEmail']
			phone = request.form['senderPhone']
			message = request.form['senderMessage']
			msg = Message("Hello", sender = app.config['MAIL_USERNAME'], recipients = ['berejnoi.yaroslav@gmail.com'])
			msg.body = "From: "+name+" / "+email+" / "+phone+" \n\n "+message+""
			mail.send(msg)
			success = "Message Sent!"
			return render_template("result.html", message = success)

@app.route('/', methods = ["GET", "POST"])
def homepage():
	form = ContactForm()
	
	con = sql.connect("projects.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from projects")
	rows = cur.fetchall()

	return render_template("main.html", form = form, rows = rows)

@app.route('/random-quote-machine')
def quotemachine():
	return render_template("quotemachine.html")

@app.route('/weather-app')
def weatherApp():
	return render_template("weatherApp.html")

@app.route('/edit-projects', methods = ['GET', 'POST'])
def add_project():
	if request.method == 'POST':
		name = request.form['project']
		link = request.form['link']
		description = request.form['description']
		dependencies = request.form['dependencies']
		language = request.form ['language']

		try:
			con = sql.connect("projects.db")
			cur = con.cursor()
			cur.execute("insert into projects (link, name, description, dependencies, language) \
				values (?,?,?,?,?)",(link, name, description, dependencies, language))
			con.commit()
			msg = "Project added successfully"

		except:
			con.rollback()
			msg = "Error adding to db"

		finally:
			con.close()
			return render_template("result.html", message = msg)
	else:
		con = sql.connect("projects.db")
		con.row_factory = sql.Row
		cur = con.cursor()
		cur.execute("select * from projects")
		rows = cur.fetchall()
		return render_template('edit-project.html', rows = rows)

@app.route('/delete-project', methods = ['POST'])
def delete_project():
	if request.method == 'POST':
		con = sql.connect("projects.db")
		con.row_factory = sql.Row
		cur = con.cursor()
		cur.execute("select * from projects")
		rows = cur.fetchall()

		project = request.form.get("project", '')
		con.execute("delete from projects where name=(?)",(project,))
		con.commit()
		con.close()

		return redirect('edit-projects')



if __name__ == "__main__":
    app.run(debug = False)
