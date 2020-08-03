# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, Text
from apps import Base


class Articles(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    article_name = Column(String)
    thumbnail_url = Column(String)
    content = Column(Text)
