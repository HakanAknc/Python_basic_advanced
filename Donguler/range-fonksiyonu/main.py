"""
range() Fonksiyonu
Pythondaki bu hazır fonksiyon bizim verdiğimiz değerlere göre range isimli bir yapı oluşturur ve bu yapı listelere oldukça benzer. 
Bu yapı başlangıç, bitiş ve opsiyonel olarak artırma değeri alarak listelere benzeyen bir sayı dizisi oluşturur. 
Kullanımlarını öğrenmeye başlayalım.
"""

print(range(0,20)) # 0'dan 20' a kadar (dahil değil) sayı dizisi oluşturur.
print(*"-------------------------")
print(*range(0,20))  # Yazdırmak için başına "*" koymamız gerekiyor.
print(*"-------------------------")
liste = list(range(0,20))
print(liste)
print(*"-------------------------")
print(*range(5,10))
print(*"-------------------------")
print(*range(15))  # Başlangıç değeri vermediğimiz 0'dan başlar.
print(*"-------------------------")
print(*range(5,20,2)) # 5'ten 20'ye kadar olan sayıları 2 atlayarak oluşturur.
print(*"-------------------------")
print(*range(5,100,5)) # 5'ten 100'e kadar olan ve 5 ile bölünebilen sayılar.
print(*"-------------------------")
print(*range(20,0)) # 20'den geri gelen sayıları oluşturmaz.
print(*"-------------------------")
print(*range(20,0,-1)) # 20'den geri gelen sayıları oluşturur.
print(*"-------------------------")

"""
Şimdi de, range fonksiyonu ile oluşturduğumuz yapının üzerinde for döngüsü ile gezinelim.
"""

for sayı in range(0,10):
    print(sayı)

print(*"-------------------------")

for sayı in range(1,20):
    print("* " * sayı)