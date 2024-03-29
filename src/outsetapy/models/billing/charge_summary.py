from typing import List
from datetime import date


class InvoiceDisplayItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class ChargeSummary:
    def __init__(
        self,
        number: int,
        invoice_date: date,
        subtotal: float,
        tax: float,
        paid: float,
        invoice_display_items: List[InvoiceDisplayItem],
        total: float,
        balance: float,
    ):
        self.number = number
        self.invoice_date = invoice_date
        self.subtotal = subtotal
        self.tax = tax
        self.paid = paid
        self.invoice_display_items = invoice_display_items
        self.total = total
        self.balance = balance
