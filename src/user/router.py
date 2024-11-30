from fastapi import APIRouter
from fastapi import  HTTPException

from src.user.schemas import AddUser, User
from src.user.service import UserRepo

router = APIRouter()
repo: UserRepo = UserRepo()

@router.get("/user", response_model=User)
def user(user_id: int) -> User:
    user = repo.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")



@router.post("/auth")
def create_user(user: AddUser):
    repo.add_user(user.name)


@router.get("/users")
def show_users():
    return repo.get_users()