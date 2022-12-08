i = 0
#rangei hızlıca sayı listesi yapmada kullanabilirsin.
for i in range(10):
    i += 1
    print(i)

print(*range(2,15,3)) #list(range(2,15,3)) same thing

harfler = ["a","b","c","d"]

for harf in enumerate(harfler):#enumerate iki çıktı oluşturur. indis ve değer
    print(harf)

ulkeler = ['tr','us','uk']
siralamalar = range(1,4)

for ulke in zip(ulkeler,siralamalar):#iki listeyi birleştirir.
    print(ulke)