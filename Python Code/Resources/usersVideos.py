#!/usr/bin/env python3
from flask import Flask, jsonify, abort, request, make_response
from flask_restful import Resource, Api
import pymysql.cursors
import settings
import json

class UsersVideos(Resource):
    def get(self, userName):
        try:
            dbConnection = pymysql.connect(settings.MYSQL_HOST,
                settings.MYSQL_USER,
                settings.MYSQL_PASSWD,
                settings.MYSQL_DB,
                charset='utf8mb4',
                cursorclass= pymysql.cursors.DictCursor)
            sqlProcName = 'getOneUser'
            sqlArgs = (userName,)
            cursor = dbConnection.cursor()
            cursor.callproc(sqlProcName, sqlArgs)
            user = cursor.fetchone()
            if user is None:
			             abort(404)
            id = user.get("userId")
            sqlProcName = 'getAUsersVideos'
            sqlArgs = (id,)
            cursor = dbConnection.cursor()
            cursor.callproc(sqlProcName, sqlArgs)
            videos = cursor.fetchall()
        except pymysql.MySQLError as e:
            print(e)
        finally:
            cursor.close()
            dbConnection.close()
        return make_response(jsonify({'Videos': videos}), 200)
