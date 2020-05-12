print("hoş geldiniz sizden iki sayı isteyecegiz ve bunların obeb ve okeki hesaplanacak")


a=int(input("1.sayınız::"))
b=int(input("2.sayınız::"))
bölenler=[]
obeb=1
if a < 0 or b < 0:
    print("negatif sayı veya sayılar girilemez:)")
elif a == 0 or b == 0:
    print("sayılarımızdan en az birisi sıfır olamaz:)")



elif a > b:
    for i in range(1, a):
        if a % i == 0 and b % i == 0:
            bölenler.append(i)
            obeb = obeb * i
else:
    for i in range(1, a):
        if a % i == 0 and b % i == 0:
            bölenler.append(i)
            obeb = obeb * i

okek=(a//obeb)*(b//obeb)*obeb #burda okeki hesapladık  parantezlerde her ikisini ortak bölmeyen tam kısmı bulduk  sayılarda ortak bölen 1 den başka yoksa sayıların çarpımı okekleridir

print(f"sayılarının bölenleri {bölenler} \n obebi{obeb} \n okeki {okek}")
