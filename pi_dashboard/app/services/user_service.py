import os, requests
from service import Service

class UserService(Service):
  def __init__(self):
    # find token and setup headers object
    token = os.getenv('WANIKANI_TOKEN')
    if not token:
      raise Exception('secret token not found')

    self.headers = {'Authorization': 'Bearer ' + token}

  # get user based on secret token
  def find_user(self):
    user = requests.get(url='https://api.wanikani.com/v2/user', headers=self.headers)
    return user.json()

  # return the username of the user associated with the secret token
  def get_username(self):
    user = requests.get(url='https://api.wanikani.com/v2/user', headers=self.headers)
    return user.json()['data']['username']
