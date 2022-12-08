harfler = ['a','b','c','d'] * 100
for index, harf in enumerate(harfler):
    if harf == 'c':
        print("{} harfi {}. indexte".format(harf,index))
        break #çalışmayı durdurur

for sayi in range(1,31):
    if sayi%2==0:
        continue #herhangi bir şey yapma
    print(sayi)

for sayi in range(1,31):
        if sayi < 20:
            pass #burayı geç oluşturmadığın kod blogunu hatasız çalışmasını sağlayabilirsin.
        else:
            print(sayi)