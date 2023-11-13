from base_service import BaseWanikaniService


class AssignmentsService(BaseWanikaniService):
  # get assignments that are currently available as of the current time
  def get_available_assignments(self, date):
    query_parameters = [
      'available_before=%s' % date
    ]
    request_url = '?' + '&'.join(query_parameters)

    # deal with possible pagination of results and collect assignment objects
    assignments = []
    get_more = True
    while get_more:
      response = self.do_get_request(url='https://api.wanikani.com/v2/assignments' + request_url).json()
      assignments.extend(response['data'])

      if response['pages']['next_url'] is not None:
        request_url = response['pages']['next_url']
      else:
        get_more = False

    # return the list of assignments objects
    return assignments
