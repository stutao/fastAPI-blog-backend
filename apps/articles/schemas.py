# -*- coding:utf-8 -*-

# 写数据库字段检验
from pydantic import BaseModel
from typing import List


class ArticlesSchemas(BaseModel):
    title: str
    thumbnail_url: str
    tags: List
    content: str
