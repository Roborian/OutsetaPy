from outsetapy.models.crm.person import Person
from outsetapy.models.marketing.emaillist import EmailList
from outsetapy.models.marketing.emaillist import EmailListPerson
from outsetapy.models.wrappers.list import List
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.util.store import Store

class EmailListSubscriptions:
  DEFAULT_FIELDS = [
    '*'
  ]

  def __init__(self, store: Store):
    self.store = store

  async def get_all(self, list_uid: str, options: dict = {}) -> List[EmailListPerson]:
    has_more = True
    results = []
    while has_more:
      request = Request(self.store, f'email/lists/{list_uid}/subscriptions') \
        .with_params({'fields': options.get('fields', ','.join(EmailListSubscriptions.DEFAULT_FIELDS))}) \
        .with_params({'orderBy': 'SubscribedDate'}) \
        .authenticate_as_server()
      if 'limit' in options:
        request.with_params({'limit': str(options['limit'])})
      if 'offset' in options:
        request.with_params({'offset': str(options['offset'])})

      response = request.get()

      if not response.ok:
        raise response
      
      json_response = response.json()
      results += json_response
      has_more = hasMoreResults(json_response)
      options['offset'] = json_response['metadata']['offset'] + json_response['metadata']['limit']

    return [EmailListPerson(json_obj) for json_obj in results]

  async def add(self, subscription: dict, options: dict = {}) -> None:
    request = Request(self.store, f'email/lists/{subscription["EmailList"]["Uid"]}/subscriptions') \
      .with_params({'fields': options.get('fields', ','.join(EmailListSubscriptions.DEFAULT_FIELDS))}) \
      .authenticate_as_server() \
      .with_body(subscription)
    response = await request.post()

    if response.status == 400:
      raise ValidationError(response.json())
    elif response.ok:
      return None
    else:
      raise response

  async def delete(self, subscription: dict) -> None:
    request = Request(
      self.store,
      f'email/lists/{subscription["EmailList"]["Uid"]}/subscriptions/{subscription["Person"]["Uid"]}'
    ).authenticate_as_server()
    response = await request.delete()

    if not response.ok:
      raise response
    return None

class SubscriptionAdd(EmailListPerson):
  EmailList: EmailList
  Person: Person

class SubscriptionDelete(EmailListPerson):
  EmailList: EmailList
  Person: Person
