from services.user_service import UserService


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_user(self, user_id: int, name: str, email: str):
        return self.user_service.create_user(user_id, name, email)

    def get_user(self, user_id: int):
        user = self.user_service.get_user(user_id)
        return user if user else "User not found"

    def list_users(self):
        return self.user_service.list_users()

    def delete_user(self, user_id: int):
        return "User deleted" if self.user_service.remove_user(user_id) else "User not found"
