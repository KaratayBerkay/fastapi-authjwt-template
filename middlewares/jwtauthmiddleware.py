import arrow
from typing import Union

from starlette import status
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi_jwt_auth.exceptions import AuthJWTException

from fastapi import HTTPException
from fastapi_jwt_auth.auth_jwt import AuthJWT

from Root_Configs.__configs import config_a, config_b, config_c, config_d, config_zero

now_date = arrow.utcnow().shift(hours=3)


class AuthHeaderMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        start_time, start_micro = now_date.time().__str__(), now_date.time().microsecond
        request_path = str(request.url.__str__())
        request_url_ext = str(request.url.path)

        response = await call_next(request)
        auth_jwt = AuthJWT(req=request)

        end_time, end_micro = now_date.time().__str__(), now_date.time().microsecond
        response.headers['request-starts'], response.headers['request-ends'] = start_time, end_time
        response.headers['elapsed-Time'] = str(end_micro - start_micro) + " ms"
        response.headers['request-path'] = str(request_path)
        response.headers['server_app'] = str(config_a["APP_URL_API"])
        # response.headers['agent'] = str(request.headers['User-Agent'])
        # response.headers['platform'] = str(request.headers['sec-ch-ua-platform'])

        check_auth_in_headers = any(request_url_ext in path for path in config_a["paths_to_ignore_at_token_check"])
        if not check_auth_in_headers:  # Check if url is insecure or secure
            try:
                auth_jwt.jwt_required()
                current_sub = auth_jwt.get_jwt_subject()
                print('1', current_sub, now_date)
            except AuthJWTException as error_auth:
                err_dict = error_auth.__dict__
                if err_dict['status_code'] == 401:
                    return JSONResponse(content={"message": "Session expired. Please login again.",
                                                 "tmstp": now_date.__str__(),
                                                 "context": err_dict},
                                        status_code=401)
                if err_dict['status_code'] == 422:
                    try:
                        auth_jwt.jwt_refresh_token_required()
                        current_sub = auth_jwt.get_jwt_subject()
                        print('2', current_sub, now_date)
                        access_token = auth_jwt.create_access_token(subject=current_sub,
                                                                    algorithm=config_b["ALGORITHM"])
                        auth_jwt.set_access_cookies(encoded_access_token=access_token,
                                                    response=response,
                                                    max_age=1000)
                        if current_sub:
                            return response
                    except Exception as e:
                        err = e
                return JSONResponse(content={"message": "Session unauthorized.",
                                             "tmstp": now_date.__str__()},
                                    status_code=401)

        return response
