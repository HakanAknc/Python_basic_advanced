"""
Proje 2
Math modülünde kullandığınız fonksiyonları kendiniz de ayrı bir modüle (Python dosyasına) yazmaya çalışın ve bu 
yazdığınız modülü kullanarak gelişmiş bir hesap makinesi yazın.
"""

import math_functions as mf

def hesap_makinesi():
    print("Gelişmiş Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Üs Alma")
    print("6. Karekök Alma")
    print("7. Sinüs")
    print("8. Kosinüs")
    print("9. Logaritma")
    print("0. Çıkış")

    while True:
        secim = input("Bir işlem seçin (0-9): ")

        if secim == '0':
            print("Çıkış yapılıyor...")
            break

        if secim in ['1', '2', '3', '4', '5']:
            x = float(input("Birinci sayıyı girin: "))
            y = float(input("İkinci sayıyı girin: "))

            if secim == '1':
                print(f"Sonuç: {mf.toplama(x, y)}")
            elif secim == '2':
                print(f"Sonuç: {mf.cikarma(x, y)}")
            elif secim == '3':
                print(f"Sonuç: {mf.carpma(x, y)}")
            elif secim == '4':
                print(f"Sonuç: {mf.bolme(x, y)}")
            elif secim == '5':
                print(f"Sonuç: {mf.us_alma(x, y)}")

        elif secim == '6':
            x = float(input("Bir sayıyı girin: "))
            print(f"Sonuç: {mf.karekök_alma(x)}")

        elif secim == '7':
            x = float(input("Açı (radyan cinsinden) girin: "))
            print(f"Sonuç: {mf.sin_alma(x)}")

        elif secim == '8':
            x = float(input("Açı (radyan cinsinden) girin: "))
            print(f"Sonuç: {mf.cos_alma(x)}")

        elif secim == '9':
            x = float(input("Logaritma tabanı ve değeri için sayıyı girin: "))
            print(f"Sonuç: {mf.logaritma(x)}")

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Hesap makinesini başlat
hesap_makinesi()
