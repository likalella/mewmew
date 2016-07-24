# -*- coding: utf-8 -*-

import datetime
from app import app, db

class PhotoModel(db.Model) : 
	__tablename__ = 'photos'	

	id = db.Column(
		BIGINT(20, unsigned=True),
		primary_key = True
	)

	title = db.Column(
		db.String(80),
		unique = True,
		nullable = False
	)

	# join할 것
	user_id = db.Column(
		BIGINT(20, unsigned=True),
		db.ForeignKey(),
		nullable = False
	)

	# 위도 경도 고도 표시
	captured_latitude = db.Column(
	)

	captured_longitude = db.Column(
	)

	captured_date = db.Column(
		DATE,
		nullable = False
	)

	create_date = db.Column(
		DATE,
		nullable = False
	)

	updated_date = db.Column(
		DATE,
		nullable = False
	)
