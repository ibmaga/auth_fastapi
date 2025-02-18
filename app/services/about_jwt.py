import jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime

from app.configs import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="sign-up")
algorithm = "HS256"
EXP = datetime.now() + timedelta(minutes=15)
SECRET_KEY = settings.SECRETKEY


def create_jwt(username: str):
    data = {"sub": username, "exp": EXP}

    return jwt.encode(payload=data, key=SECRET_KEY, algorithm=algorithm)


def decode_jwt(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=algorithm)
    return payload["sub"]
