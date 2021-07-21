import pytest
import time
import os

CASE_DIR = "./other/gputil_test.py"
marked = ""

if __name__ == "__main__":
    pytest.main(["-s", "-vv", CASE_DIR, "-m", marked])
