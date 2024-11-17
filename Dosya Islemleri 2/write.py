"""
'w' (Write - Yazma Modu)
 - Amaç: Bir dosyaya yazmak
 - Davranış:
    - Eğer dosya mevcutsa, içeriği siler ve yeni içerik yazar.
    - Eğer dosya mevcut değilse, yeni bir dosya oluşturur.
"""

# Yazma
with open('yeni_dosya.txt', 'w') as dosya:
    dosya.write("Bu yeni bir dosyadır.\n")  # Yeni içerik yaz

"""
Eğer yeni_dosya.txt zaten varsa, içeriği silinerek yenisi yazılır. Eğer yoksa, dosya oluşturulur.
"""