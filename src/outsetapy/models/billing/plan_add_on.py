from datetime import datetime


class PlanAddOn:
    def __init__(
        self, IsUserSelectable: bool, Uid: str, Created: datetime, Updated: datetime
    ):
        self.IsUserSelectable = IsUserSelectable
        self.Uid = Uid
        self.Created = Created
        self.Updated = Updated
