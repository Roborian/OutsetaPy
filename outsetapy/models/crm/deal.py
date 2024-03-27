from typing import Optional, List
from datetime import date
from outsetapy.models.crm.account import Account
from outsetapy.models.crm.deal_person import DealPerson
from .deal_pipeline_stage import DealPipelineStage
from .person import Person

class Deal:
  def __init__(
    self,
    Name: str,
    Amount: float,
    DueDate: date,
    AssignedToPersonClientIdentifier: str,
    Weight: float,
    Contacts: str,
    Uid: str,
    Created: date,
    Updated: date,
    DealPipelineStage: Optional[DealPipelineStage] = None,
    Account: Optional[Account] = None,
    DealPeople: Optional[List[DealPerson]] = None,
    Owner: Optional[Person] = None,
  ):
    self.Name = Name
    self.Amount = Amount
    self.DueDate = DueDate
    self.AssignedToPersonClientIdentifier = AssignedToPersonClientIdentifier
    self.Weight = Weight
    self.DealPipelineStage = DealPipelineStage
    self.Account = Account
    self.DealPeople = DealPeople
    self.Contacts = Contacts
    self.Owner = Owner
    self.Uid = Uid
    self.Created = Created
    self.Updated = Updated
