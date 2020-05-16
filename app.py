import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from email_class import SendEmail, BuildEmail

app = Flask(__name__)
send_email = SendEmail()
build_email = BuildEmail()

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
        # Include user input in the message text
        build_email.from_name = request.form.get("fname")
        build_email.from_email = request.form.get("email")
        build_email.message_text = request.form.get("message_text")

        # Include the message in the send_mail function
        send_email.message = str(build_email.build_email())

        # Attempt to send the email
        if send_email.send_email() == 'success':
            # Display confirmation message to user.
            flash("Email Sent", category='primary')

        else:
            # Display message failed error to the user
            flash('Email Failed', category='danger')
        return render_template("contact.html")

    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
