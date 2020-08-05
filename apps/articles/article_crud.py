# -*- coding:utf-8 -*-
from sqlalchemy.orm import Session
from .model import Articles
from apps.users.model import Users


def get_articles_by_user_id(db: Session):
    return db.query(Users).filter_by(id=1).first().articles


def get_all_articles():
    pass


def get_articles_from_fuzzy_search():
    pass
