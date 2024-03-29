import requests
from urllib.parse import urljoin, urlencode
from typing import Dict, Any
from outsetapy.static import OUTSETAPY_VERSION


class Request:
    def __init__(self, store, endpoint):
        self.store = store
        endpoint = endpoint.lstrip("/")
        self.url = urljoin(store.base_url, endpoint)
        self._options = {
            "headers": {
                "Content-Type": "application/json",
                "user-agent": "OutsetaPy/" + OUTSETAPY_VERSION,
            }
        }

    def authenticate_as_user(self):
        self._options["headers"][
            "Authorization"
        ] = self.store.user_auth.authorization_header
        return self

    def authenticate_as_user_preferred(self):
        if self.store.user_auth.is_ready:
            self.authenticate_as_user()
        elif self.store.server_auth.is_ready:
            self.authenticate_as_server()
        return self

    def authenticate_as_server(self):
        self._options["headers"][
            "Authorization"
        ] = self.store.server_auth.authorization_header
        return self

    def authenticate_as_server_preferred(self):
        if self.store.server_auth.is_ready:
            self.authenticate_as_server()
        elif self.store.user_auth.is_ready:
            self.authenticate_as_user()
        return self

    def with_params(self, params: Dict[str, str]):
        self.url += "?" + urlencode(params)
        return self

    def with_body(self, body: Dict[str, Any]):
        if "body" in self._options:
            existing_body = self._options["body"]
            body = {**existing_body, **body}
        self._options["body"] = body
        return self

    def get(self) -> requests.Response:
        return self.execute("GET")

    def post(self) -> requests.Response:
        return self.execute("POST")

    def put(self) -> requests.Response:
        return self.execute("PUT")

    def patch(self) -> requests.Response:
        return self.execute("PATCH")

    def delete(self) -> requests.Response:
        return self.execute("DELETE")

    def execute(self, method) -> requests.Response:
        self._options["method"] = method
        return requests.request(**self._options, url=self.url)


def hasMoreResults(meta) -> bool:
    return (
        meta["metadata"]["total"]
        > meta["metadata"]["offset"] + meta["metadata"]["limit"]
    )
