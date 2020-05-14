import random as rnd 
print("tv yi açmak için simgesine 1 e bas\n"
    "tv durumunu ögrenmek için 2 ye bas\n"

    "ses ayarları için 3 e basınız\n"
    "kanal listesi için 4 e basınız\n"
    "kanallar arası gezme için 8 e basın\n"
    "izlediginiz  kanalı ögrenmek için 5 e bas\n"
    "kanal ekleme için 6 e basın\n"
    "rastgele kanal açmak için 7 e bas \n"
    "kapatmak için (0) simgesine bas\n"
)
class kontrol():
    ses=1
    tv_list=["trt","kanal d","star tv","atv"]
    tv_durumu="açık"
    kanal_no=0

    def tv_aç(self):
       if self.tv_durumu=="kapalı":
           self.tv_durumu = "açık"
           print(f"tv açılıyor.... tv durumu:{self.tv_durumu}")
       elif self.tv_durumu=="açık":
           print(f"tv zaten açık tv durumu:{self.tv_durumu}")
    def tv_kapat(self):
     if self.tv_durumu=="açık":
         tv_durumu = "kapalı"
         print(f"tv kapatılıyor tv durumu:{self.tv_durumu}")

    def tv_bilgi(self):
        print(f"tv durumu:{self.tv_durumu}")

    def ses_ayar(self):
        while True:
            secim=input("ses azaltmak için bu simgeye bas ('<') ses artırmak için bu simgeye bas('>')")
            if secim=="<":
                if self.ses!=0:
                    self.ses=self.ses-1
                    print(f"ses düzeyi{self.ses}")
                elif self.ses==0:
                    print(f"ses daha fazla azalamaz ses düzeyi:{self.ses}")
            elif secim==">":
                if self.ses!=34:
                    self.ses=self.ses+1
                    print(f"ses düzeyi:{self.ses}")
                elif self.ses==34:
                    print(f"ses düzeyi artamaz ses düzeyi:{self.ses}")
            else:

                print(f"ses düzeyi:{self.ses}")
                break
               

    def k_list(self):
        print(f"kanal listesi:{self.tv_list}")
    def kanal_gezme(self):
        while True:
            gezme=input("kanal listesinde ileri için('+') simgesine basınız geri yönde gezmek için('-') simgesine basınıs")
            if gezme=="+":
                if self.kanal_no <len(self.tv_list):
                     self.kanal_no=self.kanal_no+1
                     print(f"şu an izlediginiz kanal:{self.tv_list[self.kanal_no-1]}")
                elif self.kanal_no==len(self.tv_list):
                    print(f"son kanal izlediginiz kanal:{self.tv_list[self.kanal_no-1]}")
            elif gezme=="-":
                if self.kanal_no >0:
                    self.kanal_no=self.kanal_no-1
                    print(f"şu an izlediginiz kanal:{self.tv_list[self.kanal_no]}")
                elif self.kanal_no==0:
                    print(f"son kanal daha geri gidilemez izlediginiz kanal :{self.tv_list[self.kanal_no]}")

    def izlenen_kanal(self):
        print(f"izlediginiz kanal:{self.tv_list[self.kanal_no]}")
    def kanal_ekle(self):
        isim=input("eklemek istediginiz kanal ismini yazınız:")
        self.tv_list.append(isim)  
        print(f"güncel kanal listesi:{self.tv_list}")          

    def random_kanal(self):
        rastgele_sayı=rnd.randint(0,len(self.tv_list))
        print(f"rastgele açılan:{self.tv_list[rastgele_sayı]}")


kumanda=kontrol()  

    
               
while True:
    secim=int(input("yapmak istediginiz işlem nedir"))

    if secim==1:
        kumanda.tv_aç()
    elif secim==2:
        kumanda.tv_bilgi()
    elif secim==3:
        kumanda.ses_ayar()
    elif secim==4:
        kumanda.k_list()
    elif secim==5:
        kumanda.izlenen_kanal()
    elif secim==6:
        kumanda.kanal_ekle()
    elif secim==7:
        kumanda.random_kanal()
    elif secim==8:
        kumanda.kanal_gezme()
    elif secim==0:
        kumanda.tv_kapat()
        print("sistem kapatılıyor.....")
        break

    else:
        print("tanımlı işlem degil tanım aralıgına uygun işlem yapınız")
        continue





        
  