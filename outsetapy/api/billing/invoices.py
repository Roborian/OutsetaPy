from typing import List, Union
from datetime import date
from outsetapy.util.store import Store
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.util.request import Request
from outsetapy.models.billing.invoice import Invoice
from outsetapy.models.billing.subscription import Subscription
from outsetapy.models.billing.invoice_line_item import InvoiceLineItem
from typing import List, Union
from datetime import date
from outsetapy.models.billing.subscription import Subscription
from outsetapy.models.billing.invoice_line_item import InvoiceLineItem

class Invoices:
  def __init__(self, store: Store):
    self.store = store

  async def add(self, invoice: dict) -> Union[Invoice, ValidationError[Invoice]]:
    request = Request(self.store, 'billing/invoices') \
      .authenticate_as_server() \
      .with_body(invoice)
    response = await request.post()

    if response.status == 400:
      raise Exception(await response.json())
    elif response.ok:
      return await response.json()
    else:
      raise response
    
class InvoiceAdd:
  Subscription: Union[Subscription, None]
  InvoiceDate: date
  InvoiceLineItems: List[InvoiceLineItem]
