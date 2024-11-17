"""
'a' (Append - Ekleme Modu)
 - Amaç: Var olan bir dosyaya ekleme yapmak
 - Davranış:
    - Eğer dosya mevcutsa, içeriği silmeden yeni içerik ekler.
    - Eğer dosya mevcut değilse, yeni bir dosya oluşturur.
"""

# Ekleme
with open('yeni_dosya.txt', 'a') as dosya:
    dosya.write("Bu eklenmiş bir içeriktir.\n")  # Mevcut dosyaya ekle

"""
Eğer yeni_dosya.txt mevcutsa, yeni metin dosyanın sonuna eklenir. Eğer yoksa, dosya oluşturulur.
"""