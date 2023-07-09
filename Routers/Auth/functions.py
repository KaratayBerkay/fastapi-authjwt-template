from fastapi import HTTPException
from fastapi_jwt_auth import AuthJWT
from starlette.requests import Request
from starlette.responses import Response
from werkzeug.security import check_password_hash, generate_password_hash
from Root_Configs.__configs import config_a, config_b, config_c, config_d, config_zero


# todo Login handle jwt toke with credentials
def handle_jwt_token_with_credentials(response: Response, credentials: dict, request: Request):
    credentials = {"credential": "berkay", "password": "akjskldjaklsdk"}
    user_credentials = {"credential": "berkay", "password": "akjskldjaklsdk"}

    pwd_user = str(credentials.get("credential")) + str(credentials.get("password"))
    pwd_db = str(user_credentials.get("credential")) + str(user_credentials.get("password"))

    pass_encoded = generate_password_hash(password=pwd_db)
    pass_not_correct = check_password_hash(pwhash=str(pass_encoded), password=pwd_user)

    if not pass_not_correct:
        raise HTTPException(status_code=401, detail="Invalid password")

    authorize = AuthJWT()

    access_token = authorize.create_access_token(
        subject=str("USER-891789723"),
        algorithm=config_b["ALGORITHM"],
    )
    refresh_token = authorize.create_refresh_token(
        subject=str("USER-891789723"),
        algorithm=config_b["ALGORITHM"],
    )

    authorize.set_access_cookies(
        encoded_access_token=access_token,
        response=response,
        max_age=1000)

    authorize.set_refresh_cookies(
        encoded_refresh_token=refresh_token,
        response=response,
        max_age=1000)

    return access_token, refresh_token
