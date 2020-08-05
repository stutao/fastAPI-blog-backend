# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from apps import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    niki_name = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=False)

    articles = relationship('Articles', back_populates='author')
