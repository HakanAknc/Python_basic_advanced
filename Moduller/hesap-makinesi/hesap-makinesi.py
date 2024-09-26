# from toplama import topla
# from cikarma import cikar
# from carpma import carp
# from bolme import bol

import toplama
import cikarma
import carpma
import bolme

def main():
    print(*"*-*-*-*-*-")
    print("Hesap Makinesi Programı")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print(*"*-*-*-*-*-")


    secim = int(input("İşlem seçiniz (1-4): "))

    sayi1 = float(input("Birinci sayı: "))
    sayi2 = float(input("İkinci sayı: "))

    if secim == 1:
        print("Sonuç: ",toplama.topla(sayi1, sayi2))
    elif secim == 2:
        print("Sonuç: ",cikarma.cikar(sayi1, sayi2) )
    elif secim == 3:
        print("Sonuç: ",carpma.carp(sayi1, sayi2))
    elif secim == 4:
        print("Sonuç: ", bolme.bol(sayi1, sayi2))
    else:
        print("Geçersiz seçim...")

if __name__ == "__main__":
    main()