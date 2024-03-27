from datetime import datetime
from typing import Optional
from outsetapy.models.crm.account import Account
from outsetapy.models.billing.billing_transaction_type import BillingTransactionType
from outsetapy.models.billing.invoice import Invoice

class Transaction:
  def __init__(
    self,
    transaction_date: datetime,
    billing_transaction_type: BillingTransactionType,
    account: Account,
    invoice: Invoice,
    amount: float,
    is_electronic_transaction: bool,
    uid: str,
    created: datetime,
    updated: datetime,
  ):
    self.TransactionDate = transaction_date
    self.BillingTransactionType = billing_transaction_type
    self.Account = account
    self.Invoice = invoice
    self.Amount = amount
    self.IsElectronicTransaction = is_electronic_transaction
    self.Uid = uid
    self.Created = created
    self.Updated = updated
