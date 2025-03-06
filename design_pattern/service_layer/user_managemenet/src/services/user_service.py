from services.user_service_interface import UserServiceInterface
from repositories.user_repository import UserRepository
from models.user import User


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_id: int, name: str, email: str) -> User:
        user = User(id=user_id, name=name, email=email)
        return self.user_repository.add_user(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user_by_id(user_id)

    def list_users(self):
        return self.user_repository.get_all_users()

    def remove_user(self, user_id: int) -> bool:
        return self.user_repository.delete_user(user_id)
