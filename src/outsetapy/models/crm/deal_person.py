from typing import Optional
from datetime import datetime
import importlib


class DealPerson:
    def __init__(
        self,
        uid: str,
        created: datetime,
        updated: datetime,
        person: Optional[str] = None,
        deal: Optional[str] = None,
    ):
        self.Person = person
        self.Deal = deal
        self.Uid = uid
        self.Created = created
        self.Updated = updated

    def get_person(self):
        if self.Person is not None:
            Person = importlib.import_module("outsetapy.models.crm.person").Person
            return Person

    def get_deal(self):
        if self.Deal is not None:
            Deal = importlib.import_module("outsetapy.models.crm.deal").Deal
            return Deal
