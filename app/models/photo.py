# -*- coding: utf-8 -*-

from app import db
from sqlalchemy.dialects.mysql import BIGINT, DATE, DECIMAL, TIMESTAMP
from sqlalchemy.sql.expression import text

import datetime


class PhotoModel(db.Model):
    __tablename__ = 'photos'

    id = db.Column(
        BIGINT(20, unsigned=True),
        primary_key=True,
        index=True
    )

    title = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    # 위도 경도 고도 표시
    captured_latitude = db.Column(
        DECIMAL(10, 7)
    )

    captured_longitude = db.Column(
        DECIMAL(10, 7)
    )

    captured_date = db.Column(
        DATE,
        nullable=False
    )

    create_date = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        server_default=text('CURRENT_TIMESTAMP')
    )

    updated_date = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )

    # join할 것
    user_id = db.Column(
        BIGINT(20, unsigned=True),
        db.ForeignKey('users.id'),
        nullable=False
    )

    def __init__(self, title, captured_latitude, captured_longitude, captured_date, user_id):
        self.title = title
        self.captured_latitude = captured_latitude
        self.captured_longitude = captured_longitude
        self.captured_date = captured_date
        self.user_id = user_id
