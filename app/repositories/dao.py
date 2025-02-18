from app.db.models import UserInDB
from app.repositories.basedao import CRUD


class BaseCRUD(CRUD):
    model = UserInDB
