def selamla(isim):
    print("Selam",isim)

selamla("Hakan")
# selamla()  # Böyle bir kullanım hata verecektir.

print(*"----------")
"""
Ancak biz eğer bir parametrenin değerini varsayılan olarak belirlemek istersek, bunu varsayılan değerler ile yapabiliriz. 
"""
def selamla(isim = "İsimsiz"):
    print("Selam",isim)

selamla() # Hiç bir değer göndermedik. "isim" parametresinin değeri varsayılan olarak "İsimsiz" olarak belirlendi.
selamla("Evren")

print(*"----------")
"""
İşte bu kadar ! Peki birçok parametreye sahip olursak ne olacak ? Bir fonksiyon daha tanımlayalım
"""
def bilgilerigoster(ad = "Bilgim yok", soyad = "Bilgim yokk", numara = "Bilgim yokkk"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)

bilgilerigoster() # Bütün parametreler varsayılan değerle ekrana basılacak.
bilgilerigoster("Hakan","Akıncı")   # ad ve soyad değerini verdik ancak numara parametres

"""
Ancak böyle bir durumda argümanları gönderirken değerleri sıralı vermemiz gerekiyor. 
Peki sadece numara parametresine değer vermek istersek ne yapacağız ?
"""
bilgilerigoster(numara = "123456")  # numara parametresini özel olarak belirtiyoruz.
bilgilerigoster(ad = "Mustafa Murat",numara = "123456")

print(*"----------")

"""
Aslında biz varsayılan değerleri en başlarda görmüştük. 
print fonksiyonunun sep parametresini hatırlayalım.
"""
print("Mustafa","Murat","Coşkun") # sep parametresine değer vermeyince varsayılan olarak boşluk karakteri verildi.
print("Mustafa","Murat","Coşkun",sep = "/") # sep parametresine özel olarak değer atadık.
# help(print) # sep parametresine varsayılan olarak boşluk değeri verildiğini görebiliyoruz.

print(*"----------------")
print(*"----------------")

"""
Esnek Sayıda Değerler
Biliyorsunuz bir fonksiyon yazıldığında özel olarak kaç tane parametresi olacağını önceden belirtmemiz gerekiyor. 
Örneğin, bir toplama fonksiyonu yazalım.
"""
def toplama(a,b,c):
    print(a+b+c)

toplama(3,4,5)
# toplama(3,4,5,6) # 4 tane argüman veremeyiz.
# Eğer bu fonksiyonu 4 argüman alacak şekilde tanımlamak istersek, tekrardan tanımlamamız gerekiyor.

def toplama(a,b,c,d):
    print(a+b+c+d)

toplama(3,4,5,6) 
# toplama(3,4,5) # Ancak bu sefer de 3 argüman veremiyoruz.

print(*"----------------")
print(*"----------------")

"""
Peki ben bir fonksiyonu esnek sayıda argümanla kullanmak istersem ne yapacağım ? 
Bunun için de Yıldızlı Parametre kullanmam gerekiyor. 
Kullanımı şu şekildedir;
"""
def toplama(*parametreler): # Artık parametreler değişkenini bir demet gibi kullanabilirim.
    toplam =  0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam += i
    return toplam

print(toplama(3,4,5,6,7,8,9,10))
print(toplama())
print(toplama(1,2,3))

"""
print fonksiyonunu tekrar hatırlayacak olursak aslında print fonksiyonu bu şekilde tanımlanmış bir fonksiyondur. 
Çünkü biz print fonksiyonuna istediğimiz sayıda argüman gönderebiliyorduk.
"""
print(3,4,5,6)
print("Elma","Armut")
