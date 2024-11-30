from src.user.schemas import User

class UserRepo:
    def __init__(self):
        self.users: list[User] = [User(id=2, name='Второй')]
        self._id: int = 0

    def get_user_by_id(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user
            
    def add_user(self, name):
        self.users.append(User(id=self._id,  name=name))
        self._id += 1
    
    def get_users(self) -> list[User] | None:
        return self.users
    