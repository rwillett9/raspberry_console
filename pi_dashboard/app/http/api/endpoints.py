import sys
from flask import Flask, json
from flask_cors import CORS, cross_origin
from app.assignments.service import Service as AssignmentsService
from app.subjects.service import Service as SubjectsService
from app.user.service import Service as UserService
from app.japaneseWOTD.service import Service as WOTDService


app = Flask(__name__)
CORS(app)

# helper function
def json_response(payload, status=200):
  return (json.dumps(payload), status, {'content-type': 'application/json'})

'''
this function is mainly used as a test to make sure this project was setup properly, also returns the user's username
'''
@app.route('/test', methods=['GET'])
@cross_origin()
def test():
  user = UserService().find_user()
  return json_response({'username': user['data']['username']})

'''
this function will provide the data for the main WaniKani dashboard:
{
  'assignment_stats': {
    # the 'levels' key will contain stats per level
    'levels': {
      '1': {
        'kanji': 13, # total number of Kanji items ready for review
        'radical': 12, # total number of radicals ready for review
        'total': 20, # total number of items ready for review
        'vocabulary': 5 # number of vocabulary items ready for review
      }, ...
    },
    # these keys will provide overall stats
    'kanji': 13, # total number of Kanji items ready for review
    'radical': 12, # total number of radicals ready for review
    'total': 20, # total number of items ready for review
    'vocabulary': 5 # number of vocabulary ready for review
  },
  'username': 'NinjaDino' # your username
}
'''
@app.route('/review-stats', methods=['GET'])
@cross_origin()
def get_current_assignments():
  # get assignment data
  available_assignments = AssignmentsService().get_available_assignments()
  # use the subject ids to gather subject data (each review item is a 'subject')
  subject_ids = [a['data']['subject_id'] for a in available_assignments]
  subjects = SubjectsService().get_subjects_by_id_list(subject_ids)

  # calculate meaningful statistics
  assignment_stats = {
    'levels': {},
    'kanji': 0,
    'radical': 0,
    'total': 0,
    'vocabulary': 0
  }
  for subject in subjects:
    subject_type = subject['object']
    subject_level = subject['data']['level']

    assignment_stats[subject_type] += 1
    assignment_stats['total'] += 1
    try:
      assignment_stats['levels'][subject_level]['total'] += 1
    except KeyError:
      assignment_stats['levels'][subject_level] = {
        'kanji': 0,
        'radical': 0,
        'total': 1,
        'vocabulary': 0
      }
    assignment_stats['levels'][subject_level][subject_type] += 1

  return json_response({
    'assignment_stats': assignment_stats,
    'username': UserService().get_username()
  })

@app.route('/word-of-the-day', methods=['GET'])
@cross_origin()
def get_word_of_the_day():
  word_of_the_day_data = WOTDService().get_word_of_the_day()
  print(word_of_the_day_data)

  return json_response(word_of_the_day_data)
