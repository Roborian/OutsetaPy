from models.billing.transaction import Transaction
from models.wrappers.list import List
from util.request import Request
from util.store import Store

class Transactions:
  def __init__(self, store: Store):
    self.store = store

  async def get_all(self, account_uid: str) -> List[Transaction]:
    request = Request(self.store, f"billing/transactions/{account_uid}").authenticate_as_server()
    response = await request.get()

    if not response.ok:
      raise Exception(response)

    return await response.json() as List[Transaction]
