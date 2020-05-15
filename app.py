import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
<<<<<<< Updated upstream
from boto.s3.connection import S3Connection
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
=======
from email_class import SendEmail

app = Flask(__name__)

app.secret_key = os.environ["secret_key"]
>>>>>>> Stashed changes


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/resume')
def resume():
    return render_template("resume.html")


@app.route('/story')
def story():
    return render_template("story.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
<<<<<<< Updated upstream
        msg = MIMEMultipart()
        msg['From'] = os.environ["from"]
        msg['To'] = os.environ["to"]
        msg['Subject'] = 'Portfolio Inquiry'
        message = ("Name: " + request.form.get("from_name") + " , Email: " + request.form.get("from_email")
                   + " , Message: " + request.form.get("message_html"))
        msg.attach(MIMEText(message))

        print(msg.as_string())
        mailserver = smtplib.SMTP(os.environ["smtp"], os.environ["port"])

        mailserver.login(os.environ["username"], os.environ["pass"])

        mailserver.sendmail(os.environ["from"], os.environ["to"], msg.as_string())
        mailserver.quit()
=======
        send_grid = SendEmail(request.form.get("from_name"), request.form.get("from_email"), request.form.get("message_text"))
        send_grid.email()
        flash("Email Sent")
>>>>>>> Stashed changes
        return render_template("contact.html")

    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
