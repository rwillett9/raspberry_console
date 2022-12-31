import sys
from flask import Flask, json
from flask_cors import CORS, cross_origin
from app.assignments.service import Service as AssignmentsService
from app.user.service import Service as UserService


app = Flask(__name__)
CORS(app)

# helper function
def json_response(payload, status=200):
  return (json.dumps(payload), status, {'content-type': 'application/json'})

# this function is mainly used as a test to make sure this project was setup properly, also returns the user's username
@app.route('/test', methods=['GET'])
@cross_origin()
def test():
  user = UserService().find_user()
  return json_response({'username': user['data']['username']})

@app.route('/current-assignments', methods=['GET'])
@cross_origin()
def get_current_assignments():
  username = UserService().get_username()
  available_assignments = AssignmentsService().get_available_assignments()
  return json_response({'username': username, 'assignments': available_assignments})
