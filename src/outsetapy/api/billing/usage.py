from typing import List, Optional, Union
from datetime import datetime
from dataclasses import dataclass
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.models.billing.subscription_add_on import SubscriptionAddOn
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.models.billing.usage_item import UsageItem


@dataclass
class UsageAdd:
    Amount: int
    SubscriptionAddOn: SubscriptionAddOn
    UsageDate: datetime
    # Define any additional fields for UsageAdd here


@dataclass
class Account:
    Uid: str


@dataclass
class SubscriptionAddOn:
    Uid: str


class Usage:
    DEFAULT_FIELDS = [
        "*",
        "Invoice.Uid",
        "SubscriptionAddOn.*",
        "SubscriptionAddOn.Subscription.Uid",
        "SubscriptionAddOn.Subscription.Account.Uid",
        "SubscriptionAddOn.AddOn.Uid",
    ]

    def __init__(self, store):
        self.store = store

    async def get_all(self, options: dict = {}) -> List[UsageItem]:
        has_more = True
        results = []
        while has_more:
            request = Request(self.store, "billing/usage")
            if "limit" in options:
                request.with_params({"limit": str(options["limit"])})
            if "offset" in options:
                request.with_params({"offset": str(options["offset"])})
            if "fields" in options:
                request.with_params({"fields": options["fields"]})
            if "Account" in options:
                request.with_params(
                    {
                        "SubscriptionAddOn.Subscription.Account.Uid": options[
                            "Account"
                        ].Uid
                    }
                )

            response = request.get()
            if not response.ok:
                raise response

            json_response = response.json()
            results += json_response["items"]
            has_more = hasMoreResults(json_response)
            options["offset"] = (
                json_response["metadata"]["offset"] + json_response["metadata"]["limit"]
            )

        return results

    async def add(
        self, usage: UsageAdd, fields: Optional[str] = None
    ) -> Union[UsageItem, ValidationError[UsageItem]]:
        request = (
            Request(self.store, "billing/usage")
            .authenticate_as_server()
            .with_params(
                {"fields": fields if fields else ",".join(Usage.DEFAULT_FIELDS)}
            )
            .with_body(usage)
        )
        response = await request.post()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            return response.json()
        else:
            raise response
