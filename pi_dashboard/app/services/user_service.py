import os, requests
from base_service import BaseWanikaniService

class UserService(BaseWanikaniService):
  # get user based on secret token
  def find_user(self):
    user = self.do_get_request(url='https://api.wanikani.com/v2/user')
    return user.json()

  # return the username of the user associated with the secret token
  def get_username(self):
    user = self.find_user()
    try:
      return user['data']['username']
    except:
      return 'Error retrieving user'
