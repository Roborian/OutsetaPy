from typing import Optional
from datetime import datetime

class Address:
  def __init__(
    self,
    City: str,
    State: str,
    PostalCode: str,
    AddressLine1: Optional[str] = None,
    AddressLine2: Optional[str] = None,
    AddressLine3: Optional[str] = None,
    Country: Optional[str] = None,
    Uid: Optional[str] = None,
    Created: Optional[datetime] = None,
    Updated: Optional[datetime] = None
  ):
    self.AddressLine1 = AddressLine1
    self.AddressLine2 = AddressLine2
    self.AddressLine3 = AddressLine3
    self.City = City
    self.State = State
    self.PostalCode = PostalCode
    self.Country = Country
    self.Uid = Uid
    self.Created = Created
    self.Updated = Updated
