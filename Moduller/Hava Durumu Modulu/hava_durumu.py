def hava_durumu_sehir(sehir):
    veriler = {
        "İstanbul": "Güneşli",
        "Ankara": "Yağmurlu",
        "İzmir": "Bulutlu"
    }
    return veriler.get(sehir, "Bilgi yok")

if __name__ == "__main__":
    print(hava_durumu_sehir("Ankara"))
    