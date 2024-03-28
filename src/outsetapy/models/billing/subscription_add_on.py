from typing import Optional
from datetime import date
from .add_on import AddOn
from .subscription import Subscription

class SubscriptionAddOn:
  def __init__(
    self,
    BillingRenewalTerm: int,
    Subscription: Optional[Subscription],
    AddOn: Optional[AddOn],
    Quantity: Optional[any],
    StartDate: date,
    EndDate: date,
    RenewalDate: Optional[date],
    NewRequiredQuantity: Optional[any],
    Uid: str,
    Created: date,
    Updated: date
  ):
    self.BillingRenewalTerm = BillingRenewalTerm
    self.Subscription = Subscription
    self.AddOn = AddOn
    self.Quantity = Quantity
    self.StartDate = StartDate
    self.EndDate = EndDate
    self.RenewalDate = RenewalDate
    self.NewRequiredQuantity = NewRequiredQuantity
    self.Uid = Uid
    self.Created = Created
    self.Updated = Updated
