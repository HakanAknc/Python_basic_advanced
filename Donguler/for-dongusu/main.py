"""
For Döngüleri
Bu konuda Pythondaki for döngülerinin yapısını ve for döngülerinin kullanım alanlarını öğreneceğiz.
 Ancak ondan önce , Pythondaki in operatörünü öğrenmeye çalışalım.
"""
"""
in Operatörü
Pythondaki in operatörü , bir elemanın başka bir listede,demette veya stringte (karakter dizileri) bulunup bulunmadığını 
kontrol eder. Kullanımı şu şekildedir;
"""

print("a" in "Merhaba")    # "a" harfi içinde var mı "Merhaba" 'nın
print("mer" in "merhaba")
print("t" in "merhaba")
print(4 in [1,2,3,4])
print(10 in [1,2,3,4])
print(4 in (1,2,3))
print(*"--------")

"""
for Döngüsü
for Döngüsü , listelerin ,demetlerin, stringlerin ve hatta sözlüklerin üzerinde dolaşmamızı sağlayan bir döngü türüdür. 
Yapısı şu şekildedir.

        for eleman in veri_yapısı(liste,demet vs):
            Yapılacak İşlemler

Bu yapı bize şunu söyler;

        eleman değişkeni her döngünün başında listenin,demetin vs. her bir elemanına eşit olacak ve her döngüde 
        bu elemanla işlem yapılacak.

for döngüsünü daha iyi anlamak için örneklerimize bakalım.
"""
# Listeler Üzerinde Gezinmek

liste = [1,2,3,4,5,6,7,]

for eleman in liste:
    print("Eleman -", eleman)

print(*"--------")

# Liste elemanlarını toplama
liste1 = [1,2,3,4,5,6,7]
toplam = 0
for eleman1 in liste1:
    toplam += eleman1
print("Toplam = ", toplam)

print(*"--------")

# Çift elemanları bastırma
liste2 =[1,2,3,4,5,6,7,8,9]

for eleman2 in liste2:
    if eleman2 % 2 == 0:
        print(eleman2)

print(*"--------")

# Karakter Dizileri Üzerinde Gezinmek (Stringler)
s = "Python"
for karekter in s:
    print(karekter)

print(*"--------")

# Her bir karakterleri 3 ile çarpma

s = "Python"

for karekter1 in s:
    print(karekter1 * 3)

# Demetler üzerinde gezinmek (Demetler)
# Listelerle aynı mantık
demet =  (1,2,3,4,5,6,7)

for eleman in demet:
    print(eleman)

print(*"--------")

"""
Demetlerin üzerinde for döngüsü uygularken aslında çok pratik bir yöntem bulunuyor. 
Aşağıdaki örneğe bakalım.
"""
# Listelerin için 2 boyutlu demetler

liste = [(1,2),(3,4),(5,6),(7,8)]

for eleman in liste:
    print(eleman) # Herbir elemanın  demet olduğu görebiliyoruz.

print(*"--------")

# Demet içindeki herbir elemanı almak için pratik yöntem
liste = [(1,2),(3,4),(5,6),(7,8)]

for (i,j) in liste:
    print(i,j)

print(*"--------")

# Demet içindeki elemanları çarpalım.
liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for (i,j,k) in liste:
    print(i * j * k)

print(*"--------")

"""
Sözlükler üzerinde gezinmek (Dictionary)

Hatırlarsanız, sözlükler konusunda 3 adet metod görmüştük. (keys(),values(),items()*).
 İsterseniz bunları burada hatırlayalım.
"""

sözlük = {"bir":1, "iki":2, "üç":3, "dört":4}
print(sözlük.keys())
print(sözlük.values())
print(sözlük.items())

"""
Python sonuçları dict_keys,dict_values,dict_items olarak vermesine rağmen , bunlar üzerinde liste veya demet 
üzerinde gezinir gibi for döngüsüyle gezinebiliriz.
"""

print(*"--------")

# Metodları kullanmadan sözlük üzerinde gezinmek - Sadece anahtarları alabiliyoruz.
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük:
    print(eleman)

print(*"--------")

#  keys() - Aynı şey
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük.keys():
    print(eleman)

print(*"--------")

# values() 
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük.values():
    print(eleman)

print(*"--------")

# items() 
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for (i,j) in sözlük.items():
    print("Anahtar:",i,"Değer:",j)