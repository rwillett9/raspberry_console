import os, requests
from base_service import BaseService

class UserService(BaseService):
  # get user based on secret token
  def find_user(self):
    user = requests.get(url='https://api.wanikani.com/v2/user', headers=self.headers)
    return user.json()

  # return the username of the user associated with the secret token
  def get_username(self):
    user = requests.get(url='https://api.wanikani.com/v2/user', headers=self.headers)
    return user.json()['data']['username']
