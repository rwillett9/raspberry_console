import os, requests
from time import gmtime, strftime
from urllib.parse import quote


class Service(object):
  def __init__(self):
    # find token and setup headers object
    token = os.getenv('WANIKANI_TOKEN')
    if not token:
      raise Exception('secret token not found')

    self.headers = {'Authorization': 'Bearer ' + token}

  # get assignments that are currently available as of the current time
  def get_available_assignments(self):
    query_parameters = [
      'available_before=%s' % (strftime('%Y-%m-%dT%H:%M:%SZ', gmtime()))
    ]
    request_url = '?' + '&'.join(query_parameters)

    # deal with possible pagination of results and collect assignment objects
    assignments = []
    get_more = True
    while get_more:
      response = requests.get(url='https://api.wanikani.com/v2/assignments' + request_url, headers=self.headers).json()
      assignments.extend(response['data'])

      if response['pages']['next_url'] is not None:
        request_url = response['pages']['next_url']
      else:
        get_more = False

    # return the list of assignments objects
    return assignments
