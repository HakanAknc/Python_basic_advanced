"""
Enum Nedir?
Enum, yazılımda sabitleri (constant) düzenli ve anlamlı bir şekilde temsil etmek için kullanılan bir yapıdır. Python'da Enum modülü, belli bir grup sabiti bir sınıf altında toplamak için kullanılır.

Örneğin:

Renkleri (kırmızı, mavi, yeşil),
Günleri (Pazartesi, Salı...),
Yönleri (Kuzey, Güney...) sabit değerler olarak belirtebiliriz.
Enum, bu tür sabitlerin hem anlamlı isimlere sahip olmasını sağlar hem de programda daha düzenli bir kullanım sunar.
"""

"""
Enum Nasıl Kullanılır?
Enum kullanmak için Python’un enum modülünü import etmeliyiz:

from enum import Enum
Ardından bir Enum sınıfı oluşturup içine sabitler ekleyebiliriz.
"""

from enum import Enum

class Gunler(Enum):
    PAZARTESI = 1
    SALI = 2
    CARSAMBA = 3
    PERSEMBE = 4
    CUMA = 5
    CUMARTESI = 6
    PAZAR = 7

# Enum üyelerine erişim
print(Gunler.PAZARTESI)  # Gunler.PAZARTESI
print(Gunler.PAZARTESI.name)  # PAZARTESI
print(Gunler.PAZARTESI.value)  # 1


# * Enum Kullanımıyla Sabitler Tanımlama
class Yon(Enum):
    KUZEY = "N"
    GUNEY = "S"
    DOGU = "E"
    BATI = "W"

print(Yon.KUZEY)  # Yon.KUZEY
print(Yon.KUZEY.value)  # N


# * Enum'da Döngü
class Renk(Enum):
    KIRMIZI = 1
    YESIL = 2
    MAVI = 3

for renk in Renk:
    print(f"{renk.name} = {renk.value}")


# * Enum Üyelerine Erişim
print(Renk.KIRMIZI)  # Renk.KIRMIZI
print(Renk.KIRMIZI.value)  # 1
print(Renk.KIRMIZI.name)  # KIRMIZI


# * Enum Karşılaştırması
if Renk.KIRMIZI == Renk.YESIL:
    print("Aynı renk!")
else:
    print("Farklı renkler!")


# * Enum'a Özel Metotlar Eklemek
class Durum(Enum):
    AKTIF = 1
    PASIF = 2
    BEKLEMEDE = 3

    def aciklama(self):
        return f"{self.name} durumu, değer: {self.value}"

print(Durum.AKTIF.aciklama())  # AKTIF durumu, değer: 1
