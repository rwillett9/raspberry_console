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
      'apprentice': {
        'radicals': [raw_review_struct1, ...],
        'kanji': [raw_review_struct1, ...],
        'vocabulary: [raw_review_struct1, ...]
      },
      'burned': {...}
      'enlightened: {...}
    },
    'wrong': {
      'apprentice': {...},
      ...
    }
  }
  '''
  def process_reviews(raw_reviews, subject_dict):
    # declare useful vars
    srs_num_to_stage = helpers.SRS_STAGES_DICT
    processed_reviews = {
      'correct': {},
      'wrong': {},
      'percentage': 0
    }

    # if there are any duplicates, we only want to most recent review
    num_correct = 0
    num_total = 0
    processed_ids = set()
    for review in sorted(raw_reviews['data'], key=lambda r: r['data']['created_at'], reverse=True):
      # skip any subjects we've already seen
      if review['data']['subject_id'] in processed_ids:
        continue
      processed_ids.add(review['data']['subject_id'])

      # check if this item was correct or wrong in most recent review
      num_total += 1
      key1 = 'correct'
      if review['data']['ending_srs_stage'] < review['data']['starting_srs_stage']:
        key1 = 'wrong'
      else:
        num_correct += 1

      # get the current stage as a string using helper dict
      current_stage = srs_num_to_stage[str(review['data']['ending_srs_stage'])]

      # add this item to our organized dict
      curr_type = subject_dict[review['data']['subject_id']]['type']
      if current_stage not in processed_reviews[key1]:
        processed_reviews[key1][current_stage] = {}
      try:
        processed_reviews[key1][current_stage][curr_type].append(review)
      except KeyError:
        processed_reviews[key1][current_stage][curr_type] = [review]

    processed_reviews['percentage'] = round((num_correct / num_total) * 100)
    return processed_reviews
