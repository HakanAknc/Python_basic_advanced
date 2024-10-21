"""
Şimdi isterseniz 10'luk tabandaki bir sayıyı ikilik tabana çevirmek için kullanılan *bin()* fonksiyonuna bakalım.
"""
print(bin(4))  # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)

print(bin(2796202))    # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)

print(bin(521))   # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
print(*"-----")

"""
Şimdi de 10'luk tabandaki bir sayıyı 16'lık tabana çevirmek için kullanılan hex() fonksiyonuna bakalım.
"""
print(hex(32))   # Sayımız 16'lık tabanda yazıldı.

print(hex(54))

print(hex(1212))
print(*"-----")

"""
Fonksiyonlar
abs fonksiyonu
Sayının mutlak değerini almamızı sağlar.
"""
print(abs(-4))
print(abs(4.5))
print(abs(0))
print(abs(-10))
print(*"-----")


"""
round fonksiyonu
Sayıları alta veya üste yuvarlar.
"""
print(round(3.7))
print(round(3.2))
print(round(3))
print(round(3.21329321321323,4))   # Ondalıklı sayının 4. hanesine göre yuvarlar
print(round(3.21324321321323,4))   # Ondalıklı sayının 4. hanesine göre yuvarlar
print(*"-----")


"""
max ve min fonksiyonu
*max()* fonksiyonu verdiğimiz değerlerin en büyüğünü döndürür.

*min()* fonksiyonu verdiğimiz değerlerin en küçüğünü döndürür.
"""
print(max(3,4))
print(max(100,-2,3,4,1,131))
print(max([13.2,-4.32,1.2,15.6]))
print(max((13.2,-4.32,1.2,15.6)))
print(min(3,4))
print(min(100,-2,3,4,1,131))
print(*"-----")


"""
sum fonksiyonu
*sum() fonksiyonu* verilen değerleri toplayarak döndürür. Değerlerin liste,demet vb. şeklinde verilmesi gerekir.
"""
# print(sum(3,4))
print(sum([3,4,5,6,7]))
print(sum((3,4)))
print(*"-----")


"""
pow fonksiyonu
*pow() fonksiyonu* üs alma işlemlerinde kullanılır.
"""

print(pow(2,4))
print(pow(3,4))
print(pow(17,2))
print("Teşekkürler...")