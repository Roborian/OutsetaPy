from outsetapy.util.store import Store
from .cases import Cases


class Support:
    def __init__(self, store: Store):
        self.cases = Cases(store)
