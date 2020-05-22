import time

print("hoş geldiniz  kartınız okunnuyor........")
no_login=0
time.sleep(2)


class Bilgi():
   def __init__(self,bakiye=100,para_cek=0,para_yatir=0,password=3547):
        self.bakiye=bakiye
        self.para_cek=para_cek
        self.para_yatir=para_yatir
        self.password=password
   def BakiyeSorgula(self):
       print("işlem yapılıyor")
       time.sleep(1)
       print(f"bakiyeniz::{self.bakiye}")
   def cek(self):
       miktar=int(input("ne kadar çekeceksin"))
       if miktar>self.bakiye:
           print(f"bakiye yetersiz bakiyeniz::{self.bakiye}")
       elif miktar<0:
           print("negatif degerler çekilemez")
       else:
         self.bakiye-=miktar
       print(f"çekilen miktar::{miktar} bakiyeniz:{self.bakiye}")
   def yatir(self):
       miktar=int(input("ne kadar yatırlaca"))
       self.bakiye+=miktar
       print(f"yatırılan miktar::{miktar} yeni bakiye::{self.bakiye}")
   def new_password(self):
       new=int(input("yeni şifreniz"))
       self.password=new
       print("şifre degiştirildi")



person=Bilgi()

time.sleep(1)

while True:
    password = input("şifreniz çıkmak için çıkış yaz::")

    if password=="çıkış" or password=="ÇIKIŞ":
        print("çıkış yapılıyor")
        time.sleep(2)
        print("kartınızı alın")
        break



    elif int(password) != person.password:
        no_login += 1
        print("giriş hatalı lütfen tekrar deneyiniz")
        print(f"hatalı giriş sayısı::{no_login}")
        if no_login == 3:
            print("3 kez hatalı girdiniz")
            time .sleep(1)
            print("kart bloke ediliyor")
            break

    elif int(password) == person.password:

        while True:
            print("işlem yapılıyor")
            time.sleep(2)
            print("1--bakiye sorgula\n"
                  "2--para çek \n"
                  "3--para yatır\n"
                  "4--şifre degiştir\n"
                  "5--çıkış")
            tercih = int(input("tercihiniz::"))

            if tercih== 1:
                person.BakiyeSorgula()
            elif tercih ==2:
                person.cek()
            elif tercih ==3:
                person.yatir()
            elif tercih ==4:
                person.new_password()
            elif tercih ==5:
                print("sistem kapatılıyor ")
                time.sleep(2)
                break






