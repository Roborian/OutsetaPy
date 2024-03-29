from outsetapy import OutsetaApiClient
from tests.utils import TEST_DATA_DIR

# Directory for testing paling.__init__
INIT_DIR = TEST_DATA_DIR / "init_test"


def test_init(options):
    outseta = OutsetaApiClient(
        subdomain=options["subdomain"],
        apiKey=options["apiKey"],
        secretKey=options["secretKey"],
    )

    assert outseta.__class__ == OutsetaApiClient
