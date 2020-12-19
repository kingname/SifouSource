import time
from importlib import reload
import chapter_2.cache_of_import.util as util

while True:
    util = reload(util)
    util.print_content()
    time.sleep(2)
