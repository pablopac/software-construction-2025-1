from models.user import User


class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)
        return user

    def get_user_by_id(self, user_id: int):
        return next((user for user in self.users if user.id == user_id), None)

    def get_all_users(self):
        return self.users

    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False
