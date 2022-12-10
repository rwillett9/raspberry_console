import os
import requests


# retrieve private token from virtual environment
WANIKANI_TOKEN = os.getenv('WANIKANI_TOKEN')

if WANIKANI_TOKEN is None:
  print('token not found, make sure you are in the virtual environment by running \'source venv/bin/activate\'')
  exit(-1)

USERS_REQUEST_URL = 'https://api.wanikani.com/v2/user'
AUTH_HEADERS = {'Authorization': 'Bearer %s' % WANIKANI_TOKEN}

response = requests.get(url=USERS_REQUEST_URL, headers=AUTH_HEADERS)
print('private token found for user: %s' % response.json()['data']['username'])
