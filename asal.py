print("hoş geldiniz bir sayı giriniz asl mı degil mi onu ögreneceksiniz")

sayı=int(input("sayınız nedir:"))
bölen=[]
sayac=0


for i in range(2,sayı):
    if sayı % i == 0:
        sayac = sayac + 1
        bölen.append(i)


print("sayaç degeri",sayac)
print("sayının bölenleri",bölen)

if sayac>0:
    print(f" {sayı} sayısı asal degil")
elif sayac==0 and sayı==1:
    print(f" {sayı} sayısı asal degil")
elif sayac==0 and sayı<0:
    print(f"{sayı} sayısı negatif oldugundan asal degildir")
elif sayac==0 and sayı==0:
    print(f"{sayı} saysısı asal degil")
elif sayac==0:
    print(f"{sayı} sayısı asaldır")
