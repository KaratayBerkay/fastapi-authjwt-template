from os.path import dirname, abspath

# todo APPLICATION DETAILS
config_zero = {"APP_NAME": "<APP_NAME>", "WEB_NAME": "<WEB_NAME>", "timezone": None, "WEB_URL": "<WEB_URL>"}

config_a = {
    "paths_to_ignore_at_token_check": ["/", "/openapi.json", "/openapi.json_files", "/docs#", "/docs",
                                       "/docs/oauth2-redirect", "/redoc", "/favicon.ico", "/auth/login",
                                       "/auth/logout"],
    "APP_NAME": "<APP_NAME>",
    "TITLE": "<APP_NAME>",
    "DESCRIPTION": "<DESCRIPTION>",
    "APP_URL_API": "<APP_URL_API>",
    "APP_URL": "<APP_URL>",
    "APP_ROOT": dirname(dirname(abspath(__file__))),
    "SECRET_KEY": "<SECRET_KEY>",
    "AUTH": {'cookies'}
}

# todo SECRET_KEYS
config_b = {
    "REFRESH_SECRET_KEY": "CVMfiKVpKrzUm1PIobuW501219064ae45bb5594a6e384997dee0eb1688420fac45ecaa59aae376db",
    "RESET_PASSWORD_SECRET_KEY": "rwO1OAgfwVYdLJk_Ig2e2e9ca62be3159438ba11c3c0418fe3ee77223e8d67a1a99ff3",
    "ACCESS_SECRET_KEY": "R11gRuUErm4rF0M0977e14195d7b355dcd3e61de68458946ec52f062cb0",

    "RESET_PASSWORD_TOKEN_EXPIRE_MINUTES": 30,  # 20 minutes
    "ACCESS_TOKEN_EXPIRE_MINUTES": 10,  # 10 minutes
    "REFRESH_TOKEN_EXPIRE_DAYS": 1,  # 1 days,

    "ALGORITHM": "HS256"
}

config_c = {
    "FIRST_DATABASE": {  # todo FIRST_DATABASE
        "DATABASE_NAME_CREDENTIALS": "<DATABASE_NAME_CREDENTIALS>",  # todo DATABASE_NAME_CREDENTIALS
        "DATABASE_NAME": "<WEB_URL>",  # todo DATABASE_NAME
        "USERNAME": "<WEB_URL>",  # todo USERNAME
        "PASSWORD": "<WEB_URL>",  # todo PASSWORD
        "PORT": "<WEB_URL>",  # todo PORT
        "HOST": "<WEB_URL>",  # todo HOST
        "SQL": "<WEB_URL>",  # todo SQL
    },
    "SECOND_DATABASE": {  # todo SECOND_DATABASE
        "DATABASE_NAME_CREDENTIALS": "<DATABASE_NAME_CREDENTIALS>",  # todo DATABASE_NAME_CREDENTIALS
        "DATABASE_NAME": "<WEB_URL>",  # todo DATABASE_NAME
        "USERNAME": "<WEB_URL>",  # todo USERNAME
        "PASSWORD": "<WEB_URL>",  # todo PASSWORD
        "PORT": "<WEB_URL>",  # todo PORT
        "HOST": "<WEB_URL>",  # todo HOST
        "SQL": "<WEB_URL>",  # todo SQL
    }
}

config_d = {   # todo get database config
    "DATABASE_URL": f"{config_c['FIRST_DATABASE']['SQL']}://"
                    f"{config_c['FIRST_DATABASE']['USERNAME']}:"
                    f"{config_c['FIRST_DATABASE']['PASSWORD']}@"
                    f"{config_c['FIRST_DATABASE']['HOST']}:"
                    f"{config_c['FIRST_DATABASE']['PORT']}/"
                    f"{config_c['FIRST_DATABASE']['DATABASE_NAME']}",
    "SERVER_NAME": "<SERVER_NAME>",
    "USERNAME": "<USERNAME>",
    "PASSWORD": "<PASSWORD>",
    "DEFAULT_MAIL": "<DEFAULT_MAIL>",
    "SENDER_MAIL": "<SENDER_MAIL>",
    "DEFAULT_ENCODE": "<DEFAULT_ENCODE>",
    "HOSTNAME": "<HOSTNAME>",
    "PORT": 465,
    "DEBUG": False,
    "SSL": True,
}

# todo get DATABASE from here...
""" 
    config_d["DATABASE_URL"]
    config_d["SERVER_NAME"]
    config_d["USERNAME"]
    config_d["PASSWORD"]
    config_d["DEFAULT_MAIL"]
    config_d["SENDER_MAIL"]
    config_d["DEFAULT_ENCODE"]
    config_d["HOSTNAME"]
    config_d["PORT"]
    config_d["DEBUG"]
    config_d["SSL"]
"""


# todo get Root_Configs from here...
"""
    config_a["paths_to_ignore_at_token_check"]
    config_a["APP_NAME"]
    config_a["TITLE"]
    config_a["DESCRIPTION"]
    config_a["APP_URL_API"]
    config_a["SECRET_KEY"]
    config_a["AUTH"]
"""
# todo get Auth config from here...
"""
    config_b["RESET_PASSWORD_SECRET_KEY"]
    config_b["ACCESS_SECRET_KEY"]
    config_b["REFRESH_SECRET_KEY"]
    config_b["ALGORITHM"]
    config_b["ACCESS_TOKEN_EXPIRE_MINUTES"]
    config_b["RESET_PASSWORD_TOKEN_EXPIRE_MINUTES"]
    config_b['REFRESH_TOKEN_EXPIRE_DAYS']
"""