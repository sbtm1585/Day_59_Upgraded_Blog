import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

PASSWORD = "uximnvzaytdicloc"
FROM_EMAIL = "sbtm1337@gmail.com"

def send_form(data):
    sender_email = data["email"]
    to_email = "sbtm@live.de"
    subject = f"New message from {data["name"]}!"
    body = f"""
    Name: {data["name"]}
    Email: {data["email"]}
    Phone: {data["phone"]}

    Message: 
        {data["message"]}"""

    msg = create_message(subject, body, sender_email, to_email)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=to_email,
            msg=msg
        )


def create_message(subject, body, sender, recipient):
    message = MIMEText(body, "plain")
    message["From"] = formataddr((sender, sender))
    message["To"] = formataddr((recipient, recipient))
    message["Subject"] = Header(subject, "utf-8")
    return message.as_string()