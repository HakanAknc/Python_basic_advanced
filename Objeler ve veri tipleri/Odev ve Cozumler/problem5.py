"""
Problem 5
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

a = input("a: ")
b = input("b: ")

print("Değiştirilmeden önce değerler\na: {} b: {}\n".format(a,b))

a,b = b,a

print("Değiştirildikten sonraki değerler\na: {} b: {}\n".format(a,b))
