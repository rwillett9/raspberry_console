from base_service import BaseWanikaniService

class LevelsService(BaseWanikaniService):
  # get data on all levels for this user
  def get_all_levels(self):
    levels = self.do_get_request(url='https://api.wanikani.com/v2/level_progressions')
    return levels.json()
