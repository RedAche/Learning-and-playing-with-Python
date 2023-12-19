from email.message import EmailMessage
from password import pwd
import ssl
import smtplib

email_sender = "anmoldev30@gmail.com"
email_password = pwd

email_receiver = "kitimis250@anawalls.com"

subject = "Hey There"
body = """
Hey there, whatsupp. Focus on studying rather than playing with your life!!!!.
"""
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
