import time
from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import JWTError, jwt

SECRET_KEY = 'SAVE'
ALGORITHM = 'HS256'

def create_token(data: dict):
    expire = time.time() + 1800
    data.update({'expire': expire})
    
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return {'token': encoded_jwt, 'user_data': data}

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail='Invalid or expired token',
            headers={'WWW-Authenticate': 'Bearer'}
        )
