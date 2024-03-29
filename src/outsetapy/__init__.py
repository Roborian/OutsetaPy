from outsetapy.api.marketing import Marketing
from outsetapy.api.support import Support
from outsetapy.util.credentials import ServerCredentials, UserCredentials
from outsetapy.util.store import Store
from outsetapy.api.user import User
from outsetapy.api.billing import Billing
from outsetapy.api.crm import Crm


class OutsetaApiClient:
    def __init__(self, subdomain, accessToken=None, apiKey=None, secretKey=None):
        """
        Initializing without any keys:
        ```python
        from outseta_api_client import OutsetaApiClient
        client = OutsetaApiClient(subdomain='test-company')
        ```

        Initializing with server-side API keys:
        ```python
        from outseta_api_client import OutsetaApiClient
        client = OutsetaApiClient(subdomain='test-company', apiKey=example_key, secretKey=example_secret)
        ```

        Initializing with a user access token:
        ```python
        from outseta_api_client import OutsetaApiClient
        client = OutsetaApiClient(subdomain='test-company', accessToken=jwt_user_token)
        ```

        :param subdomain: If your Outseta domain is `tiltcamp.outseta.com`, this would be `tiltcamp`
        :param accessToken: A user's access token (if available)
        :param apiKey: A server-side API key (if available)
        :param secretKey: A server-side API key secret (if available)
        """
        base_url = f"https://{subdomain}.outseta.com/api/v1/"
        user_auth = UserCredentials(accessToken)
        server_auth = ServerCredentials(apiKey, secretKey)
        store = Store(base_url, user_auth, server_auth)

        self.billing = Billing(store)
        self.crm = Crm(store)
        self.marketing = Marketing(store)
        self.support = Support(store)
        self.user = User(store)
