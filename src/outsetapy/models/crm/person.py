from outsetapy.models.shared.address import Address
from outsetapy.models.crm.account import Account
from outsetapy.models.crm.deal_person import DealPerson
from outsetapy.models.crm.person_account import PersonAccount


class Person:
    def __init__(self):
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
        self.Account = Account()
        self.FullName = ""
        self.OAuthIntegrationStatus = 0
        self.UserAgentPlatformBrowser = ""
        self.Uid = ""
        self.Created = None
        self.Updated = None
