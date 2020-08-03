# -*- coding:utf-8 -*-

from fastapi import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from settings import DATABASES_CONFIG

sqlite_engine = DATABASES_CONFIG.get('sqlite')
engine = create_engine(sqlite_engine, echo=False)

Base = declarative_base()
router = APIRouter()

from .articles import views
from .articles.model import Articles
