# -*- coding:utf-8 -*-
import os

import shortuuid
from fastapi import UploadFile, File, Depends, Path
from sqlalchemy.orm import Session

from apps import router
from settings import ROOT_PATH, BASE_URL
from apps.articles.schemas import ArticlesSchemas
from . import article_crud
from apps.commons.db_session import get_db


# 获取文章 携带user
@router.get("/article/{article_id}")
async def get_article_detail(db: Session = Depends(get_db),
                             article_id: int = Path(..., title='The ID of the article to get details')):
    details = article_crud.get_aritles_by_id(db, article_id)
    return {'code': 1001, "msg": '完事', "data": details}


# 创建文章 携带user
@router.post("/article/create")
async def create_article(article_item: ArticlesSchemas,
                         user_id: str,
                         db: Session = Depends(get_db),):

    add_article = article_crud.create_article(db, article_item, user_id)
    if not add_article:
        return {"code": 4003, "msg": '创建失败'}
    return {"code": 2001, "msg": "success"}


# 通过id修改文章内容
@router.put("/article/{article_id}")
async def update_article_info():
    pass


# 通过id删除文章,修改is_alive属性
@router.delete("/article/{article_id}")
async def delete_article():
    pass


@router.post("/img/upload")
async def upload(file: UploadFile = File(...)):
    res = await file.read()
    suffix = os.path.splitext(file.filename)[-1]
    name = shortuuid.uuid()
    path = os.path.join(ROOT_PATH, 'static', name+suffix)
    with open(path, 'wb') as f_p:
        f_p.write(res)
    return {"code": '1001', "url": BASE_URL + '/static/' + name+suffix}
