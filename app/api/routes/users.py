from fastapi import APIRouter

from app.api.dependencies import crud_dep
from app.api.schemas.user import User
from app.errors import ErrorResponseModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={401: {"model": ErrorResponseModel}},
)


@router.get("/username}")
async def get_user(username: str, crud: crud_dep) -> User:
    return await crud.get_user(username=username)


@router.put("/{username}")
async def update_user(
    username: str,
    user: User,
    crud: crud_dep,
):
    await crud.update_user(username, user)
    return {"status": "success"}
