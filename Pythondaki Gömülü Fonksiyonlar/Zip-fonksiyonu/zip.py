"""
Zip Fonksiyonu
Bu konuda zip fonksiyonu öğrenmeye çalışacağız. *zip* fonksiyonunu öğrenmeden önceden liste elemanlarını 
gruplamaya çalışalım ve daha sonrasında *zip* fonksiyonunun faydasını görmeye çalışalım.
"""

liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10,11]

# sonucu [(1,6),(2,7),(3,8),(4,9),(5,10)] yapmaya çalışalım.

i = 0
sonuç = list()
while (i < len(liste1) and i < len(liste2)):
    sonuç.append((liste1[i],liste2[i]))
    
    i +=1
print(sonuç)

"""
Peki böyle uzun bir işlemi *zip* fonksiyonuyla nasıl yaparız ? İsterseniz *zip* fonksiyonunun kullanımını direk örnek üzerinden görelim.
"""

a = list(zip(liste1,liste2))
print(a)
print(*"---")

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = ["Python","Php","Java","Javascript","C"]

b = list(zip(liste1,liste2,liste3))
print(b)
print(*"---")

## Aynı anda iki liste üzerinde gezinmek
liste1 = [1,2,3,4]
liste2 = ["Python","Php","Java","Javascript"]

for i,j in zip(liste1,liste2):
    print("i:",i,"j:",j)
print(*"---")


# Sözlükleri zipleyelim.
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}

c = list(zip(sözlük1,sözlük2)) # Anahtarlar eşleşti.
print(c)