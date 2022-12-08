sayilar = [1 , 2 , 7, 4, 5]
print(sayilar)
sayilar.append(0)#ekleme işlemi yapar
print(sayilar)
print(sayilar[2:6])
sayilar.pop()
print(sayilar)
sayilar.sort()
print(sayilar)

#Tuple örnekleri

tup  = (1 , 2 , 7, 4, 5)
# tup itemleri sabit tutar   
# tup[2] = 33
#TypeError: 'tuple' object does not support item assignment
print(tup.count(7))
print(tup.index(2))
# print(tup.index(8))
# ValueError: tuple.index(x): x not in tuple


Mercimek_Uyesi= {
"Lvl5":"Cem",
"Lvl12":"Mustafa",
"Lvl61":"Dinçer",
"Lvl99":"Tuğrul",
"Lvl100":"Yasin",
"Lvl10000000":"Fatih"
  }

for x,y in Mercimek_Uyesi.items():
    print(x,y)

print(len(Mercimek_Uyesi))

print(Mercimek_Uyesi.get('Lvl61'))
