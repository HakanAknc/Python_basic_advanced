# Liste elemanlarını toplama

def liste_toplam(liste):
    toplam = 0
    for eleman in liste:
        toplam += eleman
    return toplam

print(liste_toplam([1,2,3,4,5]))