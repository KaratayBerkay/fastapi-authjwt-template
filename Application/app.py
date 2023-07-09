import arrow
import uvicorn

from os.path import join, dirname, abspath
from smtplib import SMTPException

from fastapi_jwt_auth.auth_jwt import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from Root_Configs.__configs import config_a, config_b, config_c, config_d, config_zero

from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi

from passlib.context import CryptContext

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.staticfiles import StaticFiles

from pydantic.error_wrappers import ValidationError
from sqlalchemy_mixins.exception import SqlAlchemyException

from Routers.Auth.configs_auth import Settings
from Routers.Auth.route import auth_route
from middlewares.jwtauthmiddleware import AuthHeaderMiddleware

from Errors.error_handlers import sqlalchemy_error, http_error, valid_error, smtp_error, auth_error
from Root_Configs.__configs import config_a, config_b, config_c, config_d, config_zero


ALL_ROUTERS = [auth_route]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")   # Password hashing


def create_app():
    api_app = FastAPI(title=config_a["TITLE"], default_response_class=JSONResponse)

    @api_app.get('/', summary=config_a["TITLE"] + ' ' + config_a["DESCRIPTION"])
    async def home():
        return RedirectResponse(url='/docs')

    @api_app.get("/protected")
    def protected_route():
        # Use the current_user object
        username = "Berkay"
        return {"message": f"Hello, user {username}"}

    @api_app.post('/salut', summary="SALUT")
    async def salut():
        return {
            "app_name": config_a["APP_NAME"],
            "title": config_a["TITLE"],
            "description": config_a["DESCRIPTION"],
            "app_url_api": config_a["APP_URL_API"],
            "app_url": "<APP_URL>",
            "app_root": dirname(dirname(abspath(__file__))),
            "salut": "API handshakes with client. Says Hi!",
            "tmstp": arrow.utcnow().__str__(),
            "user": None,
            "roots": '-'.join(str(router.prefix) for router in list(ALL_ROUTERS))
        }

    register_routers(api_app)
    api_app.openapi_schema = make_doc(api_app)
    api_app.add_exception_handler(SqlAlchemyException, sqlalchemy_error)
    api_app.add_exception_handler(HTTPException, http_error)
    api_app.add_exception_handler(ValidationError, valid_error)
    api_app.add_exception_handler(SMTPException, smtp_error)
    api_app.add_exception_handler(AuthJWTException, auth_error)
    # api_app.mount(path="/statics", app=StaticFiles(directory="statics"), name="statics")

    return api_app


def make_doc(in_app):
    openapi_schema = get_openapi(
        title=config_a["TITLE"],
        description=config_a["DESCRIPTION"],
        version='0.0.1',
        routes=in_app.routes
    )

    # if "components" in openapi_schema:
    #     openapi_schema["components"]["securitySchemes"] = {
    #         "Bearer": {
    #             "type": "apiKey",
    #             "scheme": "bearer",
    #             "in": "header",
    #             "name": "Authorization",
    #             "description": "Enter: **'Bearer &lt;JWT&gt;'**, where JWT is the access token"
    #         }
    #     }

    for route in in_app.routes:

        if route.include_in_schema is False:
            continue
        path = getattr(route, "path")
        methods = [method.lower() for method in getattr(route, "methods")]

        for method in methods:

            if path != '/' and path not in config_a["paths_to_ignore_at_token_check"]:
                openapi_schema["paths"][path][method]["security"] = [
                    {
                        "Bearer": []
                    }]
                openapi_schema["paths"][path][method]["responses"]['403'] = {
                    "content": {"application/json": {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}},
                    "description": "Returned if user is unauthorized.",
                }

    return openapi_schema


def configure_static(in_app):
    static_path = join(dirname(dirname(abspath(__file__))), 'static')
    in_app.router.default = StaticFiles(directory=static_path)


def register_routers(in_app):
    for router in list(ALL_ROUTERS):
        in_app.include_router(router)


cors_ = {
    'allow_origins': ["*"],
    'allow_credentials': True,
    'allow_methods': ["*"],
    'allow_headers': ["*"]
}

app = create_app()


app.add_middleware(CORSMiddleware, **cors_)
app.add_middleware(AuthHeaderMiddleware)
# app.add_middleware(SessionMiddleware, secret_key=config_a["SECRET_KEY"], same_site='none', https_only=False)


CONFIG = Settings()


@AuthJWT.load_config
def get_config():
    """Load AuthJWT settings"""
    return CONFIG


if __name__ == "__main__":
    __config_c = {
        "app_name": "app:app",
        "host": "127.0.0.1",  # todo connect localhost
        "port": 8088,
        "log_level": "info",
        "reload": True,
    }
    uvicorn.Server(uvicorn.Config(
        app=__config_c['app_name'], host=__config_c['host'], port=__config_c['port'],
        log_level=__config_c['log_level'], reload=__config_c['reload'])).run()

