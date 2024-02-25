import smtplib
from email.mime.text import MIMEText

def send_notification():
    sender_email = ""
    receiver_email = ""
    subject = "Task-tracker Heartbeat Alert"
    body = "The heartbeat check failed. Status code is not 200."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("", 465) as server:
        server.login(sender_email, "")
        server.sendmail(sender_email, receiver_email, msg.as_string())
