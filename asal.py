print("hoş geldiniz bir sayı giriniz asl mı degil mi onu ögreneceksiniz")

sayi=int(input("sayınız nedir:"))
bolen=[]
sayac=0


for i in range(2,sayi):
    if sayi % i == 0:
        sayac = sayac + 1
        bolen.append(i)


print("sayaç degeri",sayac)
print("sayının bölenleri",bolen)

if sayac>0:
    print(f" {sayi} sayısı asal degil")
elif sayac==0 and sayi==1:
    print(f" {sayi} sayısı asal degil")
elif sayac==0 and sayi<0:
    print(f"{sayi} sayısı negatif oldugundan asal degildir")
elif sayac==0 and sayi==0:
    print(f"{sayi} saysısı asal degil")
elif sayac==0:
    print(f"{sayi} sayısı asaldır")
