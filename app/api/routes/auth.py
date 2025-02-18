from fastapi import Depends, APIRouter

from app.api.dependencies import get_service
from app.api.schemas.user import User
from app.api.schemas.other import Token
from app.errors import ErrorResponseModel
from app.services.about_jwt import create_jwt
from app.services.services import CRUDService

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"model": ErrorResponseModel}},
)


@router.post("/sign-up/")
async def register_user(
    user: User,
    crud: CRUDService = Depends(get_service),
) -> Token:
    token = create_jwt(user.username)
    await crud.add_user(user.model_dump())
    return Token(access_token=token)
