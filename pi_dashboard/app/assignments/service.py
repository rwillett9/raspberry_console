import os, requests
from datetime import datetime


class Service(object):
  ASSIGNMENTS_BASE_URL = 'https://api.wanikani.com/v2/assignments'

  def __init__(self):
    # find token and setup headers object
    token = os.getenv('WANIKANI_TOKEN')
    if not token:
      raise Exception('secret token not found')

    self.headers = {'Authorization': 'Bearer ' + token}

  # get assignments that are currently available as of the current time
  def get_available_assignments(self):
    # build request url
    query_parameters = [
      'available_before=%s' % (datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))
    ]
    request_url = '?' + '&'.join(query_parameters)

    # deal with possible pagination of results
    assignments = []
    get_more = True
    while get_more:
      response = requests.get(url=Service.ASSIGNMENTS_BASE_URL + request_url, headers=self.headers).json()
      print(response)
      assignments.extend(response['data'])

      if response['pages']['next_url'] is not None:
        request_url = response['pages']['next_url']
      else:
        get_more = False

    # return the list of assignments objects
    return assignments
