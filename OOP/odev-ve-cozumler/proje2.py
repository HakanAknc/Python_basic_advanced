"""
Proje 2
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.
"""

class Bilgisayar:
    def __init__(self, marka, model, islemci, ram, disk_kapasitesi):
        # Bilgisayarın temel özellikleri
        self.marka = marka
        self.model = model
        self.islemci = islemci
        self.ram = ram
        self.disk_kapasitesi = disk_kapasitesi
        self.acik_mi = False

    # Özel metod: Bilgisayarı açma ve kapama
    def ac(self):
        if not self.acik_mi:
            self.acik_mi = True
            print(f"{self.marka} {self.model} açılıyor...")
        else:
            print(f"{self.marka} {self.model} zaten açık!")

    def kapa(self):
        if self.acik_mi:
            self.acik_mi = False
            print(f"{self.marka} {self.model} kapanıyor...")
        else:
            print(f"{self.marka} {self.model} zaten kapalı!")

    # Özel metod: __str__ - Bilgisayarın bilgilerini kullanıcıya gösteren metot
    def __str__(self):
        return f"Bilgisayar Markası: {self.marka}, Modeli: {self.model}, İşlemcisi: {self.islemci}, RAM: {self.ram} GB, Disk Kapasitesi: {self.disk_kapasitesi} GB"

    # Özel metod: __len__ - Bilgisayarın RAM kapasitesini döndürür
    def __len__(self):
        return self.ram

    # Özel metod: __eq__ - İki bilgisayarın eşit olup olmadığını kontrol eder
    def __eq__(self, diger):
        return (self.marka == diger.marka and self.model == diger.model)

    # Özel metod: __gt__ - Bir bilgisayarın diğerinden daha güçlü olup olmadığını karşılaştırır (RAM üzerinden)
    def __gt__(self, diger):
        return self.ram > diger.ram

    # Özel metod: __add__ - İki bilgisayarın RAM kapasitelerini toplar
    def __add__(self, diger):
        return self.ram + diger.ram

    # Özel metod: __del__ - Bilgisayar nesnesi silinirken mesaj verir
    def __del__(self):
        print(f"{self.marka} {self.model} nesnesi silindi.")


# Bilgisayar sınıfını kullanma
bilgisayar1 = Bilgisayar("Dell", "XPS 13", "Intel i7", 16, 512)
bilgisayar2 = Bilgisayar("Apple", "MacBook Pro", "M1", 8, 256)

# Bilgisayarları açma ve kapama
bilgisayar1.ac()
bilgisayar1.kapa()

# Bilgisayarın özelliklerini gösterme (__str__)
print(bilgisayar1)

# RAM kapasitesini gösterme (__len__)
print(f"{bilgisayar1.marka} RAM kapasitesi: {len(bilgisayar1)} GB")

# Bilgisayarların eşit olup olmadığını kontrol etme (__eq__)
print(bilgisayar1 == bilgisayar2)

# RAM kapasitesi karşılaştırması yapma (__gt__)
print(bilgisayar1 > bilgisayar2)

# Bilgisayarların RAM kapasitelerini toplama (__add__)
toplam_ram = bilgisayar1 + bilgisayar2
print(f"Toplam RAM kapasitesi: {toplam_ram} GB")

# Bilgisayar nesnesini silme (__del__)
del bilgisayar1
