"""
'r' (Read - Okuma Modu)
 - Amaç: Var olan bir dosyayı okumak
 - Davranış:
    - Eğer dosya mevcutsa, içeriği okur ve döndürür.
    - Eğer dosya mevcut değilse, "FileNotFoundError" hatası verir.
"""

with open('dosya.txt', 'r') as dosya:
    icerik = dosya.read()