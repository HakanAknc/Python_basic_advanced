"""
Filter Fonksiyonu
Bu konuda filter fonksiyonunu öğrenmeye çalışacağız.

                filter(fonksiyon,iterasyon yapılabilen bir veritipi(liste vb.))

filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen (True , False) bir fonksiyon alır ve liste
 gibi veritiplerinin her bir elemanına bu fonksiyonunu uygular. *filter* sadece True sonuç çıkaran değerleri alarak 
 bir tane *filter* objesi döner. Hemen örneklerimize bakalım.
"""

filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])

a = list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))  # Çift olan sayılar
print(a)

def asala_mi(x):
    i = 2
    if (x == 1):
        return False  # Asal değildir
    elif (x == 2):
        return True  # Asal sayıdır
    else:
        while(i < x):
            if (x % i == 0):
                return False   # Asal Değil
            i += 1
        return True
    
print(asala_mi(34))
print(asala_mi(2))
print(asala_mi(1))
print(asala_mi(3))
print(asala_mi(4))
print(*"----")

filter(asala_mi,range(1,100))
b = list(filter(asala_mi,range(1,100)))  # 1'den 100'e kadar olan asal sayılar.
print(b)
