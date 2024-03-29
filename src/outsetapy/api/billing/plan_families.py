from outsetapy.models.billing.plan_family import PlanFamily
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.util.store import Store
from outsetapy.models.wrappers.list import List


class PlanFamilies:
    def __init__(self, store: Store):
        self.store = store

    async def get_all(self, options: dict = {}) -> List[PlanFamily]:
        has_more = True
        results = []
        while has_more:
            request = Request(self.store, "billing/planfamilies")
            if "limit" in options:
                request.with_params({"limit": str(options["limit"])})
            if "offset" in options:
                request.with_params({"offset": str(options["offset"])})

            response = request.get()
            if not response.ok:
                raise response

            json_response = response.json()
            results += json_response["items"]
            has_more = hasMoreResults(json_response)
            options["offset"] = (
                json_response["metadata"]["offset"] + json_response["metadata"]["limit"]
            )

        return [PlanFamily(json_obj) for json_obj in results]
