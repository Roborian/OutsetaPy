import contextlib
import os
import sys
import platform
import subprocess
import tempfile
import time
from pathlib import Path

import psutil

# Path to the test data folder.
TEST_DATA_DIR = Path(__file__).parent / "data"

def setup_test():
    """Setup the test environment."""
    # Ensure the test data directory exists.
    TEST_DATA_DIR.mkdir(exist_ok=True)