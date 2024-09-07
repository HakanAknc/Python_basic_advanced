"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. 
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. 
Kullanımı şu şekildedir ;
"""

sekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz? : ")
if (sekil == "Dörtgen"):
    print("Lütfen kenar sayılarını giriniz: ")
    a = int(input("Kenar-1: "))
    b = int(input("Kenar-2: "))
    c = int(input("Kenar-3: "))
    d = int(input("Kenar-4: "))

    if (a == b and  a == c and a == d):
        print("Kare")
    elif (a == b and b == d):
        print("Diktörtgen")
    else:
        print("Dörtgen")

print(*"-------")

if (sekil == "Ücgen"):
    a = int(input("Keant-1: "))
    b = int(input("Keant-2: "))
    c = int(input("Keant-3: "))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen...")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirmiyor...")
else:
    print("Geçersiz Şekil...")