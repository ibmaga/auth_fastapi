from pydantic import BaseModel, EmailStr, constr, ConfigDict


class User(BaseModel):
    username: str
    email: EmailStr


class UserFull(User):
    model_config = ConfigDict(from_attributes=True)

    password: constr(min_length=8)


class Token(BaseModel):
    access_token: str
