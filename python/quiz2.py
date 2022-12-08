kullanici1 = {
    'ad': 'Ferhat',
    'soyad': 'Ibrik',
    'uzmanlik': ['Front-End']
}
kullanici2 = {
    'ad': 'Gokce',
    'soyad': 'Gün',
    'uzmanlik': ['Tasarim']
}
kullanici3 = {
    'ad': 'Mesut',
    'soyad': 'Gün',
    'uzmanlik': ['Front-End']
}

#ferhat ibrik kullanıcısının uzmanlık alanını döndür

print(kullanici1.get('uzmanlik'))

kullanici_listesi = [ kullanici1, kullanici2, kullanici3 ]

#uzmanlık alanı frontend olan uzmanların ismini döndür.

for kullanici in kullanici_listesi:
    if kullanici.get('uzmanlik') == ['Front-End']:
        print(kullanici.get('ad'))

#Mesut kullanicisi yazilim öğrendi bilgilerini güncelle

kullanici3['uzmanlik'].append('yazilim') 

print("{} \n" .format(kullanici3))


#birden fazla uzmanlık alanı olan yazılımcıları yazdır

for kullanici in kullanici_listesi:
    if len(kullanici['uzmanlik']) > 1:
        print("{} \n" .format(kullanici))

#yazilimci yasları bulundu. İki listeyi birleştirip 30 yaşından küçük olanı yazdır.

kullanici_yaslari = [22,34,32]

for kullanici, yas in zip(kullanici_listesi, kullanici_yaslari):
     if yas < 30:
           print(kullanici,yas)

#asal sayıinator

deger = 7
x= deger-1
while x>1:
    if deger%x==0:
        print("{} sayisi asal degil" .format(deger))
        break
    else:
        x-=1
else:
    print("{} sayisi asaldir" .format(deger))
    
