from typing import Optional, Union
from outsetapy.models.crm.person import Person
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.util.request import Request
from outsetapy.util.store import Store


class ProfileUpdate(dict):
    def __init__(self, uid: str, **kwargs):
        super().__init__(**kwargs)
        self["Uid"] = uid


class Profile:
    def __init__(self, store: Store):
        self.store = store

    async def get(self, fields: Optional[str] = None) -> Person:
        request = Request(self.store, "profile").authenticate_as_user()
        if fields:
            request.with_params({"fields": fields})

        response = request.get()

        if not response.ok:
            raise Exception(response)
        return Person(response.json(), self.store)

    async def update(
        self, profile: ProfileUpdate
    ) -> Person:
        request = (
            Request(self.store, "profile").authenticate_as_user().with_body(profile)
        )
        response = await request.put()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            return Person(response.json(), self.store)
        else:
            raise Exception(response)
