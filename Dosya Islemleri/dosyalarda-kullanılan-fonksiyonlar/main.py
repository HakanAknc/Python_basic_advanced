file = open("hakan.txt", 'w', encoding='utf-8')
print(file.write("Hakan Akıncı Dosya İşlemlerini öğreniyor."))
file.close()


"""
Dosyalarda Kullanılan Fonksiyonlar
Bu derste dosya okuma işlemlerine devam edeceğiz ve dosyalarda kullanılan metodları öğrenmeye çalışacağız.
"""

"""
Dosyaları Otomatik Kapatma
Dosyalarda işlemlerimiz bittiği zaman dosyamızı kapatmamız gerektiğini biliyoruz. 
Ancak programlamacılık doğası gereği çoğu zaman dosyaları kapatmayı unutabiliriz. 
Bunun için Pythonda dosyalarda işimiz bitince otomatik kapatma özelliği bulunuyor. 
Bundan sonra Pythonda dosya işlemlerimizi şu blok içinde yapacağız.

                with open(dosya_adı,dosya_kipi) as file:
                    Dosya işlemleri
"""

with open("bilgiler.txt","r",encoding = "utf-8") as file:
    for i in file:
        print(i)


"""
Dosyaları İleri Geri Sarmak
Biliyorsunuz önceki dersimizde dosyaları okurken sadece dosyanın en başından başlayabiliyorduk ve dosya imlecimiz 
okuma işleminin sonunda , dosyanın en sonuna gidiyordu. 
Ancak biz çoğu zaman dosya imlecini (file) dosyanın herhangi bir yerine götürmek isteyebiliriz.
 Bunun için Pythondaki seek() fonksiyonunu kullanacağız.
 Ancak ondan önce dosya imlecinin hangi byteda olduğunu söyleyen tell() fonksiyonuna bakalım.
"""

with open("bilgiler.txt","r",encoding = "utf-8") as file:
    print(file.tell())

"""
Şu anda hiçbir işlem yapmadığımız için tell() fonksiyonu dosyanın en başında (0. byteda) olduğumuzu söyledi. 
Peki bir dosya imlecini dosyanın 20.byte'ına götürmek için ne yapacağız ? 
Bunun için de seek() fonksiyonunu kullanacağız.
"""

with open("bilgiler.txt","r",encoding = "utf-8") as file:
    file.seek(20) # 20.byte götürdük.
    print(file.tell())


"""
Peki biz bir dosyanın belirli bir byte'ına(karakter) gidip sadece belli sayıda karakteri nasıl okuyacağız ? 
Eğer biz read() fonksiyonuna bir sayı değeri verirsek sadece o sayı değeri kadar alanı okuyacaktır. Hemen görelim.
"""

with open("bilgiler.txt","r",encoding = "utf-8") as file:
    file.seek(5) # 5.byte gidiyoruz.
    icerik = file.read(10)  # 10 karakteri okuyoruz.
    print(icerik)
    print(file.tell())


with open("bilgiler.txt","r",encoding = "utf-8") as file:
    file.seek(5) # 5.byte gidiyoruz.
    icerik = file.read(10)  # 10 karakteri okuyoruz.
    print(icerik)
    file.seek(0)
    icerik2 = file.read(6)
    print(icerik2)