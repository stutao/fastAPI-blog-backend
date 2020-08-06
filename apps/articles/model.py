# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from apps import Base


class Articles(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    article_name = Column(String)
    thumbnail_url = Column(String)
    content = Column(Text)
    # 还有点赞量,阅读量,还可以加收藏量
    # 加一个is_active 表示删除,这样后面想恢复也是可以的呀.
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship('Users', back_populates='articles')
