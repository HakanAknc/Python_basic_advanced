"""
Nesne Tabanlı Programlama - Kalıtım (Inheritance)
Bu konuda Nesne Tabanlı Programlamadaki inheritance(kalıtım veya miras alma) konseptini öğrenmeye çalışacağız. 
Inheritance veya kalıtım bir sınıfın başka bir sınıftan özelliklerini(attribute ) ve metodlarını miras almasıdır.
Bu konsepti aslında bizim kendi anne babamızdan değişik özellikleri ve davranışları miras almamıza benzetebiliriz.
(Hani derler ya ! Babasına çekmiş :) )
Peki inheritance nerede işimize yarar ?
Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz. 
Bunun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor. 
Aslında baktığımız zaman bu sınıfların hepsinin belli ortak metodları ve özellikleri bulunuyor. 
O zaman bu ortak özellikleri ve metodları tekrar tekrar bu sınıfların içinde tanımlamak yerine, bir tane ana class tanımlayıp bu classların bu classın özelliklerini ve metodlarını almalarını sağlayabiliriz.
Inheritance'ın veya Kalıtım'ın temel mantığı budur.
"""

class Calısan():
    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgilerini göster.")
        print("İsim : {} \nMaas: {} \nDepartman: {}\n".format(self.isim,self.maas,self.departman))

    def departman_degistir(self,yeni_dpertman):
        print("Departman değişiyor...")
        self.departman = yeni_dpertman

class Yonetici(Calısan):  # Çalışan sınıfınfan miras alıyoruz.
    # pass # Pass Deyimi bir bloğu sonradan tanımlamak istediğimizde kullanılan bir deyimdir.
    def zam_yap(self, zam_miktari):
        print("Maaşa zam yapılıyor...")
        self.maas += zam_miktari

yonetici1 = Yonetici("Mehmet Baltacı",3000,"İnsan Kaynakları") # yönetici objesi
yonetici1.bilgilerigoster()
yonetici1.departman_degistir("Yazılım - Backend")
yonetici1.bilgilerigoster()
print(*"-----------")
yonetici2 = Yonetici("Hakan AKıncı",30000,"Yazılım")
yonetici2.bilgilerigoster()
yonetici2.zam_yap(5000)
yonetici2.bilgilerigoster()