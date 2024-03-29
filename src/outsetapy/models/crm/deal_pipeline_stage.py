from datetime import datetime
import importlib


class DealPipelineStage:
    def __init__(
        self, uid: str, created: datetime, updated: datetime, weight: int, name: str
    ):
        self.Weight = weight
        self.Name = name
        self.Uid = uid
        self.Created = created
        self.Updated = updated

    def get_person(self):
        Person = importlib.import_module("outsetapy.models.crm.person").Person
        return Person

    def get_deal(self):
        Deal = importlib.import_module("outsetapy.models.crm.deal").Deal
        return Deal
