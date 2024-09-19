import requests

istek = requests.get("https://api.github.com")
print(istek)
print(istek.status_code)
print(*"--------")

istek = requests.get("https://api.github.com/boyle-bir-yer-yok")
print(istek)
print(istek.status_code)
