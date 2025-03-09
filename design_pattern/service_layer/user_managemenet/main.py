from src.controllers.user_controller import UserController
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository

if __name__ == "__main__":
    user_repo = UserRepository()
    user_service = UserService(user_repo)
    user_controller = UserController(user_service)

    print("Creating Users...")
    user_controller.create_user(1, "Alice", "alice@example.com")
    user_controller.create_user(2, "Bob", "bob@example.com")

    print("\nListing Users:")
    for user in user_controller.list_users():
        print(user)

    print("\nFetching User with ID 1:")
    print(user_controller.get_user(1))

    print("\nDeleting User with ID 1:")
    print(user_controller.delete_user(1))

    print("\nListing Users after deletion:")
    for user in user_controller.list_users():
        print(user)
