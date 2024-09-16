"""
Overriding (İptal Etme)
Eğer biz miras aldığımız metodları aynı isimle kendi sınıfımızda tekrar tanımlarsak , artık metodu çağırdığımız 
zaman miras aldığımız değil kendi metodumuz çalışacaktır. 
Buna Nesne Tabanlı Programlamada bir metodu override etmek denmektedir.
"""
"""
Örneğin artık Çalışan sınıfının init metodunu kullanmak yerine Yönetici sınıfında init metodunu override edebiliriz. 
Böylelikle Yönetici sınıfına ekstra özellikler(attribute) ekleyebiliriz.
"""
class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman

class Yonetici(Çalışan):
    def __init__(self, isim, maaş, departman,kişi_sayısı): # Sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı  # Yeni eklenen özellik
    def bilgilerigoster(self):
        
        print("Yönetici sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı
    
a = Yonetici("Hakan Akıncı",60000,"Yazılım",5) # Yönetici sınıfının init fonksiyonu. Override edildi.
b = Yonetici("Serhat Say",2500,"Pazarlama",5)
b.bilgilerigoster()  # Kendi yazdığımız fonksiyon çağrıldı. Overriding