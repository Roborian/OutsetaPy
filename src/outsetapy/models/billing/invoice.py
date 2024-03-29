from .subscription import Subscription


class Invoice:
    def __init__(self):
        self.InvoiceDate = None
        self.PaymentReminderSentDate = None
        self.Number = 0
        self.BillingInvoiceStatus = 0
        self.Subscription = Subscription()
        self.Amount = 0
        self.AmountOutstanding = 0
        self.InvoiceLineItems = []
        self.IsUserGenerated = False
        self.Uid = ""
        self.Created = None
        self.Updated = None
