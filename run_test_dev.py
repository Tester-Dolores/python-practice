import pytest
import time
import os

CASE_DIR = "./about_file/excel_test.py"
marked = ""

if __name__ == "__main__":
    pytest.main(["-s","-vv",CASE_DIR,"-m",marked])
