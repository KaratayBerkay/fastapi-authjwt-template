from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func
from Database.base_mixin import session

from datetime import timezone
import datetime

# Getting the current date and time
dt = datetime.datetime.now(timezone.utc)
utc_time = dt.replace(tzinfo=timezone.utc)
utc_timestamp = utc_time.timestamp()

print(utc_timestamp)

Base = declarative_base()


def current_month_firstday(xdate=None):
    result = session.query(func.TO_DATE(
        text("'' || EXTRACT(YEAR FROM xdate) || '-' || EXTRACT(MONTH FROM xdate) || '-1'"), 'YY-MM-DD'
    )).first()

    if result[0] is None:
        result = session.query(func.current_timestamp()).first()

    session.close()
    return result[0]