"""
Dosya Okuma İşlemleri
Bu derste dosya okuma işlemlerini görmeye çalışacağız.

Dosyaları okumak ve verileri almak için "r" kipiyle açmamız gerekiyor. 
"r" kipiyle açtığımız dosya eğer bulunmuyorsa "FileNotFoundError" hatası dönecektir. 
Şimdi bulunduğumuz dizinde bulunan "bilgiler.txt" dosyasını açalım.
"""

# file = open("bilgiler.txt","r", encoding="utf-8")
# file.close()

# file = open("bilgiler2.txt","r",encoding="utf-8")  # böyle bir dosya yok . O yüzden FileNotFoundError hatası döndü.

try:
    file = open("bilgiler2.txt","r",encoding="utf-8")
except FileNotFoundError:
    print("Dosya bulunamadı....")

print(*"----------")

"""
Peki bir dosyanın içinden bilgileri nasıl okuyacağız ? Bunun için Pythonda değişik yöntemler bulunuyor. 
İsterseniz bu yöntemleri tek tek görmeye çalışalı
"""

"""
For döngüsü ile okuma
Şöyle bir kullanım dosyamızdaki herbir satırı tek tek okuyacaktır.
"""
file = open("bilgiler.txt","r",encoding="utf-8") # Dosyayı okuma kipiyle açıyoruz. Türkçe karaktere dikkat.

for i in file: # Tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
    print(i)  # Her bir satırı ekrana basıyoruz.
file.close()

"""
Burada her bir satırımız boşluklu yazıldı. 
Bunun nedeni, hem her satır sonunda "\n" karakterinin olması hem de print fonksiyonun bir alt satıra geçmek için 
boşluk bırakmasıdır. Bunu önlemek için varsayılan değer olarak "\n" karakteri alan *end* parametresine 
kendimiz değer verebiliriz.
"""
file = open("bilgiler.txt","r",encoding= "utf-8") # Dosyayı okuma kipiyle açıyoruz. Türkçe karaktere dikkat.

for i in file: # Tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
    print(i,end = "") # Her bir satırı ekrana basıyoruz. end parametresi \n yerine boşluk alacak.
file.close()

"""
read() fonksiyonu
read() fonksiyonu eğer içine hiçbir değer vermezsek bütün dosyamızı okuyacaktır.

read() fonksiyonuna değer vererek belli bir kısmı okumayı bir sonraki dersimizde görmeye çalışsak daha doğru olur.
"""

file = open("bilgiler.txt","r",encoding="utf-8")

icerik = file.read() 

print("Dosya İçeriği:\n",icerik,sep ="")

file.close()

"""
read() fonksiyonuyla bir dosyayı okuduğumuzda dosya imlecimiz dosyanın en sonuna gider ve read() fonksiyonu 2. okuma da artık boş string döner.
"""

file = open("bilgiler.txt","r",encoding="utf-8")

icerik = file.read() 

print("1. Okuma : Dosya İçeriği:\n",icerik,sep ="")

icerik2 = file.read()


print("2. Okuma : Dosya İçeriği:\n",icerik2,sep ="")

file.close()

"""
readline() fonksiyonu
readline() fonksiyonu her çağrıldığında dosyanın sadece bir satırını okur.
 Her seferinde dosya imlecimiz (file) bir satır atlayarak devam eder.
"""

file = open("bilgiler.txt","r",encoding="utf-8")
print(file.readline())


print(file.readline()) # Okuyacak herhangi bir şey kalmayınca readline fonksiyonu boş string döner.
file.close()

"""
readlines() fonksiyonu
readlines() fonksiyonu dosyanın bütün satırları bir liste şeklinde döner.
"""

file = open("bilgiler.txt","r",encoding="utf-8")
file.readlines()
file.close()