import os, requests
import helpers
from service import Service

class ReviewsService(Service):
  # get a list of reviews for the last 24 hours
  # if an item was reviews multiple times in this time period use the most recent review
  def get_recent_reviews(self, date):
    request_url = 'https://api.wanikani.com/v2/reviews?updated_after=' + date
    response = requests.get(url=request_url, headers=self.headers).json()
    return response

  '''
  process reviews into an organized dict for frontend use, format:
  {
    'correct': {
      'apprentice': [ raw_review_struct1, raw_review_struct2, ... ],
      'burned': [ raw_review_struct1 ],
      'enlightened: [ raw_review_struct1 ]
    },
    'wrong': {
      'apprentice': [ raw_review_struct1, raw_review_struct2, ... ],
    }
  }
  '''
  def process_reviews(raw_reviews):
    # declare useful vars
    srs_num_to_stage = helpers.SRS_STAGES_DICT
    processed_reviews = {
      'correct': {},
      'wrong': {}
    }

    # if there are any duplicates, we only want to most recent review
    processed_ids = set()
    for review in sorted(raw_reviews['data'], key=lambda r: r['data']['created_at'], reverse=True):
      # skip any subjects we've already seen
      if review['data']['subject_id'] in processed_ids:
        continue

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
