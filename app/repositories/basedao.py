from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.errors import NotFoundException, UserExistsException
from app.api.schemas.user import User


class ICRUD(ABC):

    @abstractmethod
    async def add_user(self, user: dict):
        pass

    @abstractmethod
    async def get_user(self, username: str):
        pass

    @abstractmethod
    async def update_user(self, username: str, user: User):
        pass


class CRUD(ICRUD):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, user: dict):
        user_db = self.model(**user)
        try:
            self.session.add(user_db)
        except IntegrityError:
            raise UserExistsException

    async def get_user(self, username: str):
        user = await self.session.get(self.model, username)
        if user:
            return user
        raise NotFoundException

    async def update_user(self, username: str, user: User):
        user_db = await self.session.get(self.model, username)

        if user_db:
            user_db.username = user.username
            user_db.email = str(user.email)
            user_db.password = user.password

        raise NotFoundException
