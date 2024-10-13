
#  ! 1. Matematiksel Fonksiyonlar

# * abs(x) Bir sayının mutlak değerini döndürür.
print(abs(-5))

# * round(x, n) Bir sayıyı belirli bir basamak sayısına yuvarlar
print(round(3.14159, 2))


# * sum(iterable) İteratif bir veri yapısındaki elemanların toplamını hesaplar.
print(sum([1,2,3]))


# ! 2. Tür Dönüştürme Fonksiyonları

# * int(x): Bir değeri tamsayıya çevirir
print(int(3.9))

# * float(x): Bir değeri ondalıklı sayıya çevirir.
print(float(6))

# * str(x): Bir değeri string (metin) tipine çevirir.
print(str(123))


# ! 3. Veri Yapıları ve İterasyon Fonksiyonları

# * len(s): Bir veri yapısındaki eleman sayısını döndürür.
print(len([1, 2, 3]))  # Çıktı: 3

# * range(start, stop, step): Belirli bir aralıkta sayılar üretir.
for i in range(1, 5):
    print(i)

# * sorted(iterable): Bir veri yapısını sıralı bir liste halinde döndürür.
print(sorted([3, 1, 2]))


# ! 4. Girdi ve Çıktı Fonksiyonları

# * print(): Konsola çıktı yazdırır.
print("Merhaba Dünya!")

# * input(): Kullanıcıdan veri alır.
isim = input("Adınız nedir? ")
print("Merhaba ",isim)


# ! 5. İteratif Fonksiyonlar

# * map(function, iterable): Bir fonksiyonu, bir veri yapısının her elemanına uygular ve yeni bir iterable döndürür.

sayilar = [1, 2, 3]
kareler = list(map(lambda x: x ** 2, sayilar))
print(kareler)  # Çıktı: [1, 4, 9]

# * filter(function, iterable): Bir fonksiyona göre elemanları filtreler.

sayilar = [1, 2, 3, 4]
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print(ciftler)  # Çıktı: [2, 4]


# ! 6. Genel Kullanım Fonksiyonları

# * type(x): Bir nesnenin türünü döndürür.

print(type(5))  # Çıktı: <class 'int'>

# * isinstance(obj, class): Bir nesnenin belirli bir sınıfa ait olup olmadığını kontrol eder.

print(isinstance(5, int))  # Çıktı: True


# ! 7. Herhangi Bir Şeye Erişim

# * dir(object): Bir nesnenin niteliklerini ve metodlarını listeler.

print(dir([]))  # Listeyle ilgili metodları gösterir

# * help(object): Bir nesneyle ilgili belgeleri ve açıklamaları verir.

help(str)  # str sınıfıyla ilgili açıklamaları gösterir
