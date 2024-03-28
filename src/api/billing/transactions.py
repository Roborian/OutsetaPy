from outsetapy.models.billing.transaction import Transaction
from outsetapy.models.wrappers.list import List
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.util.store import Store

class Transactions:
  def __init__(self, store: Store):
    self.store = store

  async def get_all(self, account_uid: str) -> List[Transaction]:
    has_more = True
    results = []
    offset = 0
    limit = 25
    while has_more:
      request = Request(self.store, f"billing/transactions/{account_uid}").authenticate_as_server()
      request.with_params({'limit': limit})
      request.with_params({'offset': offset})
      response = request.get()

      if not response.ok:
        raise Exception(response)
      json_response = response.json()
      results += json_response['items']
      has_more = hasMoreResults(json_response)
      offset = offset + limit

    return [Transaction(json_obj) for json_obj in results]
