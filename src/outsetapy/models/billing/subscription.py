from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from .billing_renewal_term import BillingRenewalTerm as _BillingRenewalTerm


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

    def __init(self, data: object):
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
            self.Account_Uid = data["Account.Uid"]
            self.Plan_Uid = data["Plan.Uid"]
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
