from flask_wtf import Form
import re
from wtforms import TextField, IntegerField, TextAreaField, SubmitField

from wtforms import validators, ValidationError

class ContactForm(Form):
	email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

	senderName = TextField("Name*", [validators.Required("Please enter your name")])

	senderEmail = TextField("Email*", [validators.Required("Please enter your email address"), \
		validators.Regexp(email_regex, message = "Email addresses must be in the form: name@example.com")])

	senderPhone = TextField("Phone Number")

	senderMessage = TextAreaField("Message*", [validators.Required("Please enter your message")])

	submit = SubmitField("Send")
