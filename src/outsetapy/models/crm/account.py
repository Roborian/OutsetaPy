from typing import List
from datetime import datetime
from outsetapy.models.shared.address import Address


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
    def __init__(self, data: object):
        self.Name = None
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

        # Update the account attributes based on the provided dictionary
        if "_objectType" in data and data["_objectType"] == "Account":
            self.Name = data["Name"]
            self.ClientIdentifier = data["ClientIdentifier"]
            self.IsDemo = data["IsDemo"]
            self.BillingAddress = data["BillingAddress"]
            self.MailingAddress = data["MailingAddress"]
            self.AccountStage = data["AccountStage"]
            self.PaymentInformation = data["PaymentInformation"]
            self.PersonAccount = data["PersonAccount"]
            self.Subscriptions = data["Subscriptions"]
            self.Deals = data["Deals"]
            self.LastLoginDateTime = data["LastLoginDateTime"]
            self.AccountSpecificPageUrl1 = data["AccountSpecificPageUrl1"]
            self.AccountSpecificPageUrl2 = data["AccountSpecificPageUrl2"]
            self.AccountSpecificPageUrl3 = data["AccountSpecificPageUrl3"]
            self.AccountSpecificPageUrl4 = data["AccountSpecificPageUrl4"]
            self.AccountSpecificPageUrl5 = data["AccountSpecificPageUrl5"]
            self.RewardFulReferralId = data["RewardFulReferralId"]
            self.HasLoggedIn = data["HasLoggedIn"]
            self.AccountStageLabel = data["AccountStageLabel"]
            self.DomainName = data["DomainName"]
            self.LatestSubscription = data["LatestSubscription"]
            self.CurrentSubscription = data["CurrentSubscription"]
            self.PrimaryContact = data["PrimaryContact"]
            self.PrimarySubscription = data["PrimarySubscription"]
            self.RecaptchaToken = data["RecaptchaToken"]
            self.LifetimeRevenue = data["LifetimeRevenue"]
            self.Uid = data["Uid"]
            self.Created = data["Created"]
            self.Updated = data["Updated"]
        elif "_objectType" in data:
            raise Exception(f"Invalid object type: {data['_objectType']}")
