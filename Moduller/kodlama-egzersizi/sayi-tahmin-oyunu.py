import random
import time

print("""************************

Sayı Tahmin Oyunu


1 ile 1000 arasında sayıyı tahmin edin.

************************""")

rastgele_sayı = random.randint(1,100)
tahmin_hakki = 5

while True:

    tahmin = int(input("Tahmininiz: "))

    if (tahmin < rastgele_sayı):
        print("Bilgileriniz sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin...")

        tahmin_hakki -= 1

    elif (tahmin > rastgele_sayı):
        print("Bilgileriniz sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin...")

        tahmin_hakki -= 1

    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! Sayımız",rastgele_sayı)
        break
    if (tahmin_hakki == 0):
        print("Tahmin hakkınız bitti...")
        print("Sayımız:",rastgele_sayı)
        break