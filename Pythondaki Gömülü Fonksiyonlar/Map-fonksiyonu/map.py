"""
Map Fonksiyonu
Bu konuyla beraber Pythonda gömülü olan bazı fonksiyonlarımızı öğrenmeye başlıyoruz.

Pythonda gömülü bir fonksiyon olan *map()* fonksiyonunun yapısı şu şekildedir.

                map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb),....)

map() fonksiyonu ilk parametre olarak bir tane fonksiyon objesi alır. 
(Fonksiyonlar da birer obje olduğu için başka bir fonksiyona gönderilebilir.)
2. parametre olarak da bir tane iterasyon yapılacak veritipi alarak , gönderilen fonksiyonu 
her bir eleman üzerinde uygulayarak sonuçları bir *map* objesi olarak döner. 
Örneklerimize geçersek bu fonksiyonun işlevini daha iyi anlayacağız.
"""

def double(x):
    return x * 2

map(double,[1,2,3,4,5,6,7])   # fonksiyon bir tane argüman alıyor ve listenin her bir elemanı üzerinde uygulanıyor.

b = list(map(double,[1,2,3,4,5,6,7]))
print(b)

c = list(map(double,(1,2,3,4,5,6,7)))
print(c)
print(*"---")

"""
Buradaki fonksiyonları lambda ifadeleriyle de yazabiliriz.
"""

map(lambda x : x ** 2, [1,2,3,4,5,6,7])

d = list(map(lambda x : x ** 2, [1,2,3,4,5,6,7]))
print(d)

# Map fonksiyonu birden fazla liste veya demet alabilir.

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

map(lambda x,y : x * y, liste1,liste2)

e = list(map(lambda x,y : x * y , liste1,liste2))
print(e)

f = list(map(lambda x,y,z : x * y * z , liste1,liste2,liste3))
print(f)