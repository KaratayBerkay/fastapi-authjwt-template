from datetime import timedelta

from typing import Optional, Sequence, Union, List
from pydantic import BaseModel, StrictInt, StrictStr, StrictBool
from Root_Configs.__configs import config_a, config_b, config_c, config_d, config_zero


class Settings(BaseModel):
    authjwt_token_location: Optional[Sequence[StrictStr]] = config_a["AUTH"]
    authjwt_header_name: Optional[StrictStr] = "Authorization"
    authjwt_header_type: Optional[StrictStr] = "Bearer"

    authjwt_secret_key: Optional[StrictStr] = config_b["RESET_PASSWORD_SECRET_KEY"]
    authjwt_public_key: Optional[StrictStr] = config_b["RESET_PASSWORD_SECRET_KEY"]
    authjwt_private_key: Optional[StrictStr] = config_b["RESET_PASSWORD_SECRET_KEY"]

    authjwt_algorithm: Optional[StrictStr] = config_b["ALGORITHM"]

    authjwt_decode_algorithms: Optional[List[StrictStr]] = None
    authjwt_decode_leeway: Optional[Union[StrictInt, timedelta]] = 0
    authjwt_encode_issuer: Optional[StrictStr] = None
    authjwt_decode_issuer: Optional[StrictStr] = None
    authjwt_decode_audience: Optional[Union[StrictStr, Sequence[StrictStr]]] = None
    authjwt_denylist_enabled: Optional[StrictBool] = False
    authjwt_denylist_token_checks: Optional[Sequence[StrictStr]] = {'access', 'refresh'}
    authjwt_access_token_expires: Optional[Union[StrictBool, StrictInt, timedelta]] = timedelta(
        minutes=config_b["ACCESS_TOKEN_EXPIRE_MINUTES"])
    authjwt_refresh_token_expires: Optional[Union[StrictBool, StrictInt, timedelta]] = timedelta(
        minutes=config_b["RESET_PASSWORD_TOKEN_EXPIRE_MINUTES"])

    # option for create cookies
    authjwt_access_cookie_key: Optional[StrictStr] = "access_token_cookie"
    authjwt_refresh_cookie_key: Optional[StrictStr] = "refresh_token_cookie"
    authjwt_access_cookie_path: Optional[StrictStr] = "/"
    authjwt_refresh_cookie_path: Optional[StrictStr] = "/"
    authjwt_cookie_max_age: Optional[StrictInt] = 1200
    authjwt_cookie_domain: Optional[StrictStr] = None
    authjwt_cookie_secure: Optional[StrictBool] = False
    authjwt_cookie_samesite: Optional[StrictStr] = 'lax'

    # option for double submit csrf protection
    authjwt_cookie_csrf_protect: Optional[StrictBool] = False
    authjwt_access_csrf_cookie_key: Optional[StrictStr] = "csrf_access_token"
    authjwt_refresh_csrf_cookie_key: Optional[StrictStr] = "csrf_refresh_token"
    authjwt_access_csrf_cookie_path: Optional[StrictStr] = "/"
    authjwt_refresh_csrf_cookie_path: Optional[StrictStr] = "/"
    authjwt_access_csrf_header_name: Optional[StrictStr] = "X-CSRF-Token"
    authjwt_refresh_csrf_header_name: Optional[StrictStr] = "X-CSRF-Token"
    authjwt_csrf_methods: Optional[Sequence[StrictStr]] = {'POST', 'PUT', 'GET', 'DELETE'}
