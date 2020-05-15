import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from email_class import SendEmail

app = Flask(__name__)
app.secret_key = os.environ["secret_key"]


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

        send_grid = SendEmail(request.form.get("from_name"), request.form.get("from_email"), request.form.get("message_text"))
        send_grid.email()
        flash("Email Sent")
        return render_template("contact.html")

    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
