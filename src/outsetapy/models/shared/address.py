from typing import Optional
from datetime import datetime


class Address:
    def __init__(self, data: dict = {}):
        self.AddressLine1 = data.get("AddressLine1")
        self.AddressLine2 = data.get("AddressLine2")
        self.AddressLine3 = data.get("AddressLine3")
        self.City = data.get("City")
        self.State = data.get("State")
        self.PostalCode = data.get("PostalCode")
        self.Country = data.get("Country")
        self.Uid = data.get("Uid")
        self.Created = data.get("Created")
        self.Updated = data.get("Updated")
