from abc import ABC, abstractmethod

class EmailServiceSMTP(ABC):
    @abstractmethod
    def send_email_smtp(self, sender: str, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to the specified recipient.

        :param sender:
        :param recipient: The recipient's email address.
        :param subject: The email subject.
        :param body: The email content.
        """
        pass