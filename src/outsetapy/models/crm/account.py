from datetime import datetime
import importlib
from outsetapy.util.store import Store
from outsetapy.models.shared.address import Address
# from .deal import Deal

class Account:
    def __init__(self, data: object, store: Store):
        self.__store = store
        self.Name = None
        self.ClientIdentifier = None
        self.IsDemo = False
        self.BillingAddress = Address("", "", "", "")
        self.MailingAddress = Address("", "", "", "")
        self.AccountStage = None
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
            if "CurrentSubscription" in data and data["CurrentSubscription"] and "Uid" in data["CurrentSubscription"]:
                self._current_subscription = data["CurrentSubscription"]['Uid']
            else:
                self._current_subscription = None
            self.PrimaryContact = data["PrimaryContact"]
            self.PrimarySubscription = data["PrimarySubscription"]
            self.RecaptchaToken = data["RecaptchaToken"]
            self.LifetimeRevenue = data["LifetimeRevenue"]
            self.Uid = data["Uid"]
            self.Created = data["Created"]
            self.Updated = data["Updated"]
        elif "_objectType" in data:
            raise Exception(f"Invalid object type: {data['_objectType']}")

    @property
    async def CurrentSubscription(self):
        subscription_api = importlib.import_module("outsetapy.api.billing.subscriptions").Subscriptions(self.__store)
        CurrentSubscription = await subscription_api.get(self._current_subscription)
        return CurrentSubscription
