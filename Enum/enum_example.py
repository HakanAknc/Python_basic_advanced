from enum import Enum

# Görevleri durumları Enum ile tanımlıyoruz
class GorevDurumu(Enum):
    AKTIF = 1
    TAMAMLANDI = 2
    BEKLEMEDE = 3
    IPTAL_EDILDI = 4

# Görev sınıf
class Gorev:
    def __init__(self,isim,durum):
        self.isim = isim
        self.durum = durum

    def durum_degistir(self, yeni_durum):
        if not isinstance(yeni_durum, GorevDurumu):
            raise ValueError("Geçersiz durum!")
        self.durum = yeni_durum

    def __str__(self):
        return f"Görev: {self.isim}, Durum: {self.durum.name}"
    
# Görevler olustur
gorev1 = Gorev("Rapor Hazırla", GorevDurumu.AKTIF)
gorev2 = Gorev("Toplantı Yap", GorevDurumu.BEKLEMEDE)

# Görev bilgileri yazdır
print(gorev1)   # Görev: Rapor Haazırla, Durum: AKTIF
print(gorev2)

# Görev durumunu değiştir.
gorev1.durum_degistir(GorevDurumu.TAMAMLANDI)
print(gorev1)