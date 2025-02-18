from fastapi import APIRouter
from fastapi import HTTPException

from src.users.jwt import create_token
from src.users.schemas import AuthModel
from src.users.service import UserRepo

router = APIRouter()
repo: UserRepo = UserRepo()


@router.post("/create", response_model=AuthModel)
def create_user(data: AuthModel) -> AuthModel | dict:
    id = repo.add_user(email=data.email, password=data.password)
    return create_token({'id': id})


@router.get("/users")
def show_users():
    return repo.get_users()
