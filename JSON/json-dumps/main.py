import json

# Bir python sözlüğü (dictionary) oluşturuyoruz

data = {
    "name": "Hakan",
    "age": 20,
    "city": "Konya"
}

# Python sözlüğünü JSON formatına dönüştürmek için json.dumps kullanılır
json_data = json.dumps(data, indent=4)
print(json_data)

