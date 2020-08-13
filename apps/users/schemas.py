
# 写数据库字段检验
from pydantic import BaseModel
from typing import List, Optional


class UserAchemas(BaseModel):
    name: str
    nick_name: str
    email: str
    avatar: str = None
    password_hash: str

    class Config:
        orm_mode = True
