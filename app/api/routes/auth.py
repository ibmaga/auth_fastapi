from fastapi import APIRouter, Depends

from app.api.schemas import User, UserFull, Token
from app.errors import ErrorResponseModel
from app.services.about_jwt import create_jwt
from app.services.services import CRUDService
from app.utils.unitofwork import IUnitOfWork, UnitOfWork

router = APIRouter(prefix="/auth", tags=["auth & users"])


async def get_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> CRUDService:
    return CRUDService(uow)


@router.post("/sign-up/", responses={401: {"model": ErrorResponseModel}})
async def register_user(
    user: UserFull, crud: CRUDService = Depends(get_service)
) -> Token:
    token = create_jwt(user.username)
    await crud.add_user(user.model_dump())
    return Token(access_token=token)


@router.get("/users/{username}", responses={401: {"model": ErrorResponseModel}})
async def get_user(username: str, crud: CRUDService = Depends(get_service)) -> User:
    return await crud.get_user(username=username)


@router.put("/users/{username}", responses={401: {"model": ErrorResponseModel}})
async def update_user(
    username: str, user: UserFull, crud: CRUDService = Depends(get_service)
):
    await crud.update_user(username, user)
    return {"status": "success"}
