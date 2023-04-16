import os, requests
import helpers

class Service(object):
  def __init__(self):
    # find token and setup headers object
    token = os.getenv('WANIKANI_TOKEN')
    if not token:
      raise Exception('secret token not found')

    self.headers = {'Authorization': 'Bearer ' + token}

  # get a list of reviews for the last 24 hours
  # if an item was reviews multiple times in this time period use the most recent review
  def get_recent_reviews(self, date):
    request_url = 'https://api.wanikani.com/v2/reviews?updated_after=' + date
    response = requests.get(url=request_url, headers=self.headers).json()
    return response

  '''
  process reviews into an organized dict for frontend use
  '''
  def process_reviews(raw_reviews):
    # declare useful vars
    srs_num_to_stage = helpers.SRS_STAGES_DICT
    processed_reviews = {
      'correct': {},
      'wrong': {}
    }

    # if there are any duplicates, we only want to most recent review
    deduped_reviews = {}
    for review in sorted(raw_reviews['data'], key=lambda r: r['data']['created_at']):
      # this will replace any older review records with a newer version if there are multiple reviews for the same subject
      deduped_reviews[review['data']['subject_id']] = review

    for subject_id, review in deduped_reviews.items():
      # check if this item was correct or wrong in most recent review
      key1 = 'correct'
      if review['data']['ending_srs_stage'] < review['data']['starting_srs_stage']:
        key1 = 'wrong'

      current_stage = srs_num_to_stage[str(review['data']['ending_srs_stage'])]

      try:
        processed_reviews[key1][current_stage].append(review)
      except:
        processed_reviews[key1][current_stage] = [review]

    return processed_reviews
