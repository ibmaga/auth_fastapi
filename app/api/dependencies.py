from typing import Annotated
from fastapi import Depends

from app.services.services import CRUDService
from app.utils.unitofwork import IUnitOfWork, UnitOfWork


async def get_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> CRUDService:
    return CRUDService(uow)


crud_dep = Annotated[CRUDService, Depends(get_service)]
