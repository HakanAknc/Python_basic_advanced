"""
Proje 1
Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin
"""

# Hayvan sınıfı (Temel sınıf)
class Hayvan:
    def __init__(self, isim, yas, tur):
        self.isim = isim
        self.yas = yas
        self.tur = tur

    def ses_cikar(self):
        return "Bu hayvan bir ses çıkarıyor."

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Tür: {self.tur}"

# Köpek sınıfı (Hayvan sınıfından miras alıyor)
class Kopek(Hayvan):
    def __init__(self, isim, yas, tur, cins, egitildi_mi):
        super().__init__(isim, yas, tur)
        self.cins = cins
        self.egitildi_mi = egitildi_mi

    def ses_cikar(self):
        return "Hav hav!"

    def bilgileri_goster(self):
        temel_bilgi = super().bilgileri_goster()
        ek_bilgi = f"Cins: {self.cins}, Eğitildi mi: {'Evet' if self.egitildi_mi else 'Hayır'}"
        return temel_bilgi + ", " + ek_bilgi

# Kuş sınıfı (Hayvan sınıfından miras alıyor)
class Kus(Hayvan):
    def __init__(self, isim, yas, tur, kanat_genisligi):
        super().__init__(isim, yas, tur)
        self.kanat_genisligi = kanat_genisligi

    def ses_cikar(self):
        return "Cik cik!"

    def uc(self):
        return f"{self.isim} uçuyor!"

    def bilgileri_goster(self):
        temel_bilgi = super().bilgileri_goster()
        ek_bilgi = f"Kanat Genişliği: {self.kanat_genisligi} cm"
        return temel_bilgi + ", " + ek_bilgi

# At sınıfı (Hayvan sınıfından miras alıyor)
class At(Hayvan):
    def __init__(self, isim, yas, tur, cins, hiz):
        super().__init__(isim, yas, tur)
        self.cins = cins
        self.hiz = hiz

    def ses_cikar(self):
        return "Kişne!"

    def kos(self):
        return f"{self.isim} saatte {self.hiz} km hızla koşuyor!"

    def bilgileri_goster(self):
        temel_bilgi = super().bilgileri_goster()
        ek_bilgi = f"Cins: {self.cins}, Hız: {self.hiz} km/s"
        return temel_bilgi + ", " + ek_bilgi


# Test edelim
kopek = Kopek("Max", 3, "Köpek", "Golden Retriever", True)
kus = Kus("Tweety", 1, "Kuş", 30)
at = At("Şahbatur", 5, "At", "Arap Atı", 60)

print(kopek.ses_cikar())
print(kopek.bilgileri_goster())

print(kus.ses_cikar())
print(kus.uc())
print(kus.bilgileri_goster())

print(at.ses_cikar())
print(at.kos())
print(at.bilgileri_goster())
