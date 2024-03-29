from outsetapy.util.store import Store
from .activities import Activities
from .deals import Deals
from .people import People
from .accounts import Accounts


class Crm:
    def __init__(self, store: Store):
        self.accounts = Accounts(store)
        self.activities = Activities(store)
        self.deals = Deals(store)
        self.people = People(store)
