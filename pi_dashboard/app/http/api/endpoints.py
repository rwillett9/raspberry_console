import sys
from flask import Flask, json
from flask_cors import CORS
from app.user.service import Service as UserService


app = Flask(__name__)
CORS(app)

@app.route('/user', methods=['GET'])
def index():
  return json_response(UserService().find_user())


# helper function
def json_response(payload, status=200):
  return (json.dumps(payload), status, {'content-type': 'application/json'})
