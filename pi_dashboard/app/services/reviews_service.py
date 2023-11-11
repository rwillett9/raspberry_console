import os, requests
import helpers
from base_service import BaseWanikaniService

class ReviewsService(BaseWanikaniService):
  # get a list of reviews for the last 24 hours
  # if an item was reviews multiple times in this time period use the most recent review
  def get_recent_reviews(self, date):
    # NOTE: this endpoint is getting reworked, this may need to be updated
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
    res = {
      'correct': {},
      'wrong': {},
      'stats': {
        'correct': {
          'radicals': 0,
          'kanji': 0,
          'vocabulary': 0
        },
        'totals': {
          'radicals': 0,
          'kanji': 0,
          'vocabulary': 0
        },
        'percentage': 0,
        'total_items': 0
      }
    }

    # if there are any duplicates, we only want to most recent review
    processed_ids = set()
    for review in sorted(raw_reviews['data'], key=lambda r: r['data']['created_at'], reverse=True):
      # skip any subjects we've already seen
      if review['data']['subject_id'] in processed_ids:
        continue
      processed_ids.add(review['data']['subject_id'])

      # get the current stage as a string using helper dict
      curr_stage = srs_num_to_stage[str(review['data']['ending_srs_stage'])]
      # get the current type of item ('radicals', 'kanji', or 'vocabulary')
      curr_type = subject_dict[review['data']['subject_id']]['type']

      # check if this item was correct or wrong in most recent review
      key1 = 'correct'
      if review['data']['ending_srs_stage'] < review['data']['starting_srs_stage']:
        key1 = 'wrong'
      else:
        res['stats']['correct'][curr_type] += 1
      res['stats']['totals'][curr_type] += 1

      # add this item to our organized dict
      if curr_stage not in res[key1]:
        res[key1][curr_stage] = {}
      try:
        res[key1][curr_stage][curr_type].append(review)
      except KeyError:
        res[key1][curr_stage][curr_type] = [review]

    # avoid divide by zero error
    res['stats']['total_items'] = res['stats']['totals']['radicals'] + res['stats']['totals']['kanji'] + res['stats']['totals']['vocabulary']
    if res['stats']['total_items'] != 0:
      num_correct = res['stats']['correct']['radicals'] + res['stats']['correct']['kanji'] + res['stats']['correct']['vocabulary']
      res['stats']['percentage'] = round((num_correct / res['stats']['total_items']) * 100)
    return res
