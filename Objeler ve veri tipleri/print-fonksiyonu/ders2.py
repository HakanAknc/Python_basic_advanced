"""
Formatlama
Programlama yaparken bazı yerlerde bir stringin içinde daha önceden tanımlı string,float, int vs. değerleri yerleştirmek isteyebiliriz. 
Böyle durumlar için Pythonda format() fonksiyonu bulunmaktadır. 
Örneğin, programımızda 3 tane tamsayı değerimiz var ve biz bunları bir string içinde ekrana basmak istiyoruz. Bunun için format() fonksiyonunu kullanabiliriz
"""

# Burada 3 tane süslü parantezimiz ({}) var ve bunların yerine sırasıyla format fonksiyonun içindeki değerler geçiyor.
print("{} {} {}".format(3.1423,5.324,7.324324))

a = 3
b = 4
print("{} + {} 'nin toplamı {} 'dır".format(a,b,a+b))

# Süslü parantezlerin içindeki sayılar format fonksiyonun içinden hangi sıradaki değerin geleceğini söylüyor.
print("{1} {0} {2}".format(43,"Murat",54))

# Süslü parantezlerin içindeki kullanım ondalıklı kısmın sadece 2 basamağına kadar almak istediğimiz söylüyor.
"{:.2f} {:.2f} {:.3f}".format(3.1463,5.324,7.324324)