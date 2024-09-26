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