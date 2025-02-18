from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi import status, Request

from .err_models import ErrorResponseModel


class UserExistsException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        message: str = "User already exists",
        error_code: str = "user_exists",
    ):
        self.error_code = error_code
        super().__init__(
            status_code=status_code,
            detail=message,
            headers={"X-ErrorHandleTime": "0.1"},
        )


class BadJWTException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        message: str = "Invalid jwt",
        error_code: str = "invalid_jwt",
    ):
        self.error_code = error_code
        super().__init__(
            status_code=status_code,
            detail=message,
            headers={"WWW-Authenticate": "Bearer"},
        )


class NotFoundException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_404_NOT_FOUND,
        message: str = "User not found",
        error_code: str = "user_not_found",
    ):
        self.error_code = error_code
        super().__init__(status_code=status_code, detail=message)


def not_fount_handler(request: Request, exc: UserExistsException):
    error = ErrorResponseModel(
        status_code=exc.status_code, message=exc.detail, error_code=exc.error_code
    ).model_dump()
    return JSONResponse(status_code=exc.status_code, content=error)


def bad_jwt_handler(request: Request, exc: BadJWTException):
    error = ErrorResponseModel(
        status_code=exc.status_code, message=exc.detail, error_code=exc.error_code
    ).model_dump()
    return JSONResponse(status_code=exc.status_code, content=error)
