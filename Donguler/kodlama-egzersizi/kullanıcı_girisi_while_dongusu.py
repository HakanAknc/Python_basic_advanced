print("**********\nKullanıcı Girişi\n**********\n")

# Kullanıcı Adı Girişi örneğinin gerçek versiyonunu PyQT5 derslerinde bulabilirsiniz.

sys_kul_adi = "hakan"  # Sistemde kayıtlı olduğunu düşündüğümüz kullanıcı adı
sys_parola = "12345"   # Sistemde kayıtlı olduğunu düşündüğümüz parola

giris_hakki = 3

while True: # Kullanıcı doğru giriş yaptığında ve giriş hakkı bittiğinde sona erecek
    kullanici_adi = input("Kullanıcı adı: ")
    parola = input("Parola: ")

    if (kullanici_adi != sys_kul_adi and parola == sys_parola):
        print("Kullanıcı adı hatalı...")
        giris_hakki -= 1
        print("Giriş Hakkı: ", giris_hakki)
    
    elif (kullanici_adi == sys_kul_adi and parola != sys_parola):
        print("Parola hatalı")
        giris_hakki -= 1
        print("Giris Hakkı: ",giris_hakki)
    
    else: 
        print("Başarıyla giriş yaptınız....")
        break
    if (giris_hakki == 0):
        print("Giriş Hakkınız Bitti...")
        break
