"""
Döngülerde kullanılan ifadeler : break ve continue
"""
"""
break ifadesi
break ifadesi döngülerde programcılar tarafından en çok kullanılan ifadedir. Anlamı şu şekildedir;

        Döngü herhangi bir yerde ve herhangi bir zamanda break ifadesiyle karşılaştığı zaman
        çalışmasını bir anda durdurur. Böylelikle döngü hiçbir koşula bağlı kalmadan sonlanmış olur.


break ifadesi sadece ve sadece içindeki bulunduğu döngüyü sonlandırır. 
Eğer iç içe döngüler bulunuyorsa ve en içteki döngüde break kullanılmışsa sadece içteki döngü sona erer. 
Örneklerle break ifadesini anlamaya çalışalım
"""

i = 0  # başlangıç değeri

while (i < 10):
    print(i)
    i += 1

print(*"-------------")

i = 0 # break kullanmaya çalışalım.

while (i < 20):
    print(i)
    if (i == 10):
        break # i'nin değeri 10 olunca bu koşul sağlanıyor ve  break ifadesiyle karşılaşıldığı için döngü anında sona eriyor.
    i +=1

print(*"-------------")

# for döngüsüyle break kullanalım.
liste = [1,2,3,4,5,6,7,8,9]
for i in liste:
    if (i == 5):
        
        break
    print(i)

print(*"-------------")

while True: # Sonsuz döngü. Nasıl sonlandırabiliriz ? 
    isim = input("İsminiz(Çıkmak için q tuşuna basın.):")
    if (isim == "q"): # break ile tabii ki.
        print("Çıkış yapılıyor...")
        break
    print(isim)

print(*"-------------")
print(*"-------------")

"""
continue ifadesi
continue ifadesi break'e göre biraz daha az kullanılan bir ifadedir. Anlamı şu şekildedir;

    Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığı zaman geri kalan işlemlerini
    yapmadan direk bloğunun başına döner.

continue ifadesini anlamak için örneklerimize bakalım.
"""

liste = [1,2,3,4,5,6,7,8,9,10]

for i in liste: # Bunu biliyoruz.
    print("i:",i)

print(*"-------------")

liste = [1,2,3,4,5,6,7,8,9] # continue kullanalım.


for i in liste:
    if (i == 3 or i == 5):
        continue
    print("i:",i)

print(*"-------------")

i = 0 # Bu kodda Sonsuz döngü olayı neden oluşur ? Bu kodu çalıştırmayalım.

# Eğer çalıştırırsak sonsuz döngüyü "Kernel" sekmesinde 

# while (i < 10):
#     print(i)
    
#     if (i == 2):
#         continue
        
#     i += 1

print(*"-------------")

i = 0 # Kodun sorunsuz hali

while (i < 10):
    
    if (i == 2):
        i += 1 # Artırma işlemi
        continue
        
    print("i:",i)
    i += 1