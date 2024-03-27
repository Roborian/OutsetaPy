from typing import List, Union
from datetime import date
from outsetapy.util.store import Store
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.util.request import Request, hasMoreResults
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
      raise Exception(response.json())
    elif response.ok:
      return response.json()
    else:
      raise response
    
  async def get_by_id(self, invoice_id: str) -> Invoice:
    request = Request(self.store, f'billing/invoices/{invoice_id}').authenticate_as_server()
    response = request.get()
    if not response.ok:
      raise response
    return response.json()
  
  async def get_all(self, options: dict = {}) -> List[Invoice]:
    has_more = True
    results = []
    while has_more:
      request = Request(self.store, 'billing/invoices').authenticate_as_server()
      if 'limit' in options:
        request.with_params({'limit': str(options['limit'])})
      if 'offset' in options:
        request.with_params({'offset': str(options['offset'])})

      response = request.get()
      if not response.ok:
        raise response
      
      json_response = response.json()
      results += json_response['items']
      has_more = hasMoreResults(json_response)
      options['offset'] = json_response['metadata']['offset'] + json_response['metadata']['limit']

    return [Invoice(json_obj) for json_obj in results]

# todo: Add functions for get_all, get_by_id
    
class InvoiceAdd:
  Subscription: Union[Subscription, None]
  InvoiceDate: date
  InvoiceLineItems: List[InvoiceLineItem]
