# -*- coding:utf-8 -*-
import os

import shortuuid
from fastapi import UploadFile, File

from apps import router
from settings import ROOT_PATH, BASE_URL

from apps.articles.schemas import ArticlesSchemas


# 获取文章 携带user
@router.get("/article/list")
async def get_article_list():
    pass


# 创建文章 携带user
@router.post("/article/create")
async def create_article(items: ArticlesSchemas):
    print(items)


# 通过id修改文章内容
@router.put("/article/{article_id}")
async def update_article_info():
    pass


# 通过id删除文章,修改is_alive属性
@router.delete("/article/{article_id}")
async def delete_article():
    pass


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    res = await file.read()
    suffix = os.path.splitext(file.filename)[-1]
    name = shortuuid.uuid()
    path = os.path.join(ROOT_PATH, 'static', suffix + name)
    with open(path, 'wb') as f_p:
        f_p.write(res)
    return {"code": '1001', "url": BASE_URL + '/static/' + suffix + name}
