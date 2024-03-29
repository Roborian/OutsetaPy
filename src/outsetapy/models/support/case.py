from typing import List, Optional
from datetime import datetime
from dataclasses import dataclass
from outsetapy.models.support.case_history import CaseHistory
from outsetapy.models.support.case_source import CaseSource
from outsetapy.models.support.case_status import CaseStatus
from outsetapy.models.crm.person import Person


@dataclass
class Case:
    SubmittedDateTime: Optional[datetime]
    FromPerson: Optional[Person]
    AssignedToPersonClientIdentifier: Optional[str]
    Subject: Optional[str]
    Body: Optional[str]
    UserAgent: Optional[str]
    Status: Optional[CaseStatus]
    Source: Optional[CaseSource]
    CaseHistories: Optional[List[CaseHistory]]
    IsOnline: Optional[bool]
    LastCaseHistory: Optional[CaseHistory]
    Participants: Optional[List[Person]]
    RecaptchaToken: Optional[str]
    Uid: Optional[str]
    Created: Optional[datetime]
    Updated: Optional[datetime]

    def __init__(self, data: object):
        self.SubmittedDateTime = None
        self.FromPerson = None
        self.AssignedToPersonClientIdentifier = None
        self.Subject = None
        self.Body = None
        self.UserAgent = None
        self.Status = None
        self.Source = None
        self.CaseHistories = None
        self.IsOnline = None
        self.LastCaseHistory = None
        self.Participants = None
        self.RecaptchaToken = None
        self.Uid = None
        self.Created = None
        self.Updated = None

        # Update the case attributes based on the provided dictionary
        if "_objectType" in data and data["_objectType"] == "Case":
            self.SubmittedDateTime = data["SubmittedDateTime"]
            self.FromPerson = data["FromPerson"]
            self.AssignedToPersonClientIdentifier = data[
                "AssignedToPersonClientIdentifier"
            ]
            self.Subject = data["Subject"]
            self.Body = data["Body"]
            self.UserAgent = data["UserAgent"]
            self.Status = data["Status"]
            self.Source = data["Source"]
            self.CaseHistories = data["CaseHistories"]
            self.IsOnline = data["IsOnline"]
            self.LastCaseHistory = data["LastCaseHistory"]
            self.Participants = data["Participants"]
            self.RecaptchaToken = data["RecaptchaToken"]
            self.Uid = data["Uid"]
            self.Created = data["Created"]
            self.Updated = data["Updated"]
        elif "_objectType" in data:
            raise Exception(f"Invalid object type: {data['_objectType']}")
