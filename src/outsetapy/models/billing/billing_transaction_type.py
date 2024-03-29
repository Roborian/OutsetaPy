from enum import Enum


class BillingTransactionType(Enum):
    Invoice = 1
    Payment = 2
    Credit = 3
    Refund = 4
    Chargeback = 5
