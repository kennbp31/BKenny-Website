import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from email_class import EmailSender, EmailBuilder, Result


app = Flask(__name__)
send_email = EmailSender()

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

        # Construct email format
        build_e = EmailBuilder()

        # Include user input in the message text
        build_e.build_email(request.form.get("fname"), request.form.get("email"), request.form.get("message_text"))

        # Pass the built email to the email sender and send it
        if send_email.send_email(build_e.email_msg) == Result.success:
            # Display confirmation message to user.
            flash("Email Sent", category='primary')

        else:
            # Display message failed error to the user
            flash('Email Failed', category='danger')
        return render_template("contact.html")

    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
