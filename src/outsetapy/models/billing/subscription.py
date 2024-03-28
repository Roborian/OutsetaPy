from typing import Optional
from datetime import datetime
import importlib

class Subscription:
  def __init__(self, plan, billing_renewal_term, account, subscription_add_ons=None, quantity=None, start_date=None, end_date=None, renewal_date=None, new_required_quantity=None, is_plan_upgrade_required=None, plan_upgrade_required_message=None, discount_coupon_subscriptions=None, created=None, updated=None):
    self.Plan = plan
    self.BillingRenewalTerm = billing_renewal_term
    self.Account = account
    self.SubscriptionAddOns = subscription_add_ons
    self.Quantity = quantity
    self.StartDate = start_date
    self.EndDate = end_date
    self.RenewalDate = renewal_date
    self.NewRequiredQuantity = new_required_quantity
    self.IsPlanUpgradeRequired = is_plan_upgrade_required
    self.PlanUpgradeRequiredMessage = plan_upgrade_required_message
    self.DiscountCouponSubscriptions = discount_coupon_subscriptions
    self.Created = created
    self.Updated = updated
