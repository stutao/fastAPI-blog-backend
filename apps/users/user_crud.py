from hashlib import new
from shortuuid.main import uuid
from sqlalchemy.orm import Session
from .schemas import UserAchemas
from apps.users.model import Users
import shortuuid


def create_user(db: Session, user_info: UserAchemas):
    user_uuid = shortuuid.uuid()
    new_user = Users(
        uuid=user_uuid,
        name=user_info.name,
        nick_name=user_info.nick_name,
        email=user_info.email,
        avatar=user_info.avatar
    )
    # TODO:还没写完 下次继续
    pass
