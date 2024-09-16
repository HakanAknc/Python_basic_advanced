"""
Nesne Tabanlı Programlama - Özel Metodlar
Nesne tabanlı programlamada son olarak sınıfların özel metodlarını nasıl kendimiz yazarız öğrenmeye çalışalım. 
Özel metodlar, daha önceden de bahsettiğimiz gibi bizim özel olarak çağırmadığımız ancak her classa ait metodlardır. 
Bunların çoğu biz tanımlamasak bile Python tarafından varsayılan olarak tanımlanır. 
Ancak bu metodların bazılarını da özel olarak bizim tanımlamamız gerekmektedir. 
Daha önceden gördüğümüz init metodu bu metodlara bir örnektir. 
Bu konuda bu metodlarını nasıl tanımlayacağımızı öğrenmeye çalışacağız. 
Şimdi örneklerimize geçelim.
"""

class Kitap():
    pass

kitap1 = Kitap() # __init__ metodu çağrılıyor.

# len(kitap1) # __len__ metodu çağrılacak ancak tanımlı değil. Bunu özellikle bizim tanımlamamız gerekiyor.

# print(kitap1) # __str__ metodu çağrılır.

del kitap1 # del anahtar kelimesi bir objeyi siler ve __del__ metodu çağrılır. 

# print(kitap1)

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür

kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye") # Kendi metodumuz 

"""
str metodu
Normalde print(kitap1) ifadesi ekrana şöyle bir yazı yazdırıyor.
"""

# print(kitap1)
"""
Ancak eğer str metodunu kendimiz tanımlarsak artık ekrana kitap1 in içeriğini daha anlaşılır yazabileceğiz.
"""

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)

kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(kitap1)
