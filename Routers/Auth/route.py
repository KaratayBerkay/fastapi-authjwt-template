from fastapi import APIRouter, status
from fastapi_jwt_auth import AuthJWT
from starlette.requests import Request
from starlette.responses import Response

# from pydantics.input_models import Login, AccessToken, RefresherToken
# from pydantics.output_models import SuccessResponse, FailureResponse
# from templates import jinja_env

from Routers.Auth.functions import handle_jwt_token_with_credentials


# Router [Authentication] starts here...
auth_route = APIRouter(prefix='/auth', tags=['Authentication'])
auth_route.include_router(auth_route, include_in_schema=True)


@auth_route.post(path="/login", summary='Login with credential and password')
def router_auth(response: Response, request: Request, login_input: dict):
    handle_jwt_token_with_credentials(response=response, credentials=login_input, request=request)
    return {"login": True}
    # access_, refresh_ = handle_jwt_token_with_credentials(response=response, credentials=login_input, request=request)
    # "tokens": {"access": access_, "refresh": refresh_}


@auth_route.post(path="/logout", summary='Logout')
def router_auth(response: Response, request: Request):
    authorize = AuthJWT(req=request)
    authorize.unset_access_cookies(response=response)
    authorize.unset_refresh_cookies(response=response)
    return {"login": False}


#
# @auth_route.post(path="/check_password", summary='Login check credential and password')
# def router_check_pwd(credentials: Login):
#     new_user = UserAccessKey.find_one(access_key=credentials.credential)
#     # print(new_user.id)
#     if not new_user:
#         return FailureResponse(status_code=status.HTTP_401_UNAUTHORIZED, message="Credentials are not verified")
#     user = User.find_one(id=new_user.user_id)
#     # print(user.id)
#     if not user:
#         return FailureResponse(status_code=status.HTTP_401_UNAUTHORIZED, message="User is not verified")
#
#     if verify_password(login_input=credentials, hashed_pass=user.hash_password) is False:
#         return FailureResponse(status_code=status.HTTP_401_UNAUTHORIZED, message="User is not verified")
#     print("truemu")
#
#     return SuccessResponse(status_code=status.HTTP_200_OK, message="Login check credential and password",
#                            payload={'reminder_day': str(user.remainder_day())})
#
#
# @auth_route.post(path='/logout', summary="User logged out logs")
# def router_log_out(request: Request):
#     # print(request.headers)
#     token = request.headers.get('Authorization', None)
#     # print("router out token : ", token)
#     user, r_headers, local_ip = read_access_token(jwt_token=token), request.headers, request.client.host
#     # print(user, 'User logged out logs to api...')
#     agent = r_headers.get('user-agent', default=None)
#     platform = r_headers.get('sec-ch-ua-platform', default=None)
#     # User session record will be filled @database[UserLoggedOut]
#     # print(user['sub'])
#     info_ = dict(uid=-1)
#
#     if user:
#         user_table = User.find_one(id=user['sub'])
#         # print(user_table)
#         if user_table is not None:
#             info_['uid'] = user_table.id
#             info_['last_time'] = user['last_time']
#             UserLoggedOut.create(user_id=user_table.id, agent=agent, local_ip=local_ip, platform=platform)
#         return SuccessResponse(status_code=status.HTTP_200_OK, message="User is logged out", payload=info_)
#     return FailureResponse(status_code=status.HTTP_401_UNAUTHORIZED, payload=info_,
#                            message="User is Not HTTP_401_UNAUTHORIZED logged out")
#
#
# @auth_route.post(path='/check_token')
# def router_check_token(access_token: AccessToken):
#     acc = access_token.access_token
#     try:
#         user_id = read_access_token(jwt_token=str(acc))
#     except jwt.exceptions.ExpiredSignatureError:
#         return FailureResponse(status_code=status.HTTP_401_UNAUTHORIZED, message="Token is NOT valid")
#     user = User.find_one(id=user_id)
#     if user:
#         return SuccessResponse(status_code=status.HTTP_200_OK, message="Token is valid")
#     return FailureResponse(status_code=status.HTTP_401_UNAUTHORIZED, message="Token is NOT valid")
#
#
# @auth_route.post(path='/remind_me_token')
# def router_check_reminder(refresher_token: RefresherToken):
#     acc = refresher_token.refresher_token
#     try:
#         user_id = read_access_token(jwt_token=str(acc))
#     except jwt.exceptions.ExpiredSignatureError:
#         return FailureResponse(status_code=status.HTTP_401_UNAUTHORIZED, message="Token is NOT valid")
#     user = User.find_one(id=user_id)
#     if user:
#         return SuccessResponse(status_code=status.HTTP_200_OK, message="Token is valid")
#     return FailureResponse(status_code=status.HTTP_401_UNAUTHORIZED, message="Token is NOT valid")
#
# # Router [User] ends here...
