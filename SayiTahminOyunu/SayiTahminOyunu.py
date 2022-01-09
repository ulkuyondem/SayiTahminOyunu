import random
from types import coroutine

randomSayi = random.randint(1, 100)
tahminSayisi = 0
print("Oyunden Çıkmak İçin '0' Kullanınız")

while True:
    sayi = int(input("Tahmin Sayınızı Giriniz:"))
    tahminSayisi += 1
    if (sayi == 0):
        print("Oyunden Çıkış Yaptınız")
        break
    elif (sayi < randomSayi):
        print("Daha Büyük Bir Sayı Giriniz")
        continue
    elif (sayi > randomSayi):
        print("Daha Küçük Bir Sayı Giriniz")
        continue
    else:
        print("Tebrikler Buldunuz!!! Rastgele Sayi = {0} " .format(randomSayi))
        print("{0} Kere Sayıyı Tahmin Ettiniz." .format(tahminSayisi))

