def karesini_al(x):
    return x**2


print(karesini_al(7))

sayilar = [*range(1,6)]#list(range(1,6)) ile aynıdır

for index in range(len(sayilar)):
    sayilar[index] = karesini_al(sayilar[index])

print(sayilar)

#bunun yerine map hazır fonksiyonunu kullanırız
#map(func,iter1)
#elimizdeki fonksiyona elimizdeki datanın elemanlarını sırasıyla göderir ve sonucu tek bir obje olarak geri döndürür.
sayilar2 = [*range(1,8)]
print([*map(karesini_al, sayilar2)])#gönderdiğimiz veri liste tipinde olduğu için map fonksiyonunu liste okumaya uygun hale getirdik(*map)

#lambda
sayilar3 = list(range(1,7))#[*range(1,7)] ile aynı şey
print(list(map(lambda x: x**2, sayilar3)))#lambda basit fonksiyonları tek satıra indirgeyip tasarruf yapmamızı sağlayan bir fonksiyonddur.

sayilar4= [*range(1,10)]
print([*filter(lambda x: x if x%2==0 else None, sayilar4)])