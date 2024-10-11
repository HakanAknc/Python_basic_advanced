"""
Dosyalarda Değişiklik Yapmak
Bu derste dosyalarda değişiklik yapmayı öğrenmeye çalışacağız. Bunun için 2 farklı yolu öğrenmeye çalışacağız.
"""

"""
seek() ve write()
Eğer biz bir dosyanın belli bir yerine seek() fonksiyonu ile gidip, write() fonksiyonunu kullanırsak, 
azdığımız değerler öncesinde bulunan değerlerin üzerine yazılacaktır. 
Bunun için hem okuma hem de yazma işlemimizi yapmamızı sağlayan "r+" kipini kullanacağız. 
İlk önce dosyamızda bilgileri görelim.
"""

with open("bilgiler.txt","r+", encoding="utf-8") as file:
    print(file.read())

with open("bilgiler.txt","r+",encoding = "utf-8") as file: 
    file.seek(10) # 10. byte
    file.write("Deneme")

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    print(file.read())


"""
Dosyanın Sonunda Değişiklik Yapmak
Bu işlemlerin en kolayıyla başlayalım. Dosyaların sonunda değişiklik yapmak için, dosyamızı "a" kipiyle açalım
 ve sadece dosyanın sonuna write() ile ekleme yapalım.
"""
with open("bilgiler.txt","a",encoding = "utf-8") as file:
    file.write("Mert Erarslan\n") # "append" metoduyla açılan bir dosyanın imleci direk dosyanın sonunda olduğu için sadece write


with open("bilgiler.txt","r",encoding = "utf-8") as file:
    print(file.read())


"""
Dosyanın Başında Değişiklik Yapmak
"bilgiler.txt" dosyamızın başına bir tane satır eklemek için ne yapabiliriz ? 
Bunun için dosyamızı bütünüyle string halinde alıp daha sonra satırımızı string'in başına eklememiz gerekiyor. 
Daha sonra dosyanın en başına seek() fonksiyonuyla giderek ,direk write() fonksiyonunu kullanabiliriz. Hemen yapalım.
"""

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)
    

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    
    icerik = "Semih Aktaş\n" + icerik
    file.seek(0)
    file.write(icerik)

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)

"""
Dosyanın Ortasında Değişiklik Yapmak
Dosyaların ortasına herhangi bir satır eklemek için ilk olarak her bir satırı liste halinde almamızı sağlayan readlines() 
fonksiyonunu kullanacağız. Daha sonra bu listenin herhangi bir yerine bir eleman ekleyerek bu listeyi 
for döngüsü ile dosyaya yazacağız.
"""

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    print(file.readlines())

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Mehmet Keper\n")
    file.seek(0)
    for satır in liste:
        file.write(satır)

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)

"""
Pythonda bir dosyaya listenin içindeki değerleri yazmak için for döngüsü dışında pratik bir fonksiyon bulunuyor. 
writelines fonksiyonu içine verdiğimiz listeyi dosyaya yazacaktır.
"""

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Ahmet Baltacı\n")
    file.seek(0)
    file.writelines(liste)


with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)