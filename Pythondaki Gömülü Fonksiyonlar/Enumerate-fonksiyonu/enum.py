"""
Enumerate Fonksiyonu
Bu konuda enumerate fonksiyonunu öğrenmeye çalışacağız. *enumerate* fonksiyonunu daha iyi anlamak için 
ilk önce şu örneğe bakalım.
"""

liste = ["Elma","Armut","Muz","Kiraz"]

# sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.

sonuç = list()

i = 0

for a in liste:
    
    sonuç.append((i,a))
    i +=1
print(sonuç)


"""
Yani aslında burada herbir elemanı indekslerle numaralandırıyor ve demet çiftleri oluşturuyoruz. *for döngüsü* yazarken bazen hem elemanları hem de indeksleri almak isteyebiliriz. 
Böyle bir durumda numaralandırma işlemi yapan *enumerate* fonksiyonunu kullanabiliriz.
"""

liste = ["Elma","Armut","Muz","Kiraz"]
c = list(enumerate(liste))
print(c)


liste = ["a","b","c","d","e","f","g"]

for index,eleman in enumerate(liste):
    if (index % 2 == 0):
        print("Eleman: ",eleman)