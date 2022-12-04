import os
import requests


# retrieve private token from virtual environment
WANIKANI_TOKEN = os.environ.get('wanikani_token')

if WANIKANI_TOKEN is None:
    print('token not found, make sure you are in the virtual environment by running \'source venv/bin/activate\'')
    exit(-1)
else:
    print('private token found')

USERS_REQUEST_URL = 'https://api.wanikani.com/v2/user'
AUTH_HEADERS = {'Authorization': 'Bearer %s' % WANIKANI_TOKEN}

response = requests.get(url=USERS_REQUEST_URL, headers=AUTH_HEADERS)
print(response.json())
