"""
Fonksiyonlarda Return
Bu konuda fonksiyonlardan değer döndürmemizi sağlayan return ifadesini görmeye çalışacağız. 
Önceki bölümde yazdığımız fonksiyonları hatırlayacak olursak, bu fonksiyonlar sadece ekrana print ile değer yazdırıyordu. 
Ancak bu fonksiyonlar yaptıklar işlemler bize herhangi bir değer vermiyorlardı. 
Ancak biz programlarımızda bir fonksiyon sonucunda elde edilen değerleri alıp programlarımızın bambaşka yerlerinde kullanmak isteyebiliriz. 
Bu derste bunu nasıl yapacağımızı öğrenmeye çalışacağız.
"""
"""
return ifadesi fonksiyonun işlemi bittikten sonra çağrıldığı yere değer döndürmesi anlamı taşır. 
Böylelikle, fonksiyonda aldığımız değeri bir değişkende depolayabilir ve değeri programın başka yerlerinde kullanabiliriz. 
Şimdi iki tane çok basit fonksiyon yazalım ve return neden gereklidir anlamaya çalışalım.
"""

# def toplama(a,b,c): # Birinci fonksiyon
#     print("Toplamları",a+b+c)

# def ikiyleçarp(a): # İkinci fonksiyon
#     print("2 ile çarpılmış hali", a * 2)

# toplam = toplama(3,4,5)
# # ikiyleçarp(toplam)
# print(type(toplam))

# print(*"-----------------")
# print(*"-----------------")

# def toplama1(a,b,c):
#     return a+b+c   # return'un kullanımı
# def ikiyle_carp(a):
#     return a*2

# toplam1 = toplama1(3,4,5)
# print(ikiyle_carp(toplam1))

# print(*"-----------------")
# print(*"-----------------")

def uclecarp(a):
    print("1.fonksiyon çalıştı")
    return a*3

def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a+2

def dordebol(a):
    print("3.fonksiyon çalıştı")
    return a/4

# 3 ünü beraber kullanalım
print(dordebol(ikiyletopla(uclecarp(5))))

print(*"------------")
print(*"------------")

"""
return ifadesinden sonra fonksiyonumuz tamamıyla sona erer. 
Yani, return ifadesinden sonra yapılan herhangi bir işlem çalıştırılmaz.
"""

def toplama(a,b,c):
    return a+b+c
    print("Toplama fonksiyonu")  # çalıştırılmadı

print(toplama(1,2,3))

print(*"------------")

def toplama(a,b,c):
    print("Toplama fonksiyonu")  # çalıştırıldı
    return a+ b+ c

print(toplama(1,2,3))

"""
Fonksiyonlarda çağrıldığı yere herhangi bir değer döndürmeyen(return kullanılmayan) fonksiyonlara void fonksiyonlar denmektedir.
 Bunu da genel kültür olarak bilmekte fayda var.
"""