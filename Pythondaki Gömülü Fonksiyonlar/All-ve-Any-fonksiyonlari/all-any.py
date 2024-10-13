"""
All ve Any Fonksiyonları
Bu derste *all* ve *any* fonksiyonlarının kullanımlarını öğrenmeden şu işlemleri bu fonksiyonları kullanmadan nasıl yaparız öğrenmeye çalışalım.
"""

def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
# Bütün değerler True ise True en az birisi False ise False döndürmek istiyoruz.
liste = [True,False,True,False,True]

print(hepsi(liste))

liste = [1,2,3,4,5] # Daha önceden biliyoruz. 0' haricinde bütün sayılar True sayılmaktadır.

c = hepsi(liste) # Hepsi True
print(c)

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
# Herhangi bir değer True ise True, Hepsi False ise False döndürmek istiyoruz.

liste = [True,False,True,False,True]
b = herhangi(liste)
print(b)
print(*"-----------")
"""
Aslında bu işlemleri *all()* ve *any()* fonksiyonları yapmaktadır. İsterseniz bunların örneklerine bakalım.

*all() fonksiyonu* bütün değerler True ise True, en az bir değer False ise False sonuç döndürür.
"""

liste = [True,False,True,False,True]
print(all(liste))

liste = [1,2,3,4,5]
print(all(liste))

"""
*any() fonksiyonu* bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.
"""

liste = [True,False,True,False,True]

print(any(liste))

liste = [0,0,0,0,0,0,0]
print(any(liste))