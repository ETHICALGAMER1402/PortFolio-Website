from flask import Flask, render_template, request,url_for,redirect
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


my_email = "ethicalgamer1402@gmail.com"
password1 = "aouyzmowuwsfawvg"


app = Flask(__name__)

@app.route("/" , methods=["GET","POST"])
def home():
    if request.method == "POST":
        full_name = request.form.get('Full Name')
        email = request.form.get('Email Address')
        phone_number = request.form.get('Phone Number')
        subject = request.form.get('Email Subject')
        message = request.form.get('Your Message')

        body = f"Name: {full_name}\nEmail: {email}\nPhone Number: {phone_number}\nSubject: {subject}\nMessage: {message}"
        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain'))
        msg['Subject'] = "New Message from the Website"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password1)

        connection.sendmail(from_addr=my_email, to_addrs="sairajallrounderconcreators@gmail.com", msg=msg.as_string())
        connection.quit()
        return redirect(url_for('home'))
    return render_template("index.html")
    


if __name__ == "__main__":
    app.run(debug=True)
