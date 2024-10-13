"""
Reduce Fonksiyonu
Bu konuda bir diğer gömülü fonksiyonumuz olan reduce fonksiyonunu öğrenmeye çalışacağız.

            reduce(function, iterasyon yapılabilen veritipi(liste vb.))

reduce() fonksiyonu* değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular ve daha
sonra çıkan sonucu listenin 3. elemanına uygular ve bu şekilde devam ederek liste bitince bir tane değer döner. 
"""

from functools import reduce  # reduce fonksiyonu son sürümlerde functools modülüne taşındı.
a = reduce(lambda x,y : x + y , [12,18,20,10])
print(a)

"""
Burada sonuç neden 60 çıkıyor bakalım. İlk önce 12 ve 18 değeri fonksiyona argüman olarak gidiyor ve toplanarak 
sonuç 30 çıkıyor. Daha sonra 30 değeriyle bir sonraki eleman olan 20 değeri toplanıyor ve sonuç 50 çıkıyor. 
En son 50 değeriyle listenin en son elemanı olan 10 değeri toplanıyor ve liste bittiği için sonuç 60 çıkıyor. 
Bunu aşağıdaki resimde görebiliriz.
"""

b = reduce(lambda x,y : x * y , [1,2,3,4,5])
print(b)

c = reduce(lambda x,y : x * y , [3,4,5,10])
print(c)


# reduce ile max fonksiyonu
def maksimum(x,y):
    if (x > y):
        return x
    else:
        return y

reduce(maksimum, [-2,1,100,35,32])