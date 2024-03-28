from typing import Optional
from datetime import date
from .invoice import Invoice
from .subscription_add_on import SubscriptionAddOn

class UsageItem:
  def __init__(self, UsageDate: date, SubscriptionAddOn: SubscriptionAddOn, Amount: float, Uid: str, Created: date, Updated: date, Invoice: Optional[Invoice] = None):
    self.UsageDate = UsageDate
    self.SubscriptionAddOn = SubscriptionAddOn
    self.Amount = Amount
    self.Uid = Uid
    self.Created = Created
    self.Updated = Updated
    self.Invoice = Invoice
