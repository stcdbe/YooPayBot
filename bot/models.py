from sqlalchemy import Column, BigInteger, String, Integer
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class DBBaseModel(AsyncAttrs, DeclarativeBase):
    pass


class UserPay(DBBaseModel):
    __tablename__ = 'userpay'
    id = Column(Integer, unique=True, primary_key=True)
    userid = Column(BigInteger, unique=True)
    label = Column(String, unique=True)
