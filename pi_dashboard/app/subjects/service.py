import os, requests

class Service(object):
  def __init__(self):
    # find token and setup headers object
    token = os.getenv('WANIKANI_TOKEN')
    if not token:
      raise Exception('secret token not found')

    self.headers = {'Authorization': 'Bearer ' + token}

  def get_subjects_by_id_list(self, ids):
    request_url = 'https://api.wanikani.com/v2/subjects?ids=' + ','.join([str(i) for i in ids])

    # deal with possible pagination of results and collect subject objects
    subjects = []
    get_more = True
    while get_more:
      response = requests.get(url=request_url, headers=self.headers).json()
      subjects.extend(response['data'])

      if response['pages']['next_url'] is not None:
        request_url = response['pages']['next_url']
      else:
        get_more = False

    return subjects
