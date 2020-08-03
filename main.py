# -*- coding:utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from apps import router, Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

# 加入static路径可以访问静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 解决跨域
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
