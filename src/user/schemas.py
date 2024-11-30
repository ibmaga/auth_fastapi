from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str


class AddUser(BaseModel): 
    name: str
