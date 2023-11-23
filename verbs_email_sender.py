from email.message import EmailMessage
import ssl
import smtplib
from json_url import VerbsHandler
import sys


def send_email(email_sender, email_password, email_receiver):
    email_subject = "English exercise"

    port = 465

    verbs_handler =  VerbsHandler()
    body = verbs_handler.random_verbs()

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = email_subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(body)

        print("\nThese random verbs has been sent to receiver")


send_email(sys.argv[1], sys.argv[2], sys.argv[3])