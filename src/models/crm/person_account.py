import importlib
from typing import Optional
from datetime import datetime

class PersonAccount:
  def __init__(self, person_id: str, account_id: str):
    self.IsPrimary: bool = False
    self.Uid: Optional[str] = None
    self.Created: Optional[datetime] = None
    self.Updated: Optional[datetime] = None

    def get_person(self):
      Person = importlib.import_module('outsetapy.models.crm.person').Person
      return Person
    def get_account(self):
      Account = importlib.import_module('outsetapy.models.crm.account').Account
      return Account
