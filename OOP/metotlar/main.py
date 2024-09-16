"""
Nesne Tabanlı Programlama - Metodlar
Bu videoda bir sınıf içinde metodlarımızı nasıl tanımlayacağımızı öğrenmeye çalışacağız. 
Bunun için ilk olarak bir Yazılımcı sınıfı tanımlayalım.
"""

class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maas = maas
        self.diller = diller

# yazılımcı1 objesi
yazilimci1 = Yazilimci("Hakan","Akıncı",12345,3000,["Python",".Net","PHP"])
yazilimci2 = Yazilimci("Serhat","Say",23456,3500,["Matlab","R","SmallTalk"])
print(yazilimci1.diller)
print(yazilimci2.soyisim)
print(*"------")

"""
Önceki dersten bunların nasıl yapıldığını biliyoruz. 
Peki bu class'a metodlarımızı nasıl tanımlayabiliriz ? 
Aynı init metodunu tanımladığımız gibi bir class'a da istediğimiz kadar metod tanımlayabiliriz. 
Örneğin ,Yazılımcı classına bilgilerigöster isimli bir metod tanımlayalım.
"""

class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maas = maas
        self.diller = diller

    def bilgilerigoster(self):
        print("""
        Çalışan Bilgisi:
        
        İsim : {}
    
        Soyisim : {}
              
        Şirket Numarasi : {}
            
        Maaş : {}
            
        Diller : {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))

yazilimci1 = Yazilimci("Hakan","AKıncı",12345,50000,["Python",".Net","PHP"])
yazilimci1.bilgilerigoster()
print(*"**------**")

"""
Burada bilgilerigöster isimli metod tanımlayarak her bir özelliğimizin değeri ekrana derli toplu bir şekilde yazdırmış olduk.
 Metodlarımızı yazarken dikkat etmemiz gerek nokta, her metodun birinci parametresinin self referansı olması gerektiğidir. 
 Ayrıca objelerimizin özelliklerine mutlaka self referansıyla erişmemiz gerekiyor. 
İsterseniz bu classa 2 tane daha metod yazalım.
"""
class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller

    def bilgilerigöster(self):
        print("""
        Çalışan Bilgisi:
        
        İsim :  {}
        
        Soyisim : {}
        
        Şirket Numarası: {}
        
        Maaş :  {}
        
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))

    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor.")
        self.diller.append(yeni_dil)
    
    def maas_yukselt(self,zam_miktari):
        print("Maaş yükseltiliyor...")
        self.maas += 250

yazilimci1 = Yazilimci("Hakan","AKıncı",12345,50000,["Python",".Net","PHP"])
yazilimci1.bilgilerigöster()

yazilimci1.maas_yukselt(500)
yazilimci1.bilgilerigöster()

yazilimci1.dil_ekle("NodeJs")
yazilimci1.bilgilerigöster()