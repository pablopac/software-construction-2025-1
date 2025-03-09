from email.message import EmailMessage

from email_services.interfaces.smtp_email_service import EmailServiceSMTP
import smtplib
import configparser


class EtherealEmailService(EmailServiceSMTP):
    config = configparser.ConfigParser()
    config.read("email_credentials.ini")
    user = config["ETHEREAL"]["username"]
    password = config["ETHEREAL"]["password"]
    port = 587

    def send_email_smtp(self, sender: str, recipient: str, subject: str, body: str) -> None:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient
        msg.set_content(body)
        with smtplib.SMTP("smtp.ethereal.email", self.port) as server:
            server.starttls()
            server.login(self.user, self.password)
            server.send_message(msg)
