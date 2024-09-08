"""
While Döngüleri
Bu bölümde while döngülerinin yapısını ve nasıl kullanılacağını öğrenmeye çalışacağız.

while döngüleri belli bir koşul sağlandığı sürece bloğundaki işlemleri gerçekleştirmeye devam eder. 
while döngülerinin sona ermesi için koşul durumunun bir süre sonra False olması gereklidir.Yapısı şu şekildedir;
while (koşul):
            İşlem1
            İşlem2
            İşlem3
               .
               .
while döngülerini daha iyi anlamak için örneklerimize bakalım.
"""

# Döngüde i değerlerini ekrana yazdırma

i = 0
while (i < 10):   # son değeri ekrana yaznaz
    print("i'nin değeri",i)
    i += 1  # Koşulun bir süre sonra False olması için gerekli - Unutma

print(*"----------------")

h = 0
while (h < 5):
    print("h'nin değeri",h)
    h += 1

print(*"----------------")

i = 0
while (i < 20):
    print("i nin değeri",i)
    i += 2  # Koşulunun bir süre sonra False olması için gerekli

print(*"----------------")

# Ekrana 25 defa "Python Öğreniyorum" yazdıralım.

i = 0

while (i < 25):
    print("Python Öğreniyorum..")
    i += 1
    
print(*"----------------")

# Liste üzerinde indeks ile gezinme
liste = [1,2,3,4,5,6]

a = 0

while (a < (len(liste))):
    print("Indeks: ",a,"Eleman: ",liste[a])
    a += 1

"""
Sonsuz Döngü Olayları
while döngüsü kullanırken biraz dikkatli olmamızda fayda var. Çünkü, while döngü koşulunun bir süre sonra False olması gerekecek ki döngümüz sonlanabilsin. 
Ancak eğer biz while döngülerinde bu durumu unutursak , döngümüz sonsuza kadar çalışacaktır. Biz buna sonsuz döngü olayı diyoruz. Örneğimize bakalım
"""
print(*"----------------")
print(*"----------------")

# Bu kodu çaıştırmayalım. Jupyter sıkıntı çıkarabilir :)
i = 0 
while (i < 10):
    print(i)
    # i değişkenini artırma işlemi yapmadığımız için i değişkeninin değeri sürekli 0 kalıyor 
    # ve döngü koşulu sürekli True kalıyor.
    