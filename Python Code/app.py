#!/usr/bin/env python3
from flask import Flask
from flask_restful import Resource, Api
import settings

app = Flask(__name__)

from Resources.users import Users
from Resources.user import User
from Resources.videos import Videos
from Resources.usersVideos import UsersVideos
from Resources.video import Video


#
# Error handlers
#
@app.errorhandler(400) # decorators to add to 400 response
def not_found(error):
	return make_response(jsonify( { "status": "Bad request" } ), 400)

@app.errorhandler(404) # decorators to add to 404 response
def not_found(error):
	return make_response(jsonify( { "status": "Resource not found" } ), 404)

# @app.route("/")
# def root():
#       return app.send_static_file('index.html')
class Root(Resource):
    def get(self):
      return app.send_static_file('index.html')

api = Api(app)
api.add_resource(Root, '/')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:userName>')
api.add_resource(UsersVideos, '/users/<string:userName>/videos')
api.add_resource(Videos, '/videos')
api.add_resource(Video, '/users/<userName>/videos/<string:title>')

if __name__ == "__main__":
   app.run(host=settings.APP_HOST, port=settings.APP_PORT, debug=True)
