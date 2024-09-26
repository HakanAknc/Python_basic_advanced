from arac import Arac

def main():
    arac1 = Arac("Ford", "Fiesta", 2018)
    arac1.hiz_artir(30)
    arac1.hiz_dusur(10)
    print(arac1.bilgi_ver())

    arac2 = Arac("Honda", "Civic", 2021)
    arac2.hiz_artir(40)
    print(arac2.bilgi_ver())

if __name__ == "__main__":
    main()