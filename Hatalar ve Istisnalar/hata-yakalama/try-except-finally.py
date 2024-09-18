"""
Hata Yakalama - try,except,finally
Bu konuda programlarımızda hata verebilecek kodları yakalayabildiğimiz try,except,finally bloklarını ve fonksiyonlarda kendi hatalarımızı nasıl fırlatacağımızı öğreneceğiz.
"""
"""
try , except blokları
try ,except bloklarının yapısı şu şekildedir;

                try:

                    Hata çıkarabilecek kodlar buraya yazılıyor.
                    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
                    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
                except Hata1:
                    Hata1 oluştuğunda burası çalışacak.
                except Hata2:
                    Hata2 oluştuğunda burası çalışacak.

                    //
                    //
                    //
Hemen try , except ile ilgili örneklerimize geçelim.
"""
# Örnek 1

# a = int("324234dsadsad") # Burası ValueError hatası veriyor.

try:

    a =  int("324234dsadsad") # Burası ValueError hatası veriyor.
    print("Program burada")
except:  # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu.")  # Burası çalışır.

print("Bloklar sona erdi.")
print(*"--------")

try:
    
    a =  int("324234") # Burası normal çalışıyor
    print("Program burada")
except ValueError: # Hatayı belirtirsek ValueError hatası bu kısma giriyor.
    print("Hata oluştu") # Hata olmadığı için çalışmadı.
    
print("Bloklar sona erdi")

print(*"----------")

# Örnek 2

# a = int("32434aaa")
# print(2 / 0)

try: 
    a = int(input("Sayı1: "))
    b = int(input("Sayı2: "))  # Hata burada oluşuyor. ValueError'a bloğuna giriyoruz. 
    print(a / b)   # Hata burada oluşuyor. ZeroDivisionError'a bloğuna giriyoruz.
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")

print(*"-----------")

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b) 
except (ValueError,ZeroDivisionError):
    print("ZeroDivision veya ValueError hatası")

print(*"-----------")
print(*"-----------")


"""
try,except,finally blokları
Bazen programlarımızda her durumda mutlaka çalışmasını istediğimiz kodlar bulunabilir.
Bunun için biz kendi try,except bloklarına ek olarak bir tane finally bloğu ekleyebiliriz. finally blokları hata olması veya olmaması durumunda mutlaka çalışacaktır. 
Yapısı şu şekildedir;

                try:

                    Hata çıkarabilecek kodlar buraya yazılıyor.
                    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
                    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
                except Hata1:
                    Hata1 oluştuğunda burası çalışacak.
                except Hata2:
                    Hata2 oluştuğunda burası çalışacak.

                    //
                    //
                    //
                finally:
                    Mutlaka çalışması gereken kodlar buraya yazılacak.
                    Bu blok her türlü çalışacak.


Hemen basit bir örnek yazalım.
"""

try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b) # Hata burada oluşuyor. ZeroDivisionError'a bloğuna giriyoruz.
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
finally:
    print("Her durumda çalışıyorum.")

print(*"-----------")
print(*"-----------")

"""
Hata fırlatmak
Bazen kendi yazdığımız fonksiyonlar yanlış kullanılırsa kendi hatalarımızı üretip Pythonda bu hataları fırlatabiliriz. Bunun içinde raise anahtar kelimesini kullanacağız. Hata fırlatma şu şekilde yapılabilmektedir;

            raise HataAdı(opsiyonel hata mesajı)
"""

def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen doğru bir input girin.")
    else:
        return s[::-1]

print(terscevir("Python"))  # Hata vermiyor.
# print(terscevir(12))


try:
    print(terscevir(12))
except ValueError:
    print("Fonksiyonda bir hata oluştu.")