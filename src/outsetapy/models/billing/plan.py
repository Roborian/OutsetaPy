from typing import List
from dataclasses import dataclass
from datetime import date
from .plan_family import PlanFamily
from .plan_add_on import PlanAddOn


@dataclass
class Plan:
    Name: str
    Description: str
    PlanFamily: PlanFamily
    IsQuantityEditable: bool
    MinimumQuantity: int
    MonthlyRate: int
    AnnualRate: int
    SetupFee: int
    IsTaxable: bool
    IsActive: bool
    TrialPeriodDays: int
    UnitOfMeasure: str
    PlanAddOns: List[PlanAddOn]
    NumberOfSubscriptions: int
    Uid: str
    Created: date
    Updated: date

    def __init__(self, data: object):
        self.Name = None
        self.Description = None
        self.PlanFamily = None
        self.IsQuantityEditable = None
        self.MinimumQuantity = None
        self.MonthlyRate = None
        self.AnnualRate = None
        self.SetupFee = None
        self.IsTaxable = None
        self.IsActive = None
        self.TrialPeriodDays = None
        self.UnitOfMeasure = None
        self.PlanAddOns = None
        self.NumberOfSubscriptions = None
        self.Uid = None
        self.Created = None
        self.Updated = None

        # Update the plan attributes based on the provided dictionary
        if "_objectType" in data and data["_objectType"] == "Plan":
            self.Name = data["Name"]
            self.Description = data["Description"]
            self.PlanFamily = data["PlanFamily"]
            self.IsQuantityEditable = data["IsQuantityEditable"]
            self.MinimumQuantity = data["MinimumQuantity"]
            self.MonthlyRate = data["MonthlyRate"]
            self.AnnualRate = data["AnnualRate"]
            self.SetupFee = data["SetupFee"]
            self.IsTaxable = data["IsTaxable"]
            self.IsActive = data["IsActive"]
            self.TrialPeriodDays = data["TrialPeriodDays"]
            self.UnitOfMeasure = data["UnitOfMeasure"]
            self.PlanAddOns = data["PlanAddOns"]
            self.NumberOfSubscriptions = data["NumberOfSubscriptions"]
            self.Uid = data["Uid"]
            self.Created = data["Created"]
            self.Updated = data["Updated"]
        elif "_objectType" in data:
            raise Exception(f"Invalid object type: {data['_objectType']}")
