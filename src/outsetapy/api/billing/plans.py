from outsetapy.models.billing.plan_family import PlanFamily
from outsetapy.util.request import Request, hasMoreResults
from outsetapy.util.store import Store
from outsetapy.models.wrappers.list import List
from outsetapy.models.billing.plan import Plan


class Plans:
    def __init__(self, store: Store):
        self.store = store

    """
  Get all available plans.

  ```python
  client = OutsetaApiClient(subdomain='test-company')
  response = client.billing.plans.get_all()
  print(response)
  ```

  :param limit: The number of results returned by the API.
  :param offset: For pagination; returns (limit) results after this value.
  :param plan_family: Get all plans that belong to a specific plan family.
  :returns: The response body.
  :raises Response: If the server returns a non-"OK" status, the whole response object will be thrown.
  """

    async def get_all(
        self, limit: int = None, offset: int = None, plan_family: PlanFamily = None
    ) -> List[Plan]:
        has_more = True
        results = []
        while has_more:
            request = Request(self.store, "billing/plans")
            if limit:
                request.with_params({"limit": str(limit)})
            if offset:
                request.with_params({"offset": str(offset)})
            if plan_family:
                request.with_params({"PlanFamily.Uid": plan_family.Uid})

            response = request.get()

            if not response.ok:
                raise response
            json_response = response.json()
            results += json_response["items"]
            has_more = hasMoreResults(json_response)
            offset = (
                json_response["metadata"]["offset"] + json_response["metadata"]["limit"]
            )

        return [Plan(json_obj) for json_obj in results]
