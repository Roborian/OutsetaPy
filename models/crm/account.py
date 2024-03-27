from typing import List
from datetime import datetime
from shared import Address


class Deal:
  def __init__(self, deal_id: str, deal_name: str):
    self.deal_id = deal_id
    self.deal_name = deal_name

class PersonAccount:
  def __init__(self, person_id: str, person_name: str):
    self.person_id = person_id
    self.person_name = person_name

class AccountStage:
  def __init__(self, stage_id: str, stage_name: str):
    self.stage_id = stage_id
    self.stage_name = stage_name

class Subscription:
  def __init__(self, subscription_id: str, subscription_name: str):
    self.subscription_id = subscription_id
    self.subscription_name = subscription_name

class Account:
  def __init__(self):
    self.Name = ""
    self.ClientIdentifier = None
    self.IsDemo = False
    self.BillingAddress = Address("", "", "", "")
    self.MailingAddress = Address("", "", "", "")
    self.AccountStage = AccountStage("", "")
    self.PaymentInformation = None
    self.PersonAccount = []
    self.Subscriptions = []
    self.Deals = []
    self.LastLoginDateTime = None
    self.AccountSpecificPageUrl1 = ""
    self.AccountSpecificPageUrl2 = ""
    self.AccountSpecificPageUrl3 = ""
    self.AccountSpecificPageUrl4 = ""
    self.AccountSpecificPageUrl5 = ""
    self.RewardFulReferralId = None
    self.HasLoggedIn = False
    self.AccountStageLabel = ""
    self.DomainName = None
    self.LatestSubscription = None
    self.CurrentSubscription = None
    self.PrimaryContact = None
    self.PrimarySubscription = None
    self.RecaptchaToken = None
    self.LifetimeRevenue = 0
    self.Uid = ""
    self.Created = datetime.now()
    self.Updated = datetime.now()
