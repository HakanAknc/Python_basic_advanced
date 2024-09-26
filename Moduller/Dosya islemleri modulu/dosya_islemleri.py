def dosya_yaz(dosya_adi, veri):
    with open(dosya_adi, "w") as dosya:
        dosya.write(veri)

def dosya_oku(dosya_adi):
    with open(dosya_adi, 'r') as dosya:
        return dosya.read()
    
if __name__ == "__main__":
    dosya_yaz("ornek.txt", "Merhaba Dünya!!!!")
    print(dosya_oku('ornek.txt"'))
