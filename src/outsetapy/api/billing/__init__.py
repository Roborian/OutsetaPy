from outsetapy.util.store import Store
from .plans import Plans
from .invoices import Invoices
from .subscriptions import Subscriptions
from .plan_families import PlanFamilies
from .transactions import Transactions
from .usage import Usage


class Billing:
    def __init__(self, store: Store):
        self.invoices = Invoices(store)
        self.plans = Plans(store)
        self.plan_families = PlanFamilies(store)
        self.subscriptions = Subscriptions(store)
        self.transactions = Transactions(store)
        self.usage = Usage(store)
