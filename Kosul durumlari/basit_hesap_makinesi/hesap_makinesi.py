print("""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz
İşlemler;
    
    1. Toplama İşlemi
    
    2. Çıkarma İşlemi
    
    3. Çarpma İşlemi
    
    4. Bölme İşlemi
-----------------------------------------------------------
""")

a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))

islem = input("İşlem numarası giriniz: ")

if (islem == "1"):
    print("{} ile {} 'nin toplamı {} dır.".format(a,b,a+b))
elif (islem == "2"):
    print("{} ile {} 'nin farkı {} dır.".format(a,b,a-b))
elif (islem == "3"):
    print("{} ile {} 'nin çarpımı {} dır.".format(a, b, a * b))
elif (islem == "4"):
    print("{} 'nın {} 'e bölümü {} dır.".format(a, b, a / b))
else:
    print("Lütfen geçerli bir işlem giriniz...")