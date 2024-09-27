import json

json_string = '{"name": "Alice", "age": 25, "city": "London"}'
data = json.loads(json_string)
print(data)