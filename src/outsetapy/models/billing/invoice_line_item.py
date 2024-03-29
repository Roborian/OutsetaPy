from typing import Optional
import importlib
from datetime import date
from outsetapy.models.shared.entity import EntityType


class InvoiceLineItem:
    def __init__(
        self,
        description: str,
        unit_of_measure: str,
        rate: float,
        amount: float,
        tax: float,
        line_item_type: EntityType,
        uid: str,
        created: date,
        updated: date,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        quantity: Optional[int] = None,
        invoice_id: Optional[str] = None,
        line_item_entity_uid: Optional[str] = None,
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.unit_of_measure = unit_of_measure
        self.quantity = quantity
        self.rate = rate
        self.amount = amount
        self.tax = tax
        self.line_item_type = line_item_type
        self.line_item_entity_uid = line_item_entity_uid
        self.uid = uid
        self.created = created
        self.updated = updated

        def get_invoice(self):
            Invoice = importlib.import_module(
                "outsetapy.models.billing.invoice"
            ).Invoice
            return Invoice
