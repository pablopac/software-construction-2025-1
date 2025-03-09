import pytest

from email_services.data_access.ethereal_email_data_access import EtherealEmailDataAccess
from email_services.services.ethereal_email_service import EtherealEmailService
from email_services.services.mail_trap_email_service import MailTrapEmailService
from email_services.data_access.mail_trap_email_data_access import MailTrapEmailDataAccess

@pytest.mark.mail_trap
def test_send_email_api_mail_trap():
    mail_trap_email_service = MailTrapEmailService()
    email_data_access = MailTrapEmailDataAccess()
    sender = "sender@inbox.mailtrap.io"
    recipient = "recipient@inbox.mailtrap.io"
    subject = "You are awesome!"
    body = "Congrats for sending test email with Mailtrap!"
    email_data = {"sender":sender,"recipient": recipient, "subject": subject, "body": body}
    mail_trap_email_service.send_email_api(sender, recipient, subject, body)
    email_content = email_data_access.get_email_content()
    assert email_data == email_content

@pytest.mark.ethereal
def test_send_email_ethereal():
    mail_trap_email_service = EtherealEmailService()
    email_data_access = EtherealEmailDataAccess()
    sender = "sender@inbox.ethereal.io"
    recipient = "recipient@inbox.ethereal.io"
    subject = "You are beautiful!"
    body = "This a message for you: never give up!\r\n"
    email_data = {"sender":sender,"recipient": recipient, "subject": subject, "body": body}
    mail_trap_email_service.send_email_smtp(sender, recipient, subject, body)
    email_content = email_data_access.get_email_content()
    assert email_data == email_content


