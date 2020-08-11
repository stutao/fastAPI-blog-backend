# -*- coding:utf-8 -*-
from sqlalchemy.orm import Session
from .model import Articles
from .schemas import ArticlesSchemas
from apps.users.model import Users


def get_articles_by_user_id(db: Session, user_id: str):
    return db.query(Users).filter_by(id=user_id).first().articles


def get_aritles_by_id(db:Session,artilce_id:int):
    pass


def get_articles_from_fuzzy_search():
    pass


def create_article(db: Session, article_item: ArticlesSchemas, user_id: str):
    author = db.query(Users).filter_by(uuid=int(user_id)).first()
    new_artilce = Articles(
        name=article_item.title,
        thumbnail=article_item.thumbnail,
        tags="$".join(article_item.tags),
        content=article_item.content,
        author=author
    )
    db.add(new_artilce)
    db.commit()
    return new_artilce
