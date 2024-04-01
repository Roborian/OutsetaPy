from outsetapy.models.billing.plan_family import PlanFamily
from outsetapy.util.store import Store
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.models.billing.subscription import Subscription
from outsetapy.models.crm.account import Account
from outsetapy.models.wrappers.list import List
from outsetapy.models.billing.charge_summary import ChargeSummary


class SubscriptionAdd:
    def __init__(self, subscription: dict):
        self.__dict__ = subscription


class SubscriptionUpdate:
    def __init__(self, subscription: dict):
        self.__dict__ = subscription


class SubscriptionUpgradeRequired:
    def __init__(self, subscription: dict):
        self.__dict__ = subscription


class Subscriptions:
    def __init__(self, store: Store):
        self.store = store

    async def get_all(self, options: dict = {}) -> List[Subscription]:
        has_more = True
        results = []
        while has_more:
            request = Request(self.store, "billing/subscriptions")
            if "limit" in options:
                request.with_params({"limit": str(options["limit"])})
            if "offset" in options:
                request.with_params({"offset": str(options["offset"])})

            response = request.get()
            if not response.ok:
                raise Exception(response)

            json_response = response.json()
            results += json_response["items"]
            has_more = hasMoreResults(json_response)
            options["offset"] = (
                json_response["metadata"]["offset"] + json_response["metadata"]["limit"]
            )

        return [Subscription(json_obj, self.store) for json_obj in results]

    async def get(self, uid: str, options: dict = {}) -> Subscription:
        request = Request(
            self.store, f"billing/subscriptions/{uid}"
        ).authenticate_as_server()

        if "fields" in options:
            request.with_params({"fields": options["fields"]})
        else:
            request.with_params({"fields": "*,Account.Uid,Plan.Uid"})

        response = request.get()

        if not response.ok:
            raise Exception(response)
        json_response = response.json()
        return Subscription(json_response, self.store)

    async def add(
        self, subscription: dict
    ) -> Subscription:
        request = (
            Request(self.store, "billing/subscriptions/firsttimesubscription")
            .authenticate_as_server()
            .with_body(subscription)
        )
        response = await request.put()

        if response.status == 400:
            raise ValidationError(response.json())
        elif response.ok:
            return Subscription(response.json(), self.store)
        else:
            raise Exception(response)

    async def preview_add(
        self, subscription: dict
    ) -> ChargeSummary | ValidationError[Subscription]:
        request = (
            Request(self.store, "billing/subscriptions/compute-charge-summary")
            .authenticate_as_server()
            .with_body(subscription)
        )
        response = await request.post()

        if response.status == 400:
            raise ValidationError(response.json())
        elif response.ok:
            return ChargeSummary(response.json())
        else:
            raise Exception(response)

    async def update(
        self, subscription: dict
    ) -> Subscription | ValidationError[Subscription]:
        request = (
            Request(
                self.store,
                f'billing/subscriptions/{subscription["Uid"]}/changesubscription',
            )
            .authenticate_as_server()
            .with_body(subscription)
        )
        response = await request.put()

        if response.status == 400:
            raise ValidationError(response.json())
        elif response.ok:
            return Subscription(response.json(), self.store)
        else:
            raise Exception(response)

    async def preview_update(
        self, subscription: dict
    ) -> ChargeSummary | ValidationError[Subscription]:
        request = (
            Request(
                self.store,
                f'billing/subscriptions/{subscription["Uid"]}/changesubscriptionpreview',
            )
            .authenticate_as_server()
            .with_body(subscription)
        )
        response = await request.put()

        if response.status == 400:
            raise ValidationError(response.json())
        elif response.ok:
            return ChargeSummary(response.json())
        else:
            raise Exception(response)

    async def set_subscription_upgrade_required(
        self, subscription: dict
    ) -> Subscription | ValidationError[None]:
        request = (
            Request(
                self.store,
                f'billing/subscriptions/{subscription["Uid"]}/setsubscriptionupgraderequired',
            )
            .authenticate_as_server()
            .with_body(subscription)
        )
        response = await request.put()

        if response.status == 400:
            raise ValidationError(response.json())
        elif response.ok:
            return Subscription(response.json(), self.store)
        else:
            raise Exception(response)

    async def change_trial_to_subscribed(
        self, uid: str
    ) -> None | ValidationError[Account]:
        request = Request(
            self.store, f"billing/subscriptions/{uid}/changetrialtosubscribed"
        ).authenticate_as_server()
        response = await request.put()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            return None
        else:
            raise Exception(response)
