from typing import Optional
from datetime import datetime
from outsetapy.models.crm.activity_type import ActivityType
from outsetapy.models.shared.entity import EntityType


class Activity:
    def __init__(self, data: object):
        self.Title = None
        self.Description = None
        self.ActivityDateTime = None
        self.ActivityType = None
        self.EntityType = None
        self.EntityUid = None
        self.Uid = None
        self.Created = None
        self.Updated = None
        self.ActivityData = None

        # Update the activity attributes based on the provided dictionary
        if "_objectType" in data and data["_objectType"] == "Activity":
            self.Title = data["Title"]
            self.Description = data["Description"]
            self.ActivityDateTime = data["ActivityDateTime"]
            self.ActivityType = data["ActivityType"]
            self.EntityType = data["EntityType"]
            self.EntityUid = data["EntityUid"]
            self.Uid = data["Uid"]
            self.Created = data["Created"]
            self.Updated = data["Updated"]
            self.ActivityData = data.get("ActivityData", None)
        elif "_objectType" in data:
            raise Exception(f"Invalid object type: {data['_objectType']}")
