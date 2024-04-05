from outsetapy.util.store import Store
from outsetapy.util.request import Request
from outsetapy.util.credentials import UserCredentials
from .profile import Profile
from .password import Password


class LoginResponse:
    def __init__(self, access_token: str, expires_in: int, token_type: str):
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type


class User:
    def __init__(self, store: Store):
        self.password = Password(store)
        self.profile = Profile(store)
        self.store = store

    async def login(self, username: str, password: str) -> LoginResponse:
        request = Request(self.store, "tokens").with_body(
            {
                "username": username,
                "password": password
            }
        )
        response = request.post()
        if not response.ok:
            raise Exception(response.content)

        response_body = response.json()
        
        self.store.user_auth = UserCredentials(response_body["access_token"])
        return response_body

    async def impersonate(self, username: str) -> LoginResponse:
        request = (
            Request(self.store, "tokens")
            .authenticate_as_server()
            .with_body(
                {
                    "username": username,
                    "password": "",
                    "grant_type": "password",
                    "client_id": "outseta_auth_widget",
                }
            )
        )
        response = request.post()
        if not response.ok:
            raise Exception(response)

        response_body = response.json()
        self.store.user_auth.access_token = response_body["access_token"]
        return response_body
