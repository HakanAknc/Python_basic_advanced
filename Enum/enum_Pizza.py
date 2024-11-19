"""
Pizza Sipariş Sistemi
Bir pizzacıda:

Boyutlar: Küçük, Orta, Büyük
Hamur Tipleri: İnce, Kalın
Sipariş Durumları: Hazırlanıyor, Fırında, Teslim Edildi
Bu bilgileri Enum ile modelleyelim ve bir sipariş sistemi yapalım
"""

from enum import Enum

# Pizza Boyutları Enum
class Boyut(Enum):
    KUCUK = "Küçük"
    ORTA = "Orta"
    BUYUK = "Büyük"

# Hamur Tipleri Enum
class HamurTipi(Enum):
    INCE = "İnce"
    KALIN = "Kalın"

# Sipariş durumları enum
class SiparisDurumu(Enum):
    HAZIRLANIYOR = "Hazırlanıyor"
    FIRINDA = "Fırında"
    TESLIM_EDILDI = "Teslim Edildi"

# Pizza Sipariş Sınıf
class PizzaSiparis:
    def __init__(self, boyut, hamur_tipi):
        if not isinstance(boyut, Boyut):
            raise ValueError("Geçersiz boyut!")
        if not isinstance(hamur_tipi, HamurTipi):
            raise ValueError("Geçersiz hamur tipi!")
        self.boyut = boyut
        self.hamur_tipi = hamur_tipi
        self.durum = SiparisDurumu.HAZIRLANIYOR

    def durum_guncelle(self, yeni_durum):
        if not isinstance(yeni_durum, SiparisDurumu):
            raise ValueError("Geçersiz sipariş durumu!")
        self.durum = yeni_durum

    def __str__(self):
        return (f"Pizza Siparişi: {self.boyut.value} boyut, "
                f"{self.hamur_tipi.value} hamur, Durum: {self.durum.value}")

# Sipariş Oluştur
siparis1 = PizzaSiparis(Boyut.ORTA, HamurTipi.INCE)
print(siparis1)  # İlk durum: Hazırlanıyor

# Sipariş durumunu güncelle
siparis1.durum_guncelle(SiparisDurumu.FIRINDA)
print(siparis1)  # Durum: Fırında

siparis1.durum_guncelle(SiparisDurumu.TESLIM_EDILDI)
print(siparis1)  # Durum: Teslim Edildi


"""
Kodun Açıklaması
Enum Tanımlamaları:

Boyut: Pizzanın boyutları.
HamurTipi: Hamurun ince veya kalın olması.
SiparisDurumu: Siparişin mevcut durumu (Hazırlanıyor, Fırında, Teslim Edildi).
PizzaSiparis Sınıfı:

Siparişe ait boyut ve hamur tipi, Enum ile kontrol ediliyor.
Başlangıç durumu SiparisDurumu.HAZIRLANIYOR olarak belirleniyor.
Durum güncellemeleri yalnızca geçerli bir Enum ile yapılabiliyor.
"""

"""
Özet: Kodun Mantığı
Boyut, HamurTipi ve SiparisDurumu gibi sabit değerler Enum ile tanımlandı.
PizzaSiparis sınıfı, bir siparişi oluşturmak ve durumunu yönetmek için tasarlandı.
__init__ metodu, başlangıçta siparişin boyutunu, hamur tipini ve durumunu belirledi.
durum_guncelle metodu, siparişin durumunu değiştirdi.
__str__ metodu, sipariş bilgilerini anlamlı bir şekilde görüntüledi.
"""

"""
Sonuç: Enum Kullanımının Avantajları
Sabit değerleri gruplandırıp düzenli hale getirdi.
Yanlış değerlerin verilmesini engelleyerek hata kontrolü sağladı.
Kodun okunabilirliğini ve anlamını artırdı.
"""