import json

with open('data.json', 'r') as file:
    data = json.load(file)  # Dosyadan okunan JSON verisi Python sözlüğüne çevrilir
    print(data)
