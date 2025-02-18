from fastapi import FastAPI
import logfire

from app.errors import (
    UserExistsException,
    not_fount_handler,
    BadJWTException,
    bad_jwt_handler,
)
from app.api.routes import auth

app = FastAPI()
logfire.configure()
logfire.instrument_fastapi(app)

app.add_exception_handler(UserExistsException, not_fount_handler)
app.add_exception_handler(BadJWTException, bad_jwt_handler)

app.include_router(auth.router)
