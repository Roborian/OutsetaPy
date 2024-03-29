class Credentials:
    def __init__(self):
        self.authorization_header = ""
        self.is_ready = False


class ServerCredentials(Credentials):
    def __init__(self, api_key=None, secret_key=None):
        super().__init__()
        self.api_key = api_key
        self.secret_key = secret_key
        self._is_ready = True

    @property
    def authorization_header(self):
        if not self.is_ready:
            raise Exception("The API client was not initialized with API keys.")
        return f"Outseta {self.api_key}:{self.secret_key}"

    @authorization_header.setter
    def authorization_header(self, value):
        self._access_token = value

    @property
    def is_ready(self):
        return bool(self.api_key and self.secret_key)

    @is_ready.setter
    def is_ready(self, value):
        self._is_ready = value


class UserCredentials(Credentials):
    def __init__(self, access_token=None):
        super().__init__()
        self._access_token = access_token
        self._is_ready = True

    @property
    def authorization_header(self):
        if not self.is_ready:
            raise Exception(
                "The API client doesn't have a user token. Please initialize the client with one or call profile.login() first."
            )
        return f"bearer {self._access_token}"

    @authorization_header.setter
    def authorization_header(self, value):
        self._access_token = value

    @property
    def is_ready(self):
        return bool(self._access_token)

    @is_ready.setter
    def is_ready(self, value):
        self._is_ready = value
