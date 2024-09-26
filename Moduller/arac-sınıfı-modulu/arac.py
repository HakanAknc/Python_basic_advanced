class Arac():
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.hiz = 0

    def hiz_artir(self, miktar):
        self.hiz += miktar
        print(f"{self.marka} {self.model} hızını {self.hiz} km/s'ye artırdı.")

    def hiz_dusur(self, miktar):
        if self.hiz - miktar < 0:
            self.hiz = 0
        else:
            self.hiz -= miktar
        print(f"{self.marka} {self.model} hızını {self.hiz} km/s'ye düşürdü.")
    
    def bilgi_ver(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}, Hız: {self.hiz} km/s")
    
if __name__ == "__main__":
    arac1 = Arac("Toyota", "Corolla", 2020)
    arac1.hiz_artir(50)
    print(arac1.bilgi_ver())
