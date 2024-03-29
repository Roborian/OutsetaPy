from outsetapy.util.store import Store
from .email_list_subscriptions import EmailListSubscriptions


class Marketing:
    def __init__(self, store: Store):
        self.emailListSubscriptions = EmailListSubscriptions(store)
