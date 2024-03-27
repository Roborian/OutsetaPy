from typing import Optional
from datetime import datetime
from outsetapy.models.crm.activity_type import ActivityType
from outsetapy.models.shared.entity import EntityType

class Activity:
  def __init__(
    self,
    Title: str,
    Description: str,
    ActivityDateTime: datetime,
    ActivityType: ActivityType,
    EntityType: EntityType,
    EntityUid: str,
    Uid: str,
    Created: datetime,
    Updated: datetime,
    ActivityData: Optional[str] = None
  ):
    self.Title = Title
    self.Description = Description
    self.ActivityData = ActivityData
    self.ActivityDateTime = ActivityDateTime
    self.ActivityType = ActivityType
    self.EntityType = EntityType
    self.EntityUid = EntityUid
    self.Uid = Uid
    self.Created = Created
    self.Updated = Updated
