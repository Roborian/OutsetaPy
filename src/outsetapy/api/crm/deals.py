from typing import Union
from outsetapy.models.crm.deal import Deal
from outsetapy.models.crm.deal_pipeline_stage import DealPipelineStage
from outsetapy.models.wrappers.list import List
from outsetapy.models.wrappers.validation_error import ValidationError
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.util.store import Store


class DealAdd(Deal):
    Name: str
    DealPipelineStage: DealPipelineStage


class DealUpdate(Deal):
    Uid: str


class Deals:
    DEFAULT_FIELDS = "*"

    def __init__(self, store: Store):
        self.store = store

    async def get_all(self, options: dict = {}) -> List[Deal]:
        has_more = True
        results = []
        while has_more:
            request = (
                Request(self.store, "crm/deals")
                .authenticate_as_server()
                .with_params({"fields": options.get("fields", Deals.DEFAULT_FIELDS)})
            )
            if "limit" in options:
                request.with_params({"limit": str(options["limit"])})
            if "offset" in options:
                request.with_params({"offset": str(options["offset"])})
            if "deal_pipeline_stage" in options:
                request.with_params(
                    {"DealPipelineStage.Uid": options["deal_pipeline_stage"]}
                )

            response = request.get()
            if not response.ok:
                raise Exception(response)

            json_response = response.json()
            results += json_response["items"]
            has_more = hasMoreResults(json_response)
            options["offset"] = (
                json_response["metadata"]["offset"] + json_response["metadata"]["limit"]
            )

        return [Deal(**json_obj) for json_obj in results]

    async def get(self, uid: str, fields=None) -> Deal:
        request = (
            Request(self.store, f"crm/deals/{uid}")
            .with_params({"fields": fields or Deals.DEFAULT_FIELDS})
            .authenticate_as_server()
        )

        response = request.get()

        if not response.ok:
            raise Exception(response)

        json_response = response.json()
        return Deal(**json_response)

    async def add(
        self, deal: DealAdd, fields=None
    ) -> Union[Deal, ValidationError[Deal]]:
        request = (
            Request(self.store, "crm/deals")
            .with_params({"fields": fields or Deals.DEFAULT_FIELDS})
            .authenticate_as_server()
            .with_body(deal)
        )

        response = await request.post()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            json_response = response.json()
            return Deal(**json_response)
        else:
            raise Exception(response)

    async def update(
        self, deal: DealUpdate, fields=None
    ) -> Union[Deal, ValidationError[Deal]]:
        request = (
            Request(self.store, f"crm/deals/{deal.Uid}")
            .with_params({"fields": fields or Deals.DEFAULT_FIELDS})
            .authenticate_as_server()
            .with_body(deal)
        )

        response = await request.put()

        if response.status == 400:
            raise Exception(response.json())
        elif response.ok:
            json_response = response.json()
            return Deal(**json_response)
        else:
            raise Exception(response)

    async def delete(self, uid: str) -> None:
        request = Request(self.store, f"crm/deals/{uid}").authenticate_as_server()

        response = await request.delete()

        if not response.ok:
            raise Exception(response)

        return None
