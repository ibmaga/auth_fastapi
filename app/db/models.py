from sqlalchemy.orm import Mapped, mapped_column

from app.db.sessions import Base


class UserInDB(Base):
    __tablename__ = "users2"

    username: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
