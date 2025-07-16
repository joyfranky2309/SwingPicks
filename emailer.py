import smtplib, ssl
from email.mime.text import MIMEText
from dotenv import load_dotenv; load_dotenv()
import os, agent

def send_email(body):
    sender, pwd = os.getenv("GMAIL_USER"), os.getenv("GMAIL_PASS")
    msg = MIMEText(body)
    msg["Subject"] = "📈 Morning Swing Picks – {}".format(agent.datetime.date.today())
    msg["From"] = sender
    msg["To"] = sender
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, pwd)
        server.send_message(msg)

if __name__ == "__main__":
    send_email(agent.get_picks())