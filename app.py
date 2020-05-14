import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
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
        server = smtplib.SMTP_SSL("smtp.gmail.com", os.environ["port"])
        server.login(os.environ["username"], os.environ["pass"])
        server.sendmail(
            request.form.get("from_email"),
            os.environ["to"],
            "<HTML>" + "Name " + request.form.get("from_name") + "/n" + request.form.get("message_html") + "</HTML>")
        server.quit()

    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
