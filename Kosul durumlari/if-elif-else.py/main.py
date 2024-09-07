"""
Koşullu Durumlar - if - elif - else koşullu durumları
Önceki konumuzda koşullu durumlardaki if-else kalıplarımızı öğrendik. Bu bölümde de if-elif-else kalıplarını öğrenmeye çalışacağız.
"""
"""
if-elif-else Blokları
Önceki konumuzda koşullu durumlarımızla sadece tek bir koşulu kontrol edebiliyorduk. 
Ancak programlamada bir durum bir çok koşula bağlı olabilir. 
Örneğin bir hesap makinesi programı yazdığımızda kullanıcının girdiği işlemlere göre koşullarımızı belirleyebiliriz. 
Bu tür durumlar için if-elif-else kalıplarını kullanırız. Kullanımı şu şekildedir;

           if koşul: 
               Yapılacak İşlemler
           elif başka bir koşul:
               Yapılacak İşlemler
           elif başka bir koşul:
               Yapılacak İşlemler
                //
                //
           else:
               Yapılacak İşlemler 
Programlarımızda, Kaç tane koşulumuz var ise o kadar elif bloğu oluşturabiliriz. 
Ayrıca else in yazılması zorunlu değildir. if - elif - else kalıplarında, hangi koşul sağlanırsa program o bloğu çalıştırır ve 
if-elif-blokları sona erer. Şimdi isterseniz kullanıcıya işlem seçtirdiğimiz bir programla , bu kalıbı öğrenmeye başlayalım.
"""
işlem = int(input("İşlem seçiniz: "))

if işlem == 1:
    print("1. işlem seçildi.")
elif işlem == 2:
    print("2. işlem seçildi.")
elif işlem == 3:
    print("3. işlem seçildi.")
else:
    print("Geçersiz İşlem!")

print(*"--------------")


"""
if-if-if Blokları
Bu blokları öğrenmeden önce isterseniz öğrendiğimiz bilgilerle, bir harf notu hesaplama sistemi yapalım.
 Daha sonra bu kalıpları anlamaya çalışalım.
"""
note = float(input("Notunuzu giriniz: "))

if note >= 90:
    print("AA")
elif note >= 85:
    print("BA")
elif note >= 90:
    print("BA")
elif note >= 80:
    print("BB")
elif note >= 75:
    print("CB")
elif note >= 70:
    print("CC")
elif note >= 65:
    print("DC")
elif note >= 60:
    print("DD")
else:
    print("Dersten Kaldınız")

print(*"--------------")

note = float(input("Notunuzu giriniz:"))

if note >= 90:
    print("AA")
if note >= 85:
    print("BA")
if note >= 90:
    print("BA")
if note >= 80:
    print("BB")
if note >= 75:
    print("CB")
if note >= 70:
    print("CC")
if note >= 65:
    print("DC")
if note >= 60:
    print("DD")
else:
    print("Dersten Kaldınız")