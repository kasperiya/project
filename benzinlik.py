
print("hoş geldiniz benzinligimize \n "
      "1-fiyatlarımız  \n"
      "2-benzin stogumuz\n"
      "3-satıs yapmak\n"
      "4-fiyat güncelle\n"
      "5-çıkış")
class fiat():
    lpg=2.75
    motorin=3.78
    dizel=4.95
    benzin_stock=750
    miktar=0


    def write(self):
        print(f"lpg nin fiyatı{self.lpg}\n motorin fiyatı {self.motorin}\ndizel in fihyatı{self.dizel}\n")
    def stock(self):
        print(f"benzin stogumuz:{self.benzin_stock} lt dir")
    def satis(self):

       self.miktar = int(input("ne kadar benzin alacaksınız"))
       secim = int(input("hangsiniz seçtiniz\n"
                         "1-lpg\n"
                         "2-motorin\n"
                         "3-dizel"))
       if self.miktar > self.benzin_stock:
           print("yeterli miktar yok")

       elif self.miktar < 0:
           print("negatif girilmez")

       elif secim == 1:
           benzin_yeni_stock=self.benzin_stock-self.miktar
           self.benzin_stock=benzin_yeni_stock
           print(f"miktarınız:{self.miktar}\n fiyat:{self.lpg}\n tutar{self.lpg * self.miktar}\n kalan benzin stogu{self.benzin_stock}")
       elif secim == 2:
           benzin_yeni_stock = self.benzin_stock - self.miktar
           self.benzin_stock = benzin_yeni_stock
           print(f"miktarınız:{self.miktar}\n fiyat:{self.motorin}\n tutar{self.motorin * self.miktar}\n kalan benzin stogu{self.benzin_stock}")
       elif secim == 3:
           benzin_yeni_stock = self.benzin_stock - self.miktar
           self.benzin_stock = benzin_yeni_stock
           print(f"miktarınız:{self.miktar}\n fiyat:{self.dizel}\n tutar{self.dizel * self.miktar}\n kalan benzin stogu{self.benzin_stock}")
    def upgraded(self):
        kim=int(input("hangisini günceleyeceksin\n "
                      "1-lpg\n"
                      "2-motorin\n"
                      "3-dizel" ))
        miktar=float(input("ne kadar zam yapacaksın"))

        if kim==1:
            yeni_fiat=self.lpg+miktar
            self.lpg=yeni_fiat
            print(f"lpg nin yeni fiatı {self.lpg}")
        elif kim==2:
            yeni_fiat=self.motorin+miktar
            self.motorin=yeni_fiat
            print(f"motorinin yeni fiyatı{self.motorin}")
        elif kim==3:
            yeni_fiat=self.dizel+miktar
            self.dizel=yeni_fiat
            print(f"dizel in fiyatı {self.dizel}")


money=fiat()
while True:
    secim = int(input("seçiminiz"))
    if secim == 1:
        money.write()
    elif secim == 2:
        money.stock()
    elif secim == 3:
        money.satis()
    elif secim == 4:
        money.upgraded()
    elif secim == 5:
        break
    else:
        continue
