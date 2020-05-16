

#faktöriyel hesaplma:
print("sizden bir sayı istenecek ve o sayınız faktöriyeli hesaplanacak")

def faktoriyel(sayı):
    number=1
    for i in range(1,sayı+1):
        number=number*i
    print(f"{sayı} sayısının faktöriyeli:{number} dır")


sayınız=int(input("sayınız nedir:"))

faktoriyel(sayınız)



#girdiginiz cümlede kaç sesli harf vardır
cümle=input("cümleniz")

ax=cümle.replace(" ","")
p=0
sesli_harf="AEUÜIİOÖaeuüiıoö"
k=0
for i in ax:
    p=p+1
    if i in sesli_harf:
        k=k+1

print(f"cümlniz {p} harflidir ve {k} sesli harf vardır")

#sayı tahmin oyunu:

import random as rnd
import time
print("*"*20)
print("SAYI TAHMİN OYUNU")
print("*"*20)
name=input("isminiz nedir")
sayi=rnd.randint(0,31)


sayac=0
while True:
    sayac+=1
    tahmin = int(input("sayınız çıkmak için 0 tuşla"))

    if tahmin==0:
        print("sistem kapatılıyor...")
        time.sleep(2)
        break


    elif tahmin>sayi:
        print("sayıyı küçült")
    elif sayi>tahmin:
        print("sayıyı yükselt")


    elif tahmin==sayi:
        print(f"tebrikler kzandın:{name} {sayi} sayısını {sayac} kerede bildiniz")


#iki sayı arasında asal sayı bulma
dizi=[2]
sayi=int(input("1.sayınız"))
sayi_2=int(input("2.sayınız"))
for x in range(sayi,sayi_2+1):
    for asal in range(2,x):
        if x%asal==0:
            break
        elif x%asal !=0 and (asal==x-1):
            dizi.append(x)
print(dizi)