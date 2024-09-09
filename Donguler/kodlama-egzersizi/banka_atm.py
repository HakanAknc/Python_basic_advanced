print("********************\nATM sistemine hoşgeldiniz\n********************")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.

""")

bakiye  = 1000 # Bakiyeniz 100 olsun

while True:
    işlem = input("İşlemi giriniz: ")

    if (işlem == "q"):
        print("Yine bekleriz...")
        break
    
    elif (işlem == "1"):
        print("Bakiyeniz {} TL'dir.".format(bakiye))
    
    elif (işlem == "2"):
        miktar = int(input("Yatırmak istediğiniz tutar: "))
        bakiye += miktar
    
    elif (işlem == "3"):
        miktar = int(input("Çekmek istediğiniz tutar: "))
        if (bakiye - miktar < 0):
            print("Bu kadar çekemezsiniz....")
            print("Bakiyeniz {} TL'dir.".format(bakiye))
            continue
        bakiye -= miktar

    else:
        print("Lütfen geçerli bir işlem giriniz..")