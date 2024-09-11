"""
Lambda İfadeleri
Bu konuda lambda ifadelerini(expression) öğrenmeye çalışacağız. lambda ifadeleri fonksiyonlarımızı oluşturmak için 
Pythonda bulunan pratik bir yöntemdir ve gerektiği yerlerde bu ifadeleri kullanabiliriz.
Biliyorsunuz listelerimizi oluşturmak için List Comprehension yöntemini kullanabiliyorduk. 
İsterseniz List Comprehension yöntemini hatırlayalım.
"""

liste1 = [1,2,3,4,5] 
liste2 = list()
for i in liste1: # Bu klasik liste oluşturma yöntemi
    liste2.append(i*2)
print(liste2)

print(*"-------")

liste3 = [1,2,3,4,5]
liste4 = [i * 2 for i in liste3] # List Comprehension
print(liste4)

print(*"-------")


"""
Aynı buradaki gibi bir fonksiyonu da tek satır halinde lambda ifadeleriyle oluşturabiliriz.
İlk önce yapısına bakalım sonra örneklerimize geçelim.

                etiket = lambda parametre1,parametre2.... :  İşlem

Bu yapıdan henüz bir şey anlamamış olabiliriz. İsterseniz örneklerimizle *lambda ifadelerini* anlamaya çalışalım. 
Bir tane iki ile çarpma görevini yerine getiren fonksiyon yazalım.
"""
def ikiylecarp(x):   # Klasik fonksiyon tanımlama
    return x * 2

print(ikiylecarp(2))

print(*"-------")
print(*"-------")

# Şimdi de bu fonksiyonu lambda ifadelerini kullanarak tek satırda yazalım.

ikiylecarp = lambda x : x * 2 # x parametre x* 2 return ifadesi ve ikiyleçarp değeri de bir etikettir(değişken gibi düşünelim)
print(ikiylecarp(3)) # Buradaki 3 argümanı lambda ifadesindeki x'in yerine geçiyor.

print(*"-------")

def toplama(a,b,c):
    return a + b + c

print(toplama(3,4,5))

print(*"-------")

topla = lambda x,y,z : x + y + z
print(topla(3,2,65))

print(*"-------")

# Stringi ters çevirme
def terscevir(s):
    return s[::-1]

print(terscevir("Python Programlama"))

print(*"-------")

ters =  lambda s : s[::-1]
print(ters("Python Programlama"))

print(*"-------")

# çift mi 

def çiftmi(sayı):
    return ( sayı % 2 == 0 )
    
print(çiftmi(12))
print(çiftmi(13))

print(*"-------")

çifttek = lambda sayı :  sayı % 2 == 0 

print(çifttek(34))
print(çifttek(13))