from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql import func
# from sqlalchemy

Base = declarative_base()


class ExampleTable(Base):
    __tablename__ = 'example_table'
    id = Column(Integer, primary_key=True)
    date_column = Column(DateTime)


def current_month_firstday(xdate=None):
    result = session.query(func.TO_DATE(
        text("'' || EXTRACT(YEAR FROM xdate) || '-' || EXTRACT(MONTH FROM xdate) || '-1'"), 'YY-MM-DD'
    )).first()

    if result[0] is None:
        result = session.query(func.current_timestamp()).first()

    session.close()
    return result[0]








