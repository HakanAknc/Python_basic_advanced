"""
Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""

boy = float(input("Boyunuzu girin : "))
kilo = int(input("Kilonuzu giriniz: "))

bki = kilo / (boy ** 2)

print("Beden Kitle İndeksi: ", bki)