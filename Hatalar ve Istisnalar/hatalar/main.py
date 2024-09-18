"""
Hatalar ve İstisnalar
Bu videoyla beraber artık Python programlarında oluşabilecek belli bir hatayı veya istisnayı nasıl çözeceğimizi öğrenmeye çalışacağız.
"""
"""
Hatalar
Python programlarında bazen bir değişkenin tanımlanmadan kullanılmaya çalıştırılması , bazen de yapılamayacak bir aritmetik işlemin yapılması Pythonda hatalara yol açar. 
Ancak bu istisnai durumlarda, hataların türüne göre programlarımızı daha güvenli bir şekilde yazabiliriz.
Yani hata çıkarabilecek kodlarımızı öngörerek bu hataları programlarımızda yakalayabiliriz. Pythondaki bazı hatalara şunlar örnek verilebilir;
"""

print(a) # Tanımlı değil - Name Error hatası

int("sdas324234") # Value Error Hatası

2 / 0 # Bir sayı 0'a bölünemez.

print('Mustafa'sadasdasdasd) # Syntax Error
