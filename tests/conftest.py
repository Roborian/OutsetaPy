import os
import platform
from unittest import mock

import pytest

@pytest.fixture
def test_setup():
    options = {}
    options['subdomain'] = os.getenv('OUTSETA_SUBDOMAIN', 'x')
    options['apiKey'] = os.getenv('OUTSETA_API_KEY', 'x')
    options['secretKey'] = os.getenv('OUTSETA_SECRET_KEY', 'x')
    yield options
