from typing import List
from .billing_add_on_type import BillingAddOnType
from .plan_add_on import PlanAddOn
from datetime import date

class AddOn:
  def __init__(self, Name: str, BillingAddOnType: BillingAddOnType, IsQuantityEditable: bool, MinimumQuantity: int, MonthlyRate: int, AnnualRate: int, SetupFee: int, UnitOfMeasure: str, IsTaxable: bool, IsBilledDuringTrial: bool, PlanAddOns: List[PlanAddOn], Uid: str, Created: date, Updated: date):
    self.Name = Name
    self.BillingAddOnType = BillingAddOnType
    self.IsQuantityEditable = IsQuantityEditable
    self.MinimumQuantity = MinimumQuantity
    self.MonthlyRate = MonthlyRate
    self.AnnualRate = AnnualRate
    self.SetupFee = SetupFee
    self.UnitOfMeasure = UnitOfMeasure
    self.IsTaxable = IsTaxable
    self.IsBilledDuringTrial = IsBilledDuringTrial
    self.PlanAddOns = PlanAddOns
    self.Uid = Uid
    self.Created = Created
    self.Updated = Updated
