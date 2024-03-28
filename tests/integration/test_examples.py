import os
import time
from tempfile import TemporaryDirectory, NamedTemporaryFile

from tests.utils import setup_test
import asyncio

def test_00_index(driver=None):
    print("test_00_index")

def test_example_01():
    from examples.test import main as example_01_main
    print("test_example_01")
    asyncio.run(example_01_main())
