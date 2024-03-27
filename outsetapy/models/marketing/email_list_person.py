from typing import Optional
from datetime import datetime
from outsetapy.models.marketing.emaillist import EmailList
from ..crm.person import Person

class EmailListPerson:
  def __init__(
    self,
    EmailList: EmailList,
    Person: Person,
    EmailListSubscriberStatus: int,
    SubscribedDate: datetime,
    Uid: str,
    Created: datetime,
    Updated: datetime,
    ConfirmedDate: Optional[datetime] = None,
    UnsubscribedDate: Optional[datetime] = None,
    CleanedDate: Optional[datetime] = None,
    WelcomeEmailDeliverDateTime: Optional[datetime] = None,
    WelcomeEmailOpenDateTime: Optional[datetime] = None,
    UnsubscribeReason: Optional[str] = None,
    UnsubscribeReasonOther: Optional[str] = None,
    RecaptchaToken: Optional[str] = None,
    RecaptchaSiteKey: Optional[str] = None,
    SendWelcomeEmail: bool = False,
    Source: Optional[str] = None,
  ):
    self.EmailList = EmailList
    self.Person = Person
    self.EmailListSubscriberStatus = EmailListSubscriberStatus
    self.SubscribedDate = SubscribedDate
    self.ConfirmedDate = ConfirmedDate
    self.UnsubscribedDate = UnsubscribedDate
    self.CleanedDate = CleanedDate
    self.WelcomeEmailDeliverDateTime = WelcomeEmailDeliverDateTime
    self.WelcomeEmailOpenDateTime = WelcomeEmailOpenDateTime
    self.UnsubscribeReason = UnsubscribeReason
    self.UnsubscribeReasonOther = UnsubscribeReasonOther
    self.RecaptchaToken = RecaptchaToken
    self.RecaptchaSiteKey = RecaptchaSiteKey
    self.SendWelcomeEmail = SendWelcomeEmail
    self.Source = Source
    self.Uid = Uid
    self.Created = Created
    self.Updated = Updated
