import importlib
from typing import Optional
from datetime import datetime

class CaseHistory:
  def __init__(
    self,
    HistoryDateTime: datetime,
    AgentName: str,
    Comment: str,
    Type: int,
    Uid: str,
    Created: datetime,
    Updated: datetime,
    SeenDateTime: Optional[datetime] = None,
    ClickDateTime: Optional[datetime] = None,
    PersonEmail: Optional[str] = None,
    NewUvi: Optional[str] = None,
  ):
    self.HistoryDateTime = HistoryDateTime
    self.AgentName = AgentName
    self.Comment = Comment
    self.Type = Type
    self.SeenDateTime = SeenDateTime
    self.ClickDateTime = ClickDateTime
    self.PersonEmail = PersonEmail
    self.NewUvi = NewUvi
    self.Uid = Uid
    self.Created = Created
    self.Updated = Updated

    def get_case(self):
      #todo: check if this is correcy
      Case = importlib.import_module('outsetapy.models.support.case').Case
      return Case(self.caseId)
