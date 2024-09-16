"""
Nesne Tabanlı Programlama - Sınıflar
Bu konuda artık kendi veri tiplerimizi ve objelerimizi üretmeye başlayacağız.

Kendi veri tiplerimizi oluşturmak ve bu veri tiplerinden objeler üretmemiz için öncelikle objeleri üreteceğimiz yapıyı tanımlamamız gerekiyor. 
Bunu tasarladığımız yapıya da sınıf veya ingilizce ismiyle class diyoruz. Şimdi class yapılarını öğrenerek konumuza başlayalım.
"""

"""
Class Anahtar Kelimesi
Sınıflar veya Classlar objelerimizi oluştururken objelerin özelliklerini ve metodlarını tanımladığımız bir yapıdır ve biz herbir objeyi bu yapıya göre üretiriz. 
İsterseniz bir Araba classı tanımlayarak yapımızı kurmaya başlayalım.
"""
# Yeni bir Araba veri tipi oluşturalım
class Araba():
    model = "Renault Megane"
    renk = "Gümüş"              # Sınıfımızın özellikleri (attributes)
    beygir_gucu = 110
    silindir = 4

"""
Sınıfımızı Pythonda tanımladık. Peki bu sınıftan obje nasıl oluşturacağız ? Bunu da şu şekilde yapabiliyoruz.

----------------------------------------------------------------------------------------------------------------------------

     obje_ismi = Sınıf_İsmi(parametreler(opsiyonel))

----------------------------------------------------------------------------------------------------------------------------
"""
araba1 = Araba()  # Araba veri tipinden bir "araba1" isminde bir obje oluşturduk.
# print(araba1)  # Objemizin veri tipi Araba
# print(type(araba1))

"""
araba1 objesi artık sınıfta tanımladığımız bütün özelliklere (attributes) sahip olmuş oldu. İşte sınıf ve obje üretmek bu şekilde olmaktadır. Peki bu araba objesinin özelliklerinin nasıl görebiliriz ?

--------------------------------------------------------------------------------------------------------------------------

        obje_ismi.özellik_ismi
--------------------------------------------------------------------------------------------------------------------------
"""
print(*"-----")
print(araba1.model)
print(araba1.renk)
print(araba1.beygir_gucu)
print(araba1.silindir)
print(*"-----")

"""
Şimdi de başka bir Araba objesi oluşturalım.
"""

araba2 = Araba()
print(araba2.model)
print(araba1.renk)
print(araba1.beygir_gucu)
print(araba1.silindir)
print(*"-----")

"""
Burda gördüğümüz gibi oluşturduğumuz objelerin buradaki model,renk vs. gibi özelliklerinin değeri aynıdır. 
Çünkü aslında burada tanımladığımız özellikler birer sınıf özelliğidir. Yani biz bir obje oluşturduğumuzda bu özelliklerin değerleri varsayılan olarak gelir. 
Bu özelliklerin değerlerine , herhangi bir obje oluşturmadan da erişebiliriz. Bunu da şu şekilde yapabiliriz.
"""
print(Araba.renk)   # Class_ismi.Özellik_ismi
print(Araba.beygir_gucu)

print(*"-----")

"""
Bizim her bir objeyi başlangıçta farklı değerlerle oluşturmamız için her bir objeyi oluştururken objelerin değerlerini göndermemiz gerekiyor. 
Bunun için de özel bir metodu kullanmamız gerekmektedir. 

------------------------------------------- init() -----------------------------------

Peki bu metod ne anlama geliyor ? İsterseniz ilk olarak *dir()* fonksiyonu yardımıyla araba1 objemizde neler var bakalım.
"""
"""
Python kendisi bunları varsayılan tanımlıyor. 
Burada aynı zamanda init metodunu da görüyoruz. 
Eğer biz bu metodu kendimiz tanımlarsak objelerimizi farklı değerlerle başlatabiliriz.
"""
"""
Aslında init metodu Pythonda yapıcı(constructor ) fonksiyon olarak tanımlanmaktadır. 
Bu metod objelerimiz oluşturulurken otomatik olarak ilk çağrılan fonksiyondur. 
Bu metodu özel olarak tanımlayarak objelerimizi farklı değerlerle oluşturabiliriz.
"""
# Araba veri tipi

class Araba():
    # Şimdilik class özelliklerine ihtiyacımız yok.

    def __init__(self):
        print("init fonksiyonu çağırıldı.")

araba1 = Araba() # araba1 objesi oluşurken otomatik olarak __init__ metodumuz çağrılıyor.
print(*"-----")

"""
Peki burada self ne anlama geliyor ?
self anahtar kelimesi objeyi oluşturduğumuz zaman o objeyi gösteren bir referanstır ve metodlarımızda en başta bulunması gereken bir parametredir.
Yani biz bir objenin bütün özelliklerini ve metodlarını bu referans üzerinden kullanabiliriz.
"""
"""
Objeler oluşturulurken, Python bu referansı metodlara otomatik olarak kendisi gönderir.
Özel olarak self referansını göndermemize gerek yoktur.
init metodunu ve self'i iyi anlamak için objelerimize özellikler ekleyelim.
"""

class Araba():
    def __init__(self,model,renk,beygir_gücü,silindir): # Parametrelerimizin değerlerini objelerimizi oluştururken göndereceğiz.
        self.model =  model # self.özellik_ismi = parametre değeri şeklinde objemizin model özelliğine değeri atıyoruz.
        self.renk = renk # self.özellik_ismi = parametre değeri şeklinde objemizin renk özelliğine değeri atıyoruz.
        self.beygir_gücü = beygir_gücü # self.özellik_ismi = parametre değeri şeklinde objemizin beygir_gücü özelliğine değeri atıyoruz.
        self.silindir = silindir # self.özellik_ismi = parametre değeri şeklinde objemizin silndir özelliğine değeri atıyoruz.

# araba1 objesini oluşturalım.
# Artık değerlerimizi göndererek objelerimizin özelliklerini istediğimiz değerle başlatabiliriz.
araba1 = Araba("Peugeot 301","Beyaz",90,4)

# araba2 objesini oluşturalım.
araba2 = Araba("Renault Megane","Gümüş",110,4)

print(araba1.model)
print(araba1.renk)
print(araba2.model)
print(araba2.renk)
print(*"-------")

"""
İstersek init metodunu varsayılan değerlerle de yazabiliriz.
"""

class Araba():
    def __init__(self , model = "Bilgi Yok",renk = "Bilgi Yok",beygir_gücü = 75 ,silindir = 4): 
        self.model =  model 
        self.renk = renk 
        self.beygir_gücü = beygir_gücü 
        self.silindir = silindir

araba1 = Araba(beygir_gücü=85, renk= "Sİyah")
print(araba1.renk)
print(araba1.model)