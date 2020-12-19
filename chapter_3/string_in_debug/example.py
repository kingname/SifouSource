import json
from data_source import get_data


data = get_data()
info = json.loads(data)
name = info['name']
print(name)
