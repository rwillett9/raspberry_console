from flask import json as flask_json
from datetime import datetime as dt
from datetime import timedelta


DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
SRS_STAGES_DICT = {
  '1': 'Apprentice',
  '2': 'Apprentice',
  '3': 'Apprentice',
  '4': 'Apprentice',
  '5': 'Guru',
  '6': 'Guru',
  '7': 'Master',
  '8': 'Enlightened',
  '9': 'Burned'
}

def formatted_date_day_ago():
  return dt.strftime(dt.utcnow() - timedelta(days=1), DATE_FORMAT)

def formatted_date_now():
  return dt.strftime(dt.utcnow(), DATE_FORMAT)

def json_response(payload, status=200):
  return (flask_json.dumps(payload), status, {'content-type': 'application/json'})
