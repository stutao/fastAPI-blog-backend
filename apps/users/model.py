# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from apps import Base
from hashlib import sha256


class Users(Base):
    __tablename__ = 'users'

    uuid = Column(String, primary_key=True)
    name = Column(String)
    avatar = Column(String)
    nick_name = Column(String, nullable=True)
    password_hash = Column(String)
    is_active = Column(Boolean, default=False)

    articles = relationship('Articles', back_populates='author')

    @property
    def password(self):
        raise AttributeError("password 不可读!")

    @password.setter
    def set_password(self, value):
        self.password_hash = sha256(value).hexdigest()

    def check_password(self, user_pwd):
        return sha256(user_pwd) == self.password
