"""
Koşullu Durumlar - if-else koşullu durumları
Şimdiye kadar Pythondaki temel veritiplerini öğrendik ve gerekli temelleri aldık. 
Artık bundan sonra çok daha eğlenceli konular göreceğiz ve elle tutulur programlar yazmaya başlayacağız. 
Bu konuda ilk olarak Python programlarının çalışma mantığını göreceğiz ve daha sonrasında koşullu durumları anlamaya çalışacağız.
"""

"""
Python Programlarının çalışma mantığı
Python programları çalışmaya başladığı zaman kodlarımız yukardan başlayarak teker teker çalıştırılır ve çalıştıracak kod kalmayınca programımız sona erer. 
Şöyle bir örneği düşünelim;
"""
a = 2
b = 3
c = 4
print(a+b+c)
print(*"--------------")

"""
Yukarıdaki basit kodda program teker teker her bir satırı ve ifadeyi çalıştırır ve çalıştıracak kod kalmayınca program sona erer.
Ancak Python'da her program bu kadar basit olmayabilir. 
Çoğu zaman Python programlarımız belirli bloklardan oluşur ve bu bloklar her zaman çalışmak zorunda olmaz.
Peki bu bloklar nasıl tanımlanır ? Pythonda bir blok tanımlama işlemi Girintiler sayesinde olmaktadır. 
Örnek olması açısından, Pythonda bloklar şu şekilde oluşabilir
"""

a = 2 # Blok 1 'e ait kod

if (a == 2):
    print(a) # Blok 2'ye ait kod
print("Merhaba") # Blok 1 ' ait kod

print(*"--------------")

a = 2 # Blok 1 'e ait kod

if (a == 3):
    print(a) # Blok 2'ye ait kod
print("Merhaba") # Blok 1 ' ait kod

print(*"--------------")

# 18 yaş kontrolü
yas = int(input("Yaşınızı giriniz: "))

if (yas < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana girmezsiniz..")

print(*"--------------")

# Negatif mi değil mi ?
sayı = int(input("Sayı giriniz: "))

if (sayı < 0):
    print("Sayı negatiftir.")

print(*"--------------")
print(*"--------------")

# 18 yas kontrolü
yas = int(input("Yaşınızı giriniz: "))

if (yas < 18):
    # if bloğu -  Girinti ile sağlanıyor.
    print("Bu mekana giremezsiniz.")
else:
    print("Mekana hoşgeşdiniz.")