print("hoş geldiniz bir sayı giriniz asl mı degil mi onu ögreneceksiniz")

number=int(input("sayınız nedir:"))
dividing=[]
sayac=0


for i in range(2,number):
    if number  %  i == 0:
        sayac = sayac + 1
        dividing.append(i)


print("sayaç degeri",sayac)
print("sayının bölenleri",dividing)

if sayac>0:
    print(f" {number} sayısı asal degil")
elif sayac==0 and number==1:
    print(f" {number} sayısı asal degil")
elif sayac==0 and number<0:
    print(f"{number} sayısı negatif oldugundan asal degildir")
elif sayac==0 and number==0:
    print(f"{number} saysısı asal degil")
elif sayac==0:
    print(f"{number} sayısı asaldır")
