import os


# retrieve private token from virtual environment
WANIKANI_TOKEN = os.environ.get('wanikani_token')

if WANIKANI_TOKEN is None:
    print('token not found, make sure you are in the virtual environment by running \'source venv/bin/activate\'')
    exit(-1)
else:
    print('private token found')

