from pydantic import BaseModel, EmailStr, constr, ConfigDict


class User(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    username: str


class UserFromDB(User):
    model_config = ConfigDict(from_attributes=True)
