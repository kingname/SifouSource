import sys
import pathlib
import os

with open('resource.txt') as f:
    content = f.read()
    print(content)

current_folder = pathlib.Path(__file__).absolute().parent
parent_folder = current_folder.parent
sys.path.insert(0, str(parent_folder))
from utils.util import hello
hello()

