"""
Python ile Girilen Sayının Tek mi Çift mi Olduğunu Bulma
"""

sayi = int(input("Bir sayı giriniz: "))
if sayi % 2 == 0:
    sonuc = "Çift"
else:
    sonuc = "Tek"
print(sayi, sonuc, "bir sayıdır.")

print(*"------")

# 2.yol
print("Girdiğiniz sayı ", "çift" if int(input("Bir sayı giriniz: ")) % 2 == 0 else "tek", "bir sayıdr.")