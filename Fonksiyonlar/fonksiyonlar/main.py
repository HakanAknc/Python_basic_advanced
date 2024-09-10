"""
Fonksiyonlar
Bu derste fonksiyonların ne olduğunu , bir fonksiyonun nasıl tanımlanacağını ve nasıl kullanılacağını öğrenmeye çalışacağız.

Fonksiyonlar programlamada belli işlevleri olan ve tekrar tekrar kullandığımız yapılardır. 
Örneğin kursumuzun başlarından beri kullandığımız print() fonksiyonunun görevi içine gönderdiğimiz değerleri ekrana yazdırdırmaktır. 
Bu fonksiyon Python geliştiricileri tarafından bir defa yazılmış ve biz de bu fonksiyonu programlarımızın değişik yerlerinde tekrar tekrar kullanıyoruz. 
İşte fonksiyonların kullanım amacı tam olarak budur. Fonksiyonlar bir defa tanımlanır ve programlarda ihtiyacımız olduğu zaman kullanırız. 
Ayrıca fonksiyonlar kod tekrarını engeller ve kodlarımız daha derli toplu durur.

İsterseniz şimdi de fonksiyonların ne olduğunu gerçek hayattan benzetme yaparak anlamaya çalışalım. 
Örneğin evimize bir adet katı meyve sıkacağı alıyoruz ve canımız ne zaman meyve suyu isterse bu aleti kullanıyoruz. 
Yani aslında bu aletin görevi ve fonksiyonu meyve suyu hazırlamaktır.

Python geliştiricilerin yazdığı fonksiyonlara yani bizim hazır kullandığımız fonksiyonlara(print(),type() vs.) 
gömülü fonksiyonlar(built-in function) denilmektedir.Ancak bunlardan hariç olarak biz kendi özel fonksiyonlarımızı(user-defined functions) da tanımlayabiliriz.

Peki biz kendi fonksiyonlarımızı nasıl tanımlayacağız ? İsterseniz şimdi yavaştan fonksiyonların nasıl tanımlanacağını öğrenelim.
"""
"""
Fonksiyonların Tanımlanması
Fonksiyon tanımlamanın yapısı şu şekildedir;

        def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
            # Fonksiyon bloğu
            Yapılacak işlemler
            # dönüş değeri - Opsiyonel

İsterseniz şimdi bir tane "selamla" isimli bir fonksiyon tanımlayalım.
"""

def selamle():
    print("Selam arkadaşlar...")
    print("Nasılsınız..")

# print(type(selamle))

"""
Fonksiyonların Kullanılması veya Çağrılması (Function Call)
Tanımlanan bir fonksiyonun kullanılmasına programlama dillerinde Fonksiyon Çağrısı denmektedir.
 O halde selamla fonksiyonumuzu nasıl çağıracağımızı öğrenelim. Fonksiyon çağrısı şu şekilde yapılabilmektedir;

        fonksiyon_adı(Argüman1,Argüman2....)
İsterseniz şimdi selamla fonksiyonumuzu çağıralım.
"""

selamle() # Fonksiyon parametre almadığında içine argümanlarımızı göndermiyoruz.

print(*"-----------")

"""
Burada gördüğünüz gibi, fonksiyonumuz çağrıldığı zaman, kendi bloğundaki işleri yaptı ve ekrana 2 tane değer yazdırdı.
 Bu fonksiyonu istediğimiz yerde tekrar tekrar çağırabiliriz.
"""
selamle()
selamle()
selamle()
selamle()
print(*"-----------")
print(*"-----------")

"""
Parametreler ve Argümanlar
Biliyorsunuz biz selamla fonksiyonunun içine herhangi bir değer göndermiyorduk ve fonksiyonumuz hep aynı işi yapıyordu. 
Ancak çoğu zaman fonksiyonlarımız içine gönderdiğimiz değerlerle farklı işlemler yaparlar. Örneğin katı meyve sıkacağına eğer "Elma" verirsek elma suyu, "Nar" verirsek nar suyu hazırlayacaktır.
 Fonksiyonlarda da Parametreleri bu şekilde düşünebilirsiniz. 
İsterseniz şimdi selamlama fonksiyonumuzu bir tane parametre alacak şekilde tanımlayalım.
"""

def selamla(isim):  # isim değişkenimiz burada parametre olmaktadır
    print("Merhaba",isim)

selamla("Hakan")  # "Hakan" değeri burada  argüman olmaktadır. 
selamla("Caner")  # "Caner" değeri burada  argüman olmaktadır.
print(*"-----------")
print(*"-----------")

"""
Bizim fonksiyon tanımlarken tanımladığımız herbir değişken birer Parametre , fonksiyon çağrısı yaptığımız zaman içine gönderdiğimiz değerler ise Argüman olmaktadır.
"""

def toplama(a,b,c):
    print("Toplam:",a+b+c)

toplama(5,8,2)
toplama(10,15,20)
toplama(101,102,50)
print(*"-----------")
print(*"-----------")

# Faktoriyel hesaplama
def faktoriyel(sayi):
    faktoriyel = 1
    if (sayi == 0 or sayi == 1):
        print("Faktoriyel",faktoriyel)
    else:
        while (sayi >= 1):
            faktoriyel *= sayi  # faktoriyel = faktoriyel * sayi
            sayi -= 1           # sayi = sayi -1
        print("Faktoriyel", faktoriyel)

faktoriyel(3)
faktoriyel(1)