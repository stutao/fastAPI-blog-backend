# -*- coding:utf-8 -*-

from fastapi import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DATABASES_CONFIG

sqlite_engine = DATABASES_CONFIG.get('sqlite')
engine = create_engine(sqlite_engine, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
router = APIRouter()

from .articles import views
from .articles.model import Articles
from .users.model import Users
