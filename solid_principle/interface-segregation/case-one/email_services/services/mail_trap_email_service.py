import json

from email_services.interfaces.api_email_service import EmailServiceAPI
from email_services.interfaces.smtp_email_service import EmailServiceSMTP
import smtplib
import requests
import configparser


class MailTrapEmailService(EmailServiceSMTP, EmailServiceAPI):
    config = configparser.ConfigParser()
    config.read("email_credentials.ini")
    user = config["MAIL_TRAP"]["username"]
    password = config["MAIL_TRAP"]["password"]
    api_token = config["MAIL_TRAP"]["api_token"]
    inbox_id = config["MAIL_TRAP"]["inbox_id"]
    port = 2525

    def send_email_api(self, sender: str, recipient: str, subject: str, body: str) -> None:
        url = "https://sandbox.api.mailtrap.io/api/send/{0}".format(self.inbox_id)

        payload = {
            "from": {"email": sender, "name": "Mailtrap Test Sender"},
            "to": [{"email": recipient}],
            "subject": subject,
            "text": body,
            "category": "Integration Test"
        }
        headers = {
            "Authorization": "Bearer {0}".format(self.api_token),
            "Content-Type": "application/json"
        }
        requests.request("POST", url, headers=headers, data=json.dumps(payload))

    def send_email_smtp(self, sender: str, recipient: str, subject: str, body: str) -> None:
        message = f"""\
        Subject: {subject}
        To: {recipient}
        From: {sender}
        {body}"""
        with smtplib.SMTP("sandbox.smtp.mailtrap.io", self.port) as server:
            server.starttls()
            server.login(self.user, self.password)
            server.sendmail(sender, recipient, message)
