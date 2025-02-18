from src.users.schemas import AuthModel


class UserRepo:
    def __init__(self):
        self.users: list[AuthModel] = []

    def get_user_by_id(self, user_id: int) -> AuthModel | None:
        for user in self.users:
            if user.id == user_id:
                return user

    def add_user(self, email: str, password: str) -> AuthModel | dict:
        user: AuthModel = AuthModel(email=email, password=password)
        self.users.append(user)
        return user

    def get_users(self) -> list[AuthModel] | None:
        return self.users
