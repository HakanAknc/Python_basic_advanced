import json

data = {"name": "Alice", "age": 25, "city": "London"}

with open('JSON/json-dump/data.json', 'w') as file:
    json.dump(data, file, indent=4)