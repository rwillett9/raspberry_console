from flask import json as flask_json
from datetime import datetime as dt
from datetime import timedelta


DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
SRS_STAGES_DICT = {
  '1': 'apprentice',
  '2': 'apprentice',
  '3': 'apprentice',
  '4': 'apprentice',
  '5': 'guru',
  '6': 'guru',
  '7': 'master',
  '8': 'enlightened',
  '9': 'burned'
}

def formatted_date_day_ago():
  return dt.strftime(dt.utcnow() - timedelta(days=1), DATE_FORMAT)

def formatted_date_now():
  return dt.strftime(dt.utcnow(), DATE_FORMAT)

def json_response(payload, status=200):
  return (flask_json.dumps(payload), status, {'content-type': 'application/json'})
