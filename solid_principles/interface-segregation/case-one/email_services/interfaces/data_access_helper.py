from abc import ABC, abstractmethod

class DataAccessHelper(ABC):
    @abstractmethod
    def get_email_content(self) -> dict:
        """
        Returns the content of the email.
        """
        pass