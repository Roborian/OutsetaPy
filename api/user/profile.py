from typing import Optional
from models.crm.person import Person
from models.wrappers.validation_error import ValidationError
from util.request import Request
from util.store import Store

class Profile:
  def __init__(self, store: Store):
    self.store = store

  async def get(self, fields: Optional[str] = None) -> Person:
    request = Request(self.store, 'profile').authenticate_as_user()
    if fields:
      request.with_params({'fields': fields})

    response = await request.get()

    if not response.ok:
      raise response
    return await response.json() as Person

  async def update(self, profile: ProfileUpdate) -> Union[Person, ValidationError[Person]]:
    request = Request(self.store, 'profile') \
      .authenticate_as_user() \
      .with_body(profile)
    response = await request.put()

    if response.status == 400:
      return await response.json() as ValidationError[Person]
    elif response.ok:
      return await response.json() as Person
    else:
      raise response

class ProfileUpdate(dict):
  def __init__(self, uid: str, **kwargs):
    super().__init__(**kwargs)
    self['Uid'] = uid
