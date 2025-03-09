import configparser

import requests

from email_services.interfaces.data_access_helper import DataAccessHelper


class MailTrapEmailDataAccess(DataAccessHelper):

    def get_email_content(self) -> dict:
        config = configparser.ConfigParser()
        config.read("email_credentials.ini")
        api_token = config["MAIL_TRAP"]["api_token"]
        inbox_id = config["MAIL_TRAP"]["inbox_id"]
        headers = {"Api-Token": api_token, "Content-Type": "application/json"}
        response = requests.get(f"https://mailtrap.io/api/v1/inboxes/{inbox_id}/messages", headers=headers)
        if response.status_code == 200:
            emails = response.json()
            last_email = emails[0]
            return  {
                    "sender": last_email['from_email'],
                    "recipient": last_email['to_email'],
                    "subject": last_email['subject'],
                    "body": last_email['text_body']
                }
        return {}
