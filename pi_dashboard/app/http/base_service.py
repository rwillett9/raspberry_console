import os
import requests

class BaseService(object):
  def __init__(self):
    # find token and setup headers object
    token = os.getenv('WANIKANI_TOKEN')
    if not token:
      raise Exception('secret token not found')

    self.headers = {'Authorization': 'Bearer ' + token}

  def do_get_request(self, url, params, headers):
    return requests.get(url=url, params=params, headers={**headers, **self.headers})
