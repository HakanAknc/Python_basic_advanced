"""
Nesne Tabanlı Programlama Mantığı
Bu konuyla beraber Nesne Tabanlı Programlamaya giriş yapıyoruz ve bu konuda biraz Nesne Tabanlı programlama hakkında konuşacağız. 
Nesne Tabanlı Programlama veya ingilizce ismiyle ** Object Oriented Programming** en basit anlamıyla gerçek hayatı programlamaya uyarlamak olarak düşünülebilir. 
Örneğin bir tane öğrenci otomasyon sistemi yazmak istiyoruz. Bunun için öğretmenleri , öğrencileri ve kursları aslında birer nesne olarak oluşturmamız gerekiyor. 
Böyle bir sistemi programlamayla gerçekleştirmek için aslında her bir nesnenin yapısını tanımlayıp, daha sonra bu yapılardan nesneler üretmemiz gerekiyor. 
İşte Nesne Tabanlı Programlama en basit anlamıyla bu şekildedir. Şimdi isterseniz obje veya nesne nedir anlamaya çalışalım.
"""
"""
Obje nedir ?
Etrafımıza baktığımızda aslında her bir eşyanın bir obje olduğunu görüyoruz. Örneğin bir tane televizyon kumandasını düşünelim.
 Bu kumandanın kendi içinde değişik özellikleri (attribute) ve fonksiyonları(metod) bulunuyor. 
Örneğin, kumandanın markası, tuşları aslında bu kumandanın özellikleridir(attribute).
Kumandanın kırmızı tuşuna bastığımızda televizyonun kapanması ve sesi kapatma tuşuna bastığımızda televizyonun sesinin kapanması bu kumandanın metodlarıdır. 
Bunun gibi Pythondaki aslında her şey bir objedir. Örneğin, listelere bakacak olursak bu liste objelerinin aslında birçok metodu ve özelliği bulunur.
"""
liste = [1,2,3,4,5]  # Liste objesi oluşturduk.

liste.append(6) # append metodu
print(liste)

# print(type(liste))

sozluk = dict()   # dictionary objesi
print(type(sozluk))

print(type((1,2,3,4))) # tuple objesi

def toplam(a,b):
    return a + b

print(type(toplam))  # Fonksiyon objesi