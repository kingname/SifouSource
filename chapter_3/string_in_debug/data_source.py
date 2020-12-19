#  Copyright (c) 2020. by Kingname.
import json


def get_data():
    data = {'name': '青南', 'address': '上海'}
    a = json.dumps(data, ensure_ascii=False)
    b = json.dumps(a, ensure_ascii=False)
    return b

