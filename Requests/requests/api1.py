import requests

istek = requests.get("https://api.github.com")
# print(istek.headers)


istek = requests.get("https://api.github.com")
print(istek.json())

""""
json.dumps(): Bir Python objesini, JSON formatındaki bir stringe dönüştürür.
json.loads(): Bir JSON stringini, Python objesine dönüştürür.
"""
