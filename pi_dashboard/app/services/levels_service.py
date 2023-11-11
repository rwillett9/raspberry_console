import os, requests
from service import Service

class LevelsService(Service):
  def __init__(self):
    # find token and setup headers object
    token = os.getenv('WANIKANI_TOKEN')
    if not token:
      raise Exception('secret token not found')

    self.headers = {'Authorization': 'Bearer ' + token}

  # get data on all levels for this user
  def get_all_levels(self):
    levels = requests.get(url='https://api.wanikani.com/v2/level_progressions', headers=self.headers)
    return levels.json()
