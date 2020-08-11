# -*- coding:utf-8 -*-

# 写数据库字段检验
from pydantic import BaseModel
from typing import List, Optional


class ArticlesSchemas(BaseModel):
    title: str
    thumbnail: Optional[str] = None
    tags: List[str] = []
    content: str

    class Config:
        orm_mode = True
