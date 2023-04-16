import os, requests
from service import Service

class SubjectsService(Service):
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

  def process_subjects(raw_subjects):
    processed_subjects = {}
    for subject in raw_subjects:
      # @TODO might have to deal with images here
      # if subject['data']['characters'] is not None:
      #   pass
      processed_subjects[subject['id']] = {
        'type': subject['object']
      }
      try:
        processed_subjects[subject['id']]['character'] = subject['data']['characters']
      except:
        try:
          processed_subjects[subject['id']]['image'] = subject['data']['character_images'][0]['url']
        except:
          print('no characters or images: %s' % subject)

    return processed_subjects
