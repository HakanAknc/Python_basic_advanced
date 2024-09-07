"""
Mantıksal Bağlaçlar
Mantıksal bağlaçlar daha çok karşılaştırma işlemini kontrol ettiğimiz zamanlarda kullanılır. 
Bu konuda bunları öğrenmeye çalışacağız.
"""
"""
and Operatörü
Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonucunun True olmasına bakar. 
Bağlanan karşılaştırma işlemlerinin hepsinin kendi içinde sonucu True ise genel sonuç True , diğer durumlarda ise sonuç False çıkar.
Kullanımı şu şekildedir.
"""
print(*"and")

print(bool(1 < 2 and "Murat" == "Murat"))
print(bool(2 > 3 and "Murat" == "Murat"))
print(bool(2 == 2 and 3.14 < 2.54 and "Elma" != "Armut"))

print(*"-----------")
print(*"or")
"""
or Operatörü
Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonuçlarından en az birinin True olmasına bakar. 
Bağlanan karşılaştırma işlemlerinin en az birinin True olmasında genel sonuç True , diğer durumlarda ise sonuç False çıkar. 
Kullanımı şu şekildedir.
"""
print(bool(1 < 2 or "Murat" != "Murat"))
print(bool(2 > 3 or "Murat" != "Murat"))
print(bool(2 > 3 or "Murat" != "Murat" or 3.14 < 4.32))
print(*"-----------")
print(*"not")

"""
not operatörü
not operatörü aslında bir mantıksal bağlaç değildir. Bu operatör sadece bir mantıksal değeri veya karşılaştırma işlemininin tam tersi sonuca çevirir. 
Yani, not operatörü True olan bir sonucu False , False olan bir sonucu True sonucuna çevirir. Kullanımı şu şekildedir.
"""
print(bool(not 2 == 2))
print(bool(not "Python" == "Php"))
print(*"-----------")
print(*"and\tor\tnot")

"""
Operatörleri Beraber Kullanma
Burada gördüğümüz 3 operatörü beraber kullanmak karmaşıklığa yol açacağı için, parantez kullanabiliriz.
"""
print(bool(not (2.14 > 3.49 or ( 2 != 2 and "Murat" == "Murat"))))
print(bool("Araba" < "Zula" and ( "Bebek" < "Çoçuk" or (not 14 ))))