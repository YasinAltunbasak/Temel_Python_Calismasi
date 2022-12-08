#2.3 ve 5.6'nın toplama işlemininin veri tipi
print(2.3+5.6)
print(type(2.3+5.6))

strvar = "Mercimek Üyeleri"
#split komutuyla ayırma
print(strvar.split('e'))

liste = [1, 3, 'b', 'mercimek', 6, 3]
#tersten yazdırma
liste.reverse()
print(liste)

#dictionary içinde anahtar değeri değiştirmek 
myDict = {
    'name':'Yoshi',
    'age': '22',
    'location': 'Isparta'
     }
print(myDict)
myDict['name'] = 'Yasin'
print(myDict)

# print komutu ile ve print komutsuz yazdırmanın farkı nedir? Her durumda birbiri yerine kullanılabilir mi?
# print ile istedigimiz kadar satir yazdirabiliriz, 
# print kullanilmazsa sadece son satir yazdirilir

# String ifadelerinin içerisinde \t ile \n kullanmanın farkı nedir?
# t tab ifadesidir, bir kac satir bosluk birakir, 
# n ifadesi yeni satira gecirtir

# değişken isimlendirmelerinde dikkat edilmesi gereken hususlar nelerdir?
# bosluk, rezerve edilmis karakterler kullanilamaz, 
# degisken ismi sayi ile baslayamaz

# [] {} ve () işaretlerini veri tipleri ile eşleştirin:
# '' -> String 
# [] -> liste
# {} -> dictionary
# () -> tuple, set