from enum import Enum

class AccountStage(Enum):
  Trialing = 2
  Subscribing = 3
  Cancelling = 4
  Expired = 5
  TrialExpired = 6
  PastDue = 7
