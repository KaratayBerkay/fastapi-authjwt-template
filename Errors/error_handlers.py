from fastapi.exceptions import HTTPException, FastAPIError
from sqlalchemy_mixins.exception import SqlAlchemyException

from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic.error_wrappers import ValidationError
from smtplib import SMTPException
from fastapi_jwt_auth.exceptions import AuthJWTException


def fastapi_error(request: Request, exc: FastAPIError) -> JSONResponse:
    # todo print(exc.message.__str__())
    return JSONResponse(
        content={
            'exception': exc.__str__(),
            'request': request.url.__str__()}
    )


def sqlalchemy_error(request: Request, exc: SqlAlchemyException) -> JSONResponse:
    # todo print(exc.message.__str__())
    return JSONResponse(
        content={
            'exception': exc.message.__str__(),
            'request': request.url.__str__()}
    )


def http_error(request: Request, exc: HTTPException) -> JSONResponse:
    # todo  print(exc.detail.__str__())
    return JSONResponse(
        content={
            'exception': exc.detail.__str__(),
            'request': request.url.__str__()
        }
    )


def valid_error(request: Request, exc: ValidationError) -> JSONResponse:
    # todo print(str(exc.model))
    return JSONResponse(
        content={
            'exception': str(exc.model),
            'request': request.url.__str__(),
            'json': exc.json()
        }
    )


def smtp_error(request: Request, exc: SMTPException) -> JSONResponse:
    # todo print(exc.strerror.__str__())
    return JSONResponse(
        content={
            'exception': exc.strerror.__str__(),
            'request': request.url.__str__()
        }
    )


def auth_error(request: Request, exc: AuthJWTException) -> JSONResponse:
    # todo print(exc.strerror.__str__())
    return JSONResponse(
        content={
            'exception': exc.__str__(),
            'request': request.url.__str__()
        }
    )
