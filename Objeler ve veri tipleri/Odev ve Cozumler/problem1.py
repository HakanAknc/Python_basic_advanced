"""
Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
"""
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

carp = a * b * c
print("Sonuc : {} * {} * {}  = {}".format(a,b,c,carp))