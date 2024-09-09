"""
List Comprehension
Bu konuda listeleri üretmek ve oluşturmak Pythonda çok pratik bir yöntem olan "List Comprehension" konusunu öğreneceğiz.
Biliyorsunuz Pythonda birçok işimizi çok kısa kodlar halledebiliyoruz. 
Ancak kodları daha da kısaltmak ve pratik yöntemler kullanmak her zaman isteriz. 
Şimdi örneklerimizle list comprehension'ı anlamaya çalışalım.
"""

# Listelerdeki append metodunu hatırlayalım.
liste = [1,2,3,4]
liste.append(5)
liste.append(6)
print(liste)

print(*"----------------")

# liste1'den liste2'yi oluşturalım.

liste1 = [1,2,3,4,5]

liste2 = list() # veya liste2 = [] ikisi de boş liste oluşturur.


for i in liste1:
    liste2.append(i) # liste2 'ye liste1 in elemanları for döngüsü yardımıyla atıyoruz.
    
print(liste2)

print(*"----------------")
print(*"----------------")
"""
Acaba bu kodumuzu list comprehension ile daha kısa yazabilir miyiz ?
"""
liste1 = [1,2,3,4,5] # Örnek 1
liste2 = [i for i in liste1]  # List Comprehension
print(liste2)

print(*"----------------")

liste1 = [1,2,3,4,5] # Örnek 2
liste2 = [i*2 for i in liste1] # List Comprehension
print(liste2)

print(*"----------------")

liste1 = [(1,2),(3,4),(5,6)] # Örnek 3
liste2 = [i*j for (i,j) in liste1] # List Comprehension
print(liste2)

print(*"----------------")

liste1 = [1,2,3,4,5,6,7,8,9,10] # Örnek 4
liste2 = [i for i in liste1 if not (i == 4 or i == 9)] # List Comprehension
print(liste2)

print(*"----------------")

s = "Python"  # Örnek 5
liste = [i * 3 for i in s] # List Comprehension
print(liste)

print(*"----------------")

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]

# yeni_liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = list()
for i in liste:
    print(i) ## Buradaki i değeri de aslında bir liste.

print(*"----------------")

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = list()
for i in liste:
    for x in i:
        print("x:",x)
        liste2.append(x)
print(liste2)

print(*"----------------")

# List Comprehension 

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = [x for i in liste for x in i] # Biraz karmaşık
print(liste2)