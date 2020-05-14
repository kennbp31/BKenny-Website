import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from boto.s3.connection import S3Connection
import smtplib

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

        # Handle using local variables, will be removed once local testing is complete.
        if not os.environ["username"]:
            server = smtplib.SMTP_SSL("smtp.gmail.com", S3Connection(os.environ["port"]))
            server.login(S3Connection(os.environ["username"]), S3Connection(os.environ["pass"]))
            server.sendmail(
                request.form.get("from_email"),
                S3Connection(os.environ["to"]),
                "Name: " + request.form.get("from_name") + ", Message: " + request.form.get(
                    "message_html"))
            server.quit()

        # Setup for Heroku App Vaiables.
        else:
            server = smtplib.SMTP_SSL("smtp.gmail.com", os.environ["port"])
            server.login(os.environ["username"], os.environ["pass"])
            server.sendmail(
                request.form.get("from_email"),
                os.environ["to"],
                "Name: " + request.form.get("from_name") + ", Message: " + request.form.get("message_html"))
            server.quit()

    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
