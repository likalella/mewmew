# -*- coding: utf-8 -*-

import datetime
from app import app, db
from sqlalchemy import Column, Integer, String

class DocumentModel(db.Model) :
	id = db.Column(
		BIGINT(20, unsigned=True),
		primary_key = True
	)

	# join할 것
	user_id = db.Column(
		BIGINT(20, unsigned=True),
		db.ForeignKey(),
		nullable = False
	)

	# join할 것
	photo_id = db.Column(
		BIGINT(20, unsigned=True),
		db.ForeignKey(),
		nullable = False
	
	