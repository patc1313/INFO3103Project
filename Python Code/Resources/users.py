#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request, make_response
from flask_restful import Resource, Api
import pymysql.cursors
import settings
import json

class Users(Resource):
	def get(self):
		try:
			dbConnection = pymysql.connect(settings.MYSQL_HOST,
				settings.MYSQL_USER,
				settings.MYSQL_PASSWD,
				settings.MYSQL_DB,
				charset='utf8mb4',
				cursorclass= pymysql.cursors.DictCursor)
			sqlProcName = 'getAllUsers'
			cursor = dbConnection.cursor()
			cursor.callproc(sqlProcName)
			users = cursor.fetchall()
		except pymysql.MySQLError as e:
			print(e)
		finally:
			cursor.close()
			dbConnection.close()
		return make_response(jsonify({'Users': users}), 200)
