"""
Modül Kullanımı - math Modülü
Bu derste Pythonda modüller nasıl kullanılır öğrenmeye çalışacağız. Ayrıca bir modülü içeri aktarmanın değişik yöntemlerini göreceğiz.

İsterseniz hazır bir modül olan math modülünü kullanmaya başlayalım.
"""
"""
Yöntem1 - import modül_adı
Bir modülü içeri aktarmak yani programımıza dahil etmek için import modül_adı yazabiliriz. İsterseniz bunun için math modülünü içeri aktaralım.
"""

import math # Modülü içeri aktarıyoruz. Artık bu modülün tüm fonksiyonlarını kullanabiliriz.
# print(dir(math))  # Math modülünün içindekileri görmek için dir fonksiyonunu kullanabiliriz.

# print(help(math)) # Fonksiyonların görevlerini görebilmek için help fonksiyonunu kullanabiliriz.

"""
Peki bu içeri aktarma yöntemiyle math modülünün herhangi bir fonksiyonunu nasıl kullanacağız ?

----------------------------------------------------------------------------------------------------------------------------

        modül_adı.fonksiyonadı()

----------------------------------------------------------------------------------------------------------------------------

Örneğin ilk olarak math modülünün içindeki factorial fonksiyonu ne iş yapıyor bakalım.
"""

# print(help(math.factorial))
print(math.factorial(5))
print(math.factorial(10))

# print(help(math.floor))
print(math.floor(5.4))
print(math.floor(3.5))

# print(help(math.ceil))
print(math.ceil(5.4))
print(math.ceil(3.5))

print(*"----------")
print(*"----------")
"""
Peki biz bir modülü kendi belirlediğimiz isimle nasıl kullanıyoruz ? Bunun için de şu şekilde bir şey yapacağı
"""
import math as matematik
print(matematik.factorial(6)) # Modülü artık matematik ismiyle kullanabiliriz.
print(matematik.factorial(0))

"""
Yöntem2 - from modül_adı import *
Bir modülü programımıza dahil etmek için bu yöntemi de kullanabiliriz. İsterseniz math modülünü bu yöntem içeri aktaralım.
"""

from math import * # Yıldızın anlamı math modülünün içindeki bütün fonksiyonları almak istediğimizi belirtiyor.
# print(dir(math))

"""
Peki böyle bir durumda math modülünün içindeki fonksiyonları nasıl kullanacağız. Bunun için modül ismini yazmamıza gerek kalmamaktadır.

-------------------------------- fonksiyon_adı() ----------------------------------
"""

print(factorial(5))