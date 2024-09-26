import json

def json_yaz(dosya_adi, veri):
    """Veriyi JSON formatında bir dosyaya yaz."""
    with open(dosya_adi, 'w', encoding='utf-8') as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)

def json_oku(dosya_adi):
    """JSON formatındaki veriyi bir dosyadan oku."""
    with open(dosya_adi, 'r', encoding='utf-8') as dosya:
        return json.load(dosya)

if __name__ == "__main__":
    # Örnek veri
    veri = {
        "kullanicilar": [
            {"isim": "Ahmet", "yas": 25},
            {"isim": "Ayşe", "yas": 30},
            {"isim": "Ali", "yas": 22}
        ]
    }
    
    # JSON dosyasına yaz
    json_yaz('kullanicilar.json', veri)
    
    # JSON dosyasından oku
    okunan_veri = json_oku('kullanicilar.json')
    print(okunan_veri)
