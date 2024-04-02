import importlib
from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from .billing_renewal_term import BillingRenewalTerm as _BillingRenewalTerm
from outsetapy.util.store import Store


@dataclass
class Subscription:
    Uid: str
    BillingRenewalTerm: _BillingRenewalTerm
    Account_Uid: Optional[str]
    Plan_Uid: Optional[str]
    Quantity: Optional[float]
    StartDate: datetime
    EndDate: Optional[datetime]
    RenewalDate: Optional[datetime]
    NewRequiredQuantity: Optional[float]
    IsPlanUpgradeRequired: bool
    PlanUpgradeRequiredMessage: Optional[str]
    Created: datetime
    Updated: datetime

    def __init__(self, data: object, store: Store):
        self.__store = store
        self.Uid = None
        self.BillingRenewalTerm = None
        self.Account_Uid = None
        self.Plan_Uid = None
        self.Quantity = None
        self.StartDate = None
        self.EndDate = None
        self.RenewalDate = None
        self.NewRequiredQuantity = None
        self.IsPlanUpgradeRequired = None
        self.PlanUpgradeRequiredMessage = None
        self.Created = None
        self.Updated = None
        if "_objectType" in data and data["_objectType"] == "Subscription":
            self.Uid = data["Uid"]
            self.BillingRenewalTerm = data["BillingRenewalTerm"]
            if "Account" in data and data['Account'] is not None and '_objectType' in data["Account"] and data["Account"]["_objectType"] == 'Account':
                self.Account_Uid = data["Account"]['Uid']
            else:
                self.Account_Uid = data["Account"]
            self._plan = data["Plan"]['Uid']
            self.Quantity = data["Quantity"]
            self.StartDate = data["StartDate"]
            self.EndDate = data["EndDate"]
            self.RenewalDate = data["RenewalDate"]
            self.NewRequiredQuantity = data["NewRequiredQuantity"]
            self.IsPlanUpgradeRequired = data["IsPlanUpgradeRequired"]
            self.PlanUpgradeRequiredMessage = data["PlanUpgradeRequiredMessage"]
            self.Created = data["Created"]
            self.Updated = data["Updated"]
        else:
            raise ValueError("Invalid object type")
        
    @property
    async def Plan(self):
        plan_api = importlib.import_module("outsetapy.api.billing.plans").Plans(self.__store)
        return await plan_api.get(self._plan)
