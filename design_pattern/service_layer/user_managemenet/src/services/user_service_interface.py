from abc import ABC, abstractmethod
from models.user import User


class UserServiceInterface(ABC):

    @abstractmethod
    def create_user(self, user_id: int, name: str, email: str) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def list_users(self):
        pass

    @abstractmethod
    def remove_user(self, user_id: int) -> bool:
        pass
