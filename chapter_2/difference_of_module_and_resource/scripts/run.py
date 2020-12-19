import os
import sys
import pathlib
from utils.util import hello


def run():
    hello()
    current_path = pathlib.Path(__file__).absolute().parent
    os.chdir(str(current_path))
    with open('resource.txt') as f:
        content = f.read()
        print(content)

