from enum import Enum


class BillingRenewalTerm(Enum):
    Monthly = 1
    Annually = 2
    Quarterly = 3
    OneTime = 4
