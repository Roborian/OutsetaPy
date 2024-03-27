from typing import List, Optional
from datetime import datetime

class Person:
  pass

class CaseHistory:
  pass

class CaseSource:
  pass

class CaseStatus:
  pass

class Case:
  def __init__(
    self,
    SubmittedDateTime: datetime,
    FromPerson: Optional[Person],
    AssignedToPersonClientIdentifier: str,
    Subject: str,
    Body: str,
    UserAgent: Optional[str],
    Status: CaseStatus,
    Source: CaseSource,
    CaseHistories: Optional[List[CaseHistory]],
    IsOnline: bool,
    LastCaseHistory: Optional[CaseHistory],
    Participants: Optional[str],
    RecaptchaToken: Optional[str],
    Uid: str,
    Created: datetime,
    Updated: datetime
  ):
    self.SubmittedDateTime = SubmittedDateTime
    self.FromPerson = FromPerson
    self.AssignedToPersonClientIdentifier = AssignedToPersonClientIdentifier
    self.Subject = Subject
    self.Body = Body
    self.UserAgent = UserAgent
    self.Status = Status
    self.Source = Source
    self.CaseHistories = CaseHistories
    self.IsOnline = IsOnline
    self.LastCaseHistory = LastCaseHistory
    self.Participants = Participants
    self.RecaptchaToken = RecaptchaToken
    self.Uid = Uid
    self.Created = Created
    self.Updated = Updated
