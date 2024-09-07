print(35)

print(3.14)

a = 4
b = 15
print(a+b)

print("Mustafa Murat Coşkun")

print("Murat'ın bugün dersi var.")

print("Murat",12,545,66767,3.56)

print("Mustafa","Murat","Coşkun")

"""
Stringlerdeki Özel Karakterler
Pythonda stringlerde kullanılan özel karakterler mevcuttur ve kullanıldıkları yerler de işlerimizi kolaylaştırır. En çok kullanılan 2 tanesi şunlardır;
"""
"""
\n karakteri
Eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa alt satırdan ekrana yazdırma işlemine devam eder. Hemen örneklerimize bakalım.
"""

print("Merhaba\nNasılsın\nİyi misin")
print("Selam\nGençler")

"""
\t karakteri
Eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa bir tab boşluk bırakarak ekrana yazdırma işlemine devam eder. Hemen örneklerimize bakalım.
"""

print("Ocak\tMart\tŞubat")
print("a\t\t\t\t\tb")

"""
type() fonksiyonu
print() fonksiyonundan bahsetmişken type() fonksiyonunu öğrenmekte fayda var. type() fonksiyonu içine gönderilen değerin hangi veri tipinden olduğunu söyler.
"""

# Integer (Tamsayı) türü
a = 65
print(type(a))

# Float (Ondalıklı Sayı) türü
a = 5.87
print(type(a))

# String (Karakter Dizisi) türü
a = "Murat"
print(type(a))

"""
sep parametresi
print() fonksiyonunda kullanılabilen sep parametresi yazdırdığımız değerlerin arasına istediğimiz karakterlerin yerleştirilmesini sağlar.
"""

print(3,4,5,6,7,8,9)

# sep parametresi sayesinde değerlerin arasına nokta konuyor.
print(3,4,5,6,7,8,9,sep = ".")

# Değerlerin arasında "/" sembolü yerleştiriliyor.
print("06","04","2015",sep = "/")

print("Mustafa","Murat","Coşkun",sep = "\n")

"""
Yıldızlı Parametreler
Eğer bir stringin başına * işareti koyup, print fonksiyonuna gönderirsek bu string karakterlerine ayrılacak ve her bir karakter ayrı birer string olarak davranılarak ekrana basılacaktır.
"""

# Varsayılan olarak karakterlerin arasına boşluk konuluyor.
print(*"Hakan")

print(*"Hakan",sep = "\t")
