import configparser
import email
import imaplib


class EtherealEmailDataAccess:

    @staticmethod
    def get_email_content() -> dict:
        config = configparser.ConfigParser()
        config.read("email_credentials.ini")
        user = config["ETHEREAL"]["username"]
        password = config["ETHEREAL"]["password"]
        port = 993
        imap_server = "imap.ethereal.email"

        mail = imaplib.IMAP4_SSL(imap_server, port)
        mail.login(user, password)

        mail.select("inbox")
        status, messages = mail.search(None, "ALL")

        email_ids = messages[0].split()
        latest_email_id = email_ids[-1]

        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        last_message = None
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                raw_email = response_part[1]
                msg = email.message_from_bytes(raw_email)

                body = [part.get_payload(decode=True).decode() if msg.is_multipart() else msg.get_payload(
                    decode=True).decode() for part in msg.walk()]

                last_message = {
                    "sender": msg['From'],
                    "recipient": msg['To'],
                    "subject": msg['Subject'],
                    "body": body[-1]
                }
        mail.logout()
        return last_message

