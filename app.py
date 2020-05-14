import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from boto.s3.connection import S3Connection
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

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
        msg = MIMEMultipart()
        msg['From'] = 'kennbp31@gmail.com'
        msg['To'] = 'kennbp31@gmail.com'
        msg['Subject'] = 'simple email in python'
        message = 'here is the email'
        msg.attach(MIMEText(message))

        print(msg.as_string())
        mailserver = smtplib.SMTP('smtp.sendgrid.net', 587)
        # identify ourselves to smtp gmail client

        mailserver.login(os.environ["username"], os.environ["pass"])

        mailserver.sendmail("kennbp31@gmail.com", "kennbp31@gmail.com", msg.as_string())
        mailserver.quit()

    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
