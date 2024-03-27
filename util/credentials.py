class Credentials:
    def __init__(self):
        self.authorization_header = ""
        self.is_ready = False

class ServerCredentials(Credentials):
    def __init__(self, api_key=None, secret_key=None):
        super().__init__()
        self.api_key = api_key
        self.secret_key = secret_key

    @property
    def authorization_header(self):
        if not self.is_ready:
            raise Exception('The API client was not initialized with API keys.')
        return f"Outseta {self.api_key}:{self.secret_key}"

    @property
    def is_ready(self):
        return bool(self.api_key and self.secret_key)

class UserCredentials(Credentials):
    def __init__(self, access_token=None):
        super().__init__()
        self.access_token = access_token

    @property
    def authorization_header(self):
        if not self.is_ready:
            raise Exception('The API client doesn\'t have a user token. Please initialize the client with one or call profile.login() first.')
        return f"bearer {self.access_token}"

    @property
    def is_ready(self):
        return bool(self.access_token)