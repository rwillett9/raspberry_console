import os
import requests

class BaseWanikaniService(object):
  # initialize wanikani secret token and setup header field to use it for auth purposes
  def __init__(self):
    # find token and setup headers object
    token = os.getenv('WANIKANI_TOKEN')
    if not token:
      raise Exception('secret token not found')

    self.headers = {'Authorization': 'Bearer ' + token}

  # wrapper for requests.get, avoid needing to use self.headers in all subclass requests
  def do_get_request(self, url, params=None, headers={}):
    return requests.get(url=url, params=params, headers={**headers, **self.headers})
