# -*- coding: utf-8 -*-

from app import db

from sqlalchemy.dialects.mysql import BIGINT, DATE

#import datetime


class UserModel(db.Model):
    __tablename__ = 'users'

    gender_enums = ('male', 'female', 'others')

    id = db.Column(
        BIGINT(20, unsigned=True),
        primary_key=True,
        index=True
    )

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(150),
        nullable=False
    )

    nickname = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    birthday = db.Column(
        DATE,
        nullable=False
    )

    gender = db.Column(
        db.Enum(*gender_enums),
        default=gender_enums[0],
        server_default=gender_enums[0]
    )

    def __init__(self, username, password, nickname, birthday, gender):
        self.username=username
        self.password=password
        self.nickname=nickname
        self.birthday=birthday
        self.gender=gender
