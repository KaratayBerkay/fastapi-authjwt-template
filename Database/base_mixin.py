import uuid

from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, TIMESTAMP, Boolean
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_mixins.crud_mixin import CrudMixin
from sqlalchemy_mixins.base_query import BaseQuery
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy import inspect

from Root_Configs.__configs import config_a, config_b, config_c, config_d

engine = create_engine(url=config_d["DATABASE_URL"], convert_unicode=True, pool_size=100, echo=True)
session = scoped_session(sessionmaker(autocommit=True, query_cls=BaseQuery, bind=engine))
Base = declarative_base()
Base.query = session.query_property()
# inspector = inspect(engine)


class BaseMixin(Base, CrudMixin):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    created_at = Column(TIMESTAMP, server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=text('now()'), onupdate=text('now()'), nullable=False)
    deleted = Column(Boolean, server_default='false')
    replication_id = Column(Integer, server_default="0")


BaseMixin.set_session(session)




