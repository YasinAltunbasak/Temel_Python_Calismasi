a = 2
b = 5
c = 3

if a+b == c:
    print("a+bnin toplamı cdir")
elif a+b > c:
    print("a+bnin toplamı cden büyüktür")
else:
    print("a+bnin toplamı cden küçüktür")



liste = ['a', 'b','c', 'd']

hedef = 'e'
if hedef in liste:
    print('aha burada')
else:
    liste.append(hedef+ ' eklenen')
    print("listeye ekledim.")
    print("güncel liste {}\n" .format(liste))

#Donguler(loops)
#for

erkekler = ["hasan", "basri", "fuat", "receb", "haydar"]

for erkek in erkekler:
    print(erkek)

mercimek_sayisi = 0

for mercimek in erkekler:
    mercimek_sayisi = mercimek_sayisi +1
    print(mercimek_sayisi, mercimek )

x = 0

while x < 10:
    print("{} degeri 10'dan kucuktur".format(x))
    x += 1
else:
    print("{} degeri 10dan kucuk degil".format(x))
    
sayi = 5
sonuc = 1

while sayi > 1:
    sonuc = sonuc * sayi
    sayi -= 1
    print(sonuc)

    