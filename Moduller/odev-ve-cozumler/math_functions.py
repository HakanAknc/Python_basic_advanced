import math

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Bölme hatası: Sıfıra bölme!"

def us_alma(x, y):
    return x ** y

def karekok_alma(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Karekök hatası: Negatif sayı!"

def sin_alma(x):
    return math.sin(x)

def cos_alma(x):
    return math.cos(x)

def logaritma(x):
    if x > 0:
        return math.log10(x)
    else:
        return "Logaritma hatası: Pozitif sayı gerekli!"
