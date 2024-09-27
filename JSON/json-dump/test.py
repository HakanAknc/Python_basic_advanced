import json

data = {"Isim": "Hakan", "Soyisim": "Akinci", "Yas": 22, "Meslek": "Backend", "Maas": 50000}

with open("JSON/json-dump/hakan.json", 'w') as file:
    json.dump(data, file, indent=4)