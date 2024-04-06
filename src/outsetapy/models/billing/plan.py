from typing import List
from dataclasses import dataclass
from datetime import date
from .plan_family import PlanFamily as _PlanFamily
from .plan_add_on import PlanAddOn


@dataclass
class Plan:
    Name: str
    Description: str
    PlanFamily: _PlanFamily
    IsQuantityEditable: bool
    MinimumQuantity: int
    MaximumPeople: int
    MonthlyRate: float
    AnnualRate: float
    QuarterlyRate: float
    OneTimeRate: float
    SetupFee: float
    IsTaxable: bool
    IsActive: bool
    IsPerUser: bool
    RequirePaymentInformation: bool
    TrialPeriodDays: int
    TrialUntilDate: date
    UnitOfMeasure: str
    PlanAddOns: List[PlanAddOn]
    NumberOfSubscriptions: int
    Uid: str
    AccountRegistrationMode: str
    ActivityEventData: object
    ExpiresAfterMonths: int
    ExpirationDate: date
    PostLoginPath: str
    StripeTaxCodeId: str
    Created: date
    Updated: date

    def __init__(self, data: object):
        self.Name = None
        self.Description = None
        self.PlanFamily = None
        self.IsQuantityEditable = None
        self.MinimumQuantity = None
        self.MaximumPeople = None
        self.MonthlyRate = None
        self.AnnualRate = None
        self.QuarterlyRate = None
        self.OneTimeRate = None
        self.SetupFee = None
        self.IsTaxable = None
        self.IsActive = None
        self.IsPerUser = None
        self.RequirePaymentInformation = None
        self.TrialPeriodDays = None
        self.TrialUntilDate = None
        self.UnitOfMeasure = None
        self.PlanAddOns = None
        self.NumberOfSubscriptions = None
        self.Uid = None
        self.AccountRegistrationMode = None
        self.ActivityEventData = None
        self.ExpiresAfterMonths = None
        self.ExpirationDate = None
        self.PostLoginPath = None
        self.StripeTaxCodeId = None
        self.UnitOfMeasure = None
        self.Created = None
        self.Updated = None

        # Update the plan attributes based on the provided dictionary
        if "_objectType" in data and data["_objectType"] == "Plan":
            self.Name = data.get("Name")
            self.Description = data.get("Description")
            self.PlanFamily = data.get("PlanFamily")
            self.IsQuantityEditable = data.get("IsQuantityEditable")
            self.MinimumQuantity = data.get("MinimumQuantity")
            self.MaximumPeople = data.get("MaximumPeople")
            self.MonthlyRate = data.get("MonthlyRate")
            self.AnnualRate = data.get("AnnualRate")
            self.QuarterlyRate = data.get("QuarterlyRate")
            self.OneTimeRate = data.get("OneTimeRate")
            self.SetupFee = data.get("SetupFee")
            self.IsTaxable = data.get("IsTaxable")
            self.IsActive = data.get("IsActive")
            self.IsPerUser = data.get("IsPerUser")
            self.RequirePaymentInformation = data.get("RequirePaymentInformation")
            self.TrialPeriodDays = data.get("TrialPeriodDays")
            self.TrialUntilDate = data.get("TrialUntilDate")
            self.UnitOfMeasure = data.get("UnitOfMeasure")
            self.PlanAddOns = data.get("PlanAddOns")
            self.NumberOfSubscriptions = data.get("NumberOfSubscriptions")
            self.Uid = data.get("Uid")
            self.AccountRegistrationMode = data.get("AccountRegistrationMode")
            self.ActivityEventData = data.get("ActivityEventData")
            self.ExpiresAfterMonths = data.get("ExpiresAfterMonths")
            self.ExpirationDate = data.get("ExpirationDate")
            self.PostLoginPath = data.get("PostLoginPath")
            self.StripeTaxCodeId = data.get("StripeTaxCodeId")
            self.UnitOfMeasure = data.get("UnitOfMeasure")
            self.Created = data.get("Created")
            self.Updated = data.get("Updated")
        elif "_objectType" in data:
            raise Exception(f"Invalid object type: {data['_objectType']}")
