# CORRECT
from outsetapy.models.shared.address import Address
from outsetapy.models.crm.account import Account
import importlib

class Person:
    def __init__(self, data: dict, store=None):
        self.__store = store
        self._account = None
        self.Email = ""
        self.FirstName = ""
        self.LastName = ""
        self.ProfileImageS3Url = ""
        self.MailingAddress = Address()
        self.PasswordMustChange = False
        self.PhoneMobile = ""
        self.PhoneWork = ""
        self.Title = ""
        self.Timezone = None
        self.Language = ""
        self.IPAddress = ""
        self.Referer = ""
        self.UserAgent = ""
        self.LastLoginDateTime = None
        self.OAuthGoogleProfileId = None
        self.PersonAccount = []
        self.DealPeople = []
        self.FullName = ""
        self.OAuthIntegrationStatus = 0
        self.UserAgentPlatformBrowser = ""
        self.Uid = ""
        self.Created = None
        self.Updated = None

        if "_objectType" in data and data["_objectType"] == "Person":
            self.Email = data["Email"]
            self.FirstName = data["FirstName"]
            self.LastName = data["LastName"]
            self.ProfileImageS3Url = data["ProfileImageS3Url"]
            self.MailingAddress = data["MailingAddress"]
            self.PasswordMustChange = data["PasswordMustChange"]
            self.PhoneMobile = data["PhoneMobile"]
            self.PhoneWork = data["PhoneWork"]
            self.Title = data["Title"]
            self.Timezone = data["Timezone"]
            self.Language = data["Language"]
            self.IPAddress = data["IPAddress"]
            self.Referer = data["Referer"]
            self.UserAgent = data["UserAgent"]
            self.LastLoginDateTime = data["LastLoginDateTime"]
            self.OAuthGoogleProfileId = data["OAuthGoogleProfileId"]
            self.PersonAccount = data["PersonAccount"]
            self.DealPeople = data["DealPeople"]
            if "Account" in data and data['Account'] is not None and 'Uid' in data["Account"]:
                self._account = data["Account"]['Uid']
            self.FullName = data["FullName"]
            self.OAuthIntegrationStatus = data["OAuthIntegrationStatus"]
            self.UserAgentPlatformBrowser = data["UserAgentPlatformBrowser"]
            self.Uid = data["Uid"]
            self.Created = data["Created"]
            self.Updated = data["Updated"]

    @property
    async def Account(self) -> Account:
        account_api = importlib.import_module("outsetapy.api.crm.accounts").Accounts(self.__store)
        return await account_api.get(self._account)