"""
Python ile Girilen Sayının Pozitif Olup Olmadığını Bulmak
"""

sayi = int(input("Bir sayı giriniz: "))
if sayi == 0:
    print("Sıfır ne pozitif ne negatifir.")
elif sayi > 0:
    print(sayi, "pozitif bir sayıdır.")
else:
    print(sayi, "negatif bir saydır.")


# 2.yol
sayi = int(input("Bir sayı giriniz: "))
print(f"{sayi} {'pozitif' if sayi > 0 else 'negatif'} bir sayıdır.")