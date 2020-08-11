# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from apps import Base


class Articles(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    thumbnail = Column(String)
    # 本想采用多对多,不过只能有四个标签,考虑自己拼接字符串,用'$'隔开
    tags = Column(String, nullable=True)
    content = Column(Text)
    # 还有点赞量,阅读量,还可以加收藏量
    views = Column(Integer, default=0)
    upvote = Column(Integer, default=0)
    # 加一个is_delete 表示删除,这样后面想恢复也是可以的呀.
    is_delete = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey("users.uuid"))

    author = relationship('Users', back_populates='articles')
