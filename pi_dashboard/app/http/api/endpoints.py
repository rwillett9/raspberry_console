import sys
from flask import Flask, json
from flask_cors import CORS, cross_origin
from app.user.service import Service as UserService


app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
@cross_origin()
def index():
  user = UserService().find_user()
  return json_response({'username': user['data']['username']})


# helper function
def json_response(payload, status=200):
  return (json.dumps(payload), status, {'content-type': 'application/json'})
