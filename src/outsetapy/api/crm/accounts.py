from datetime import datetime
from typing import List, Union
from outsetapy.models.crm.account import Account
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.models.crm.account_stage import AccountStage
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.models.billing.subscription import Subscription


class Accounts:
    def __init__(self, store):
        self.store = store

    async def get_all(self, options: dict = {}) -> List[Account]:
        has_more = True
        results = []
        while has_more:
            request = (
                Request(self.store, "crm/accounts")
                .authenticate_as_server()
                .with_params(
                    {
                        "fields": options.get(
                            "fields", "*,PersonAccount.*,PersonAccount.Person.Uid"
                        )
                    }
                )
            )
            if "limit" in options:
                request.with_params({"limit": str(options["limit"])})
            if "offset" in options:
                request.with_params({"offset": str(options["offset"])})
            if "accountStage" in options:
                request.with_params({"AccountStage": str(options["accountStage"])})

            response = request.get()
            if not response.ok:
                raise Exception(response)

            json_response = response.json()
            results += json_response["items"]
            has_more = hasMoreResults(json_response)
            options["offset"] = (
                json_response["metadata"]["offset"] + json_response["metadata"]["limit"]
            )

        return [Account(json_obj, self.store) for json_obj in results]

    async def get(self, uid: str, options: dict = {}) -> Account:
        request = (
            Request(self.store, f"crm/accounts/{uid}")
            .authenticate_as_server()
            .with_params(
                {
                    "fields": options.get(
                        # "fields", "*,PersonAccount.*,PersonAccount.Person.Uid"
                        "fields", "*,PersonAccount.*,BillingAddress.*,MailingAddress.*,PersonAccount.Person.Uid,CurrentSubscription.Uid,LatestSubscription.Uid, PrimarySubscription.Uid, PrimaryContact.*"
                    )
                }
            )
        )
        response = request.get()

        if not response.ok:
            raise Exception(response)
        response_json = response.json()
        return Account(response_json, self.store)

    async def add(
        self, account: dict, options: dict = {}
    ) -> Union[Account, ValidationError[Account]]:
        request = (
            Request(self.store, "crm/accounts")
            .authenticate_as_server()
            .with_body(account)
            .with_params(
                {
                    "fields": options.get(
                        "fields", "*,PersonAccount.*,PersonAccount.Person.Uid"
                    )
                }
            )
        )
        response = await request.post()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            response_json = response.json()
            return Account(response_json, self.store)
        else:
            raise Exception(response)

    async def update(
        self, account: dict, options: dict = {}
    ) -> Union[Account, ValidationError[Account]]:
        request = (
            Request(self.store, f'crm/accounts/{account["Uid"]}')
            .authenticate_as_server()
            .with_body(account)
            .with_params(
                {
                    "fields": options.get(
                        "fields", "*,PersonAccount.*,PersonAccount.Person.Uid"
                    )
                }
            )
        )
        response = await request.put()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            response_json = response.json()
            return Account(response_json, self.store)
        else:
            raise Exception(response)

    async def cancel(self, cancellation: dict) -> Union[None, ValidationError[Account]]:
        request = (
            Request(
                self.store,
                f'crm/accounts/cancellation/{cancellation["Account"]["Uid"]}',
            )
            .authenticate_as_server()
            .with_body(cancellation)
        )

        response = await request.put()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            return None
        else:
            raise Exception(response)

    async def delete(self, uid: str) -> None:
        request = Request(self.store, f"crm/accounts/{uid}").authenticate_as_server()
        response = await request.delete()

        if not response.ok:
            raise Exception(response)
        return None

    async def extend_trial(
        self, uid: str, date: datetime
    ) -> Union[None, ValidationError[Subscription]]:
        request = (
            Request(self.store, f"crm/accounts/{uid}/extend-trial")
            .authenticate_as_server()
            .with_body({"ToDate": date})
        )
        response = await request.put()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            return None
        else:
            raise Exception(response)

    async def remove_cancellation(
        self, uid: str
    ) -> Union[None, ValidationError[Account]]:
        request = Request(
            self.store, f"crm/accounts/{uid}/remove-cancellation"
        ).authenticate_as_server()
        response = await request.put()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            return None
        else:
            raise Exception(response)

    async def expire_current_subscription(
        self, uid: str
    ) -> Union[None, ValidationError[Subscription]]:
        request = Request(
            self.store, f"crm/accounts/{uid}/expire-current-subscription"
        ).authenticate_as_server()
        response = await request.put()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            return None
        else:
            raise Exception(response)


class AccountAdd(dict):
    def __init__(self, name: str, account_stage: AccountStage, **kwargs):
        super().__init__(**kwargs)
        self["Name"] = name
        self["AccountStage"] = account_stage


class AccountUpdate(dict):
    def __init__(self, uid: str, **kwargs):
        super().__init__(**kwargs)
        self["Uid"] = uid


class AccountCancellation(dict):
    def __init__(self, account: AccountUpdate, **kwargs):
        super().__init__(**kwargs)
        self["Account"] = account
