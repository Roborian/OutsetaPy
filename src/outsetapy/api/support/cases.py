from typing import Union
from outsetapy.models.support.case import Case
from outsetapy.models.support.case_history import CaseHistory
from outsetapy.models.wrappers.list import List
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.util.store import Store


class Cases:
    DEFAULT_FIELDS = ["*"]

    def __init__(self, store: Store):
        self.store = store

    async def get_all(self, options: dict = {}) -> List[Case]:
        has_more = True
        results = []
        while has_more:
            request = (
                Request(self.store, "support/cases")
                .with_params(
                    {"fields": options.get("fields", ",".join(Cases.DEFAULT_FIELDS))}
                )
                .authenticate_as_server()
            )

            if "limit" in options:
                request.with_params({"limit": str(options["limit"])})
            if "offset" in options:
                request.with_params({"offset": str(options["offset"])})

            if "FromPerson" in options:
                from_person = options["FromPerson"]
                if "Uid" in from_person:
                    request.with_params({"FromPerson.Uid": from_person["Uid"]})
                elif "Email" in from_person:
                    request.with_params({"FromPerson.Email": from_person["Email"]})

            response = request.get()

            if not response.ok:
                raise response

            response_json = response.json()
            results += response_json["items"]
            has_more = hasMoreResults(response_json)
            options["offset"] = (
                response_json["metadata"]["offset"] + response_json["metadata"]["limit"]
            )

        return [Case(json_obj) for json_obj in results]

    async def add(
        self, new_case: dict, options: dict = {}
    ) -> Union[Case, ValidationError[Case]]:
        request = (
            Request(self.store, "support/cases")
            .with_params(
                {"fields": options.get("fields", ",".join(Cases.DEFAULT_FIELDS))}
            )
            .authenticate_as_server()
            .with_body(new_case)
        )

        if "sendAutoResponder" in options:
            request.with_params(
                {"sendAutoResponder": str(options["sendAutoResponder"])}
            )

        response = await request.post()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            response_json = response.json()
            return Case(response_json)
        else:
            raise response

    async def add_reply_from_agent(self, reply: dict) -> None:
        request = (
            Request(self.store, f"support/cases/{reply['Case']['Uid']}/replies")
            .authenticate_as_server()
            .with_body(reply)
        )

        response = await request.post()

        if not response.ok:
            raise response

    async def add_reply_from_client(self, reply: dict) -> CaseHistory:
        request = Request(
            self.store,
            f"support/cases/{reply['Case']['Uid']}/clientresponse/{reply['Comment']}",
        ).authenticate_as_server()

        response = await request.post()

        if response.ok:
            return CaseHistory(response.json())
        else:
            raise response


class CaseAdd:
    def __init__(self, new_case: dict):
        self.FromPerson = new_case["FromPerson"]
        self.Subject = new_case["Subject"]
        self.Body = new_case["Body"]
        self.Source = new_case["Source"]
        self.__dict__.update(new_case)


class SupportReply:
    def __init__(self, reply: dict):
        self.AgentName = reply["AgentName"]
        self.Case = reply["Case"]
        self.Comment = reply["Comment"]
        self.__dict__.update(reply)


class ClientReply:
    def __init__(self, reply: dict):
        self.Case = reply["Case"]
        self.Comment = reply["Comment"]
        self.__dict__.update(reply)
