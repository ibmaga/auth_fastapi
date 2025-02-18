from app.utils.unitofwork import IUnitOfWork
from app.api.schemas import UserFull


class CRUDService:

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_user(self, user: dict):
        async with self.uow:
            await self.uow.crud.add_user(user)
            await self.uow.commit()

    async def get_user(self, username: str):
        async with self.uow:
            result = await self.uow.crud.get_user(username)
            await self.uow.commit()
            return UserFull.model_validate(result)

    async def update_user(self, username: str, user: dict):
        async with self.uow:
            await self.uow.crud.update_user(username, UserFull(**user))
            await self.uow.commit()
