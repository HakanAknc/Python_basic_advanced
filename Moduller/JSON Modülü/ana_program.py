from json_islemleri import json_yaz, json_oku

def main():
    # Kullanıcı verisi
    veri = {
        "kullanicilar": [
            {"isim": "Fatma", "yas": 28},
            {"isim": "Mehmet", "yas": 35},
            {"isim": "Zeynep", "yas": 26}
        ]
    }
    
    # JSON dosyasına yaz
    json_yaz('kullanicilar.json', veri)
    
    # JSON dosyasından oku
    okunan_veri = json_oku('kullanicilar.json')
    print(okunan_veri)

if __name__ == "__main__":
    main()
