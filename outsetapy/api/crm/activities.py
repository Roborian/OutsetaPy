from typing import Union
from outsetapy.models.shared.entity import EntityType
from outsetapy.models.crm.activity import Activity
from outsetapy.models.crm.activity_type import ActivityType
from outsetapy.models.wrappers.list import List
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.util.store import Store

class Activities:
  DEFAULT_FIELDS = '*'

  def __init__(self, store: Store):
    self.store = store

  async def get_all(self, options: dict = {}) -> List[Activity]:
    has_more = True
    results = []
    while has_more:
      request = Request(self.store, 'activities') \
        .with_params({'fields': options.get('fields', Activities.DEFAULT_FIELDS)}) \
        .authenticate_as_server()

      if 'limit' in options:
        request.with_params({'limit': str(options['limit'])})
      if 'offset' in options:
        request.with_params({'offset': str(options['offset'])})
      if 'ActivityType' in options:
        request.with_params({'ActivityType': str(options['ActivityType'])})
      if 'EntityType' in options:
        request.with_params({'EntityType': str(options['EntityType'])})
      if 'EntityUid' in options:
        request.with_params({'EntityUid': str(options['EntityUid'])})

      response = await request.get()

      if response.ok:
        json_response = await response.json()
        results += json_response['items']
        has_more = hasMoreResults(json_response)
        options['offset'] = json_response['metadata']['offset'] + json_response['metadata']['limit']
      else:
        raise response

    return [Activity(json_obj) for json_obj in results]

  async def add(self, activity: dict, options: dict = {}) -> Union[Activity, ValidationError[None]]:
    request = Request(self.store, 'activities/customactivity') \
      .authenticate_as_server() \
      .with_params({'fields': options.get('fields', Activities.DEFAULT_FIELDS)}) \
      .with_body(activity)
    response = await request.post()

    if response.status == 400:
      raise Exception(await response.json())
    elif response.ok:
      json_response = await response.json()
      return Activity(json_response)
    else:
      raise response

class ActivityAdd:
  pass
#todo! check this line