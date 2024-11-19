"""
Enum nedir?
enum, sabit değerler kümesini bir sınıf içinde gruplayarak onlara anlamlı isimler verir. 
Bu sabitler, genellikle bir kategoriye ait değerleri ifade etmek için kullanılır (örneğin, günler, renkler, yönler vb.).
Python'daki enum modülü, bu tür sabitleri tanımlamak için bir Enum sınıfı sağlar.
"""

from enum import Enum

class Renk(Enum):
    KIRMIZI = 1
    YESIL = 2
    MAVI = 3

"""
Bu örnekte, Renk adında bir enum sınıfı oluşturduk. 
Bu sınıfın KIRMIZI, YESIL ve MAVI adında üç üyesi var. Her üyenin kendine özgü bir değeri bulunur (1, 2, 3).
"""

# Enum Üyelerine Erişim

# İsimle erişim
print(Renk.KIRMIZI)
print(Renk.YESIL)
print(Renk.MAVI)

print(*"***")

# Değerle erişim
print(Renk.KIRMIZI.value)
print(Renk.MAVI.value)
print(Renk.YESIL.value)

print(*"***")

# Enum adını yazdırmak
print(Renk.KIRMIZI.name)
print(Renk.YESIL.name)
print(Renk.MAVI.name)

print("------------------------------------------")

for renk in Renk:
    print(f"{renk.name} = {renk.value}")

print("------------------------------------------")

if Renk.KIRMIZI == Renk.KIRMIZI:
    print("Aynı!")
else:
    print("Farklı!")

print("------------------------------------------")

class Durum(Enum):
    BASARILI = 1
    BASARISIZ = 2
    BEKLEMEDE = 3

    def describe(self):
        return f"{self.name} ({self.value})"

print(Durum.BASARILI.describe())  # BASARILI (1)

print("------------------------------------------")

class Yon(Enum):
    KUZEY = "N"
    GUNEY = "S"
    DOGU = "E"
    BATI = "W"

print(Yon.KUZEY.value)  # 'N'


"""
? Enum'un Avantajları
! Okunabilirlik: Sabitlerin isimlendirilmesi kodu daha anlamlı yapar.
! Hata Önleme: Sabitlerin yanlış yazılmasını engeller.
! Gruplama: İlgili sabitleri tek bir sınıf altında toplar.
! Karşılaştırma Kolaylığı: Sabitlerin eşitliği kolayca kontrol edilebilir.
"""