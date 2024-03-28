from typing import List
from datetime import datetime

class EmailListPerson:
  # Define the EmailListPerson class here
  pass

class EmailList:
  def __init__(self):
    self.Name: str
    self.WelcomeSubject: str
    self.WelcomeBody: str
    self.WelcomeFromName: str
    self.WelcomeFromEmail: str
    self.EmailListPerson: List[EmailListPerson]
    self.CountSubscriptionsActive: int
    self.CountSubscriptionsBounce: int
    self.CountSubscriptionsSpam: int
    self.CountSubscriptionsUnsubscribed: int
    self.Uid: str
    self.Created: datetime
    self.Updated: datetime
