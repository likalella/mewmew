# -*- coding: utf-8 -*-

from app import db

from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP
from sqlalchemy.sql.expression import text

import datetime


class DocumentModel(db.Model):
    __tablename__ = 'documents'

    id = db.Column(
        BIGINT(20, unsigned=True),
        primary_key=True,
        index=True
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

    content = db.Column(
        db.String(300)
    )

    # join할 것
    user_id = db.Column(
        BIGINT(20, unsigned=True),
        db.ForeignKey('users.id'),
        nullable=False
    )

    # join할 것
    photo_id = db.Column(
        BIGINT(20, unsigned=True),
        db.ForeignKey('photos.id'),
        nullable=False
    )

    def __init__(self, user_id, photo_id):
        self.user_id = user_id
        self.photo_id = photo_id
