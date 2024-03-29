from outsetapy.util.store import Store
from outsetapy.models.crm.person import Person
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.models.wrappers.list import List
from outsetapy.models.wrappers.validation_error import ValidationError


class People:
    def __init__(self, store: Store):
        self.store = store

    async def get_all(self, options: dict = {}) -> List[Person]:
        has_more = True
        results = []
        while has_more:
            request = Request(self.store, "crm/people").authenticate_as_server()
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

        return [Person(json_obj) for json_obj in results]

    async def get(self, uid: str) -> Person:
        request = Request(self.store, f"crm/people/{uid}").authenticate_as_server()
        response = request.get()

        if not response.ok:
            raise Exception(response)
        return response.json()

    async def add(self, person: dict) -> Person:
        request = (
            Request(self.store, "crm/people").authenticate_as_server().with_body(person)
        )
        response = await request.post()

        if response.status == 400:
            return response.json()
        elif response.ok:
            return response.json()
        else:
            raise Exception(response)

    async def update(self, person: dict) -> Person:
        request = (
            Request(self.store, f'crm/people/{person["Uid"]}')
            .authenticate_as_server()
            .with_body(person)
        )
        response = await request.put()

        if response.status == 400:
            return response.json()
        elif response.ok:
            return response.json()
        else:
            raise Exception(response)

    async def delete(self, uid: str) -> None:
        request = Request(self.store, f"crm/people/{uid}").authenticate_as_server()
        response = await request.delete()

        if not response.ok:
            raise Exception(response)
        return None


class PersonAdd(Person):
    Email: str


class PersonUpdate(Person):
    Uid: str
