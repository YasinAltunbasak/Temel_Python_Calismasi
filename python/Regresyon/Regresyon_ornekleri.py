import re

cumle = "Mustafa Kemal Atatürk, Türk asker, devlet adamı ve Türkiye Cumhuriyeti'nin kurucusudur."

patern = "Türk"

print(re.search(patern, cumle))

durum = re.search(patern, cumle)#Cumle içinde mevcut patern araması

print(durum.start())# hangi index değerinde başladğını gösterir


print(durum.end())# hangi indexte bittigini gösterir.

# coklu eslesmeler (match)

for eslesme in re.findall(patern, cumle):
    print(eslesme)

for eslesme in re.finditer(patern, cumle):
    print(eslesme.span(), eslesme.group())

cumle2 = " Korkma sönmez bu şafaklarda yüzen al sancak Sönmeden yurdumun üstünde tüten en son ocak O benim milletimin yıldızıdır parlayacak O benimdir o benim milletimindir ancak"
patern = r"\s\w{5,}"# harfli kelimeleri arar. \s boşluktan sonra anlamına gelir boşlukları değer olarak almaz


for eslesme in re.finditer(patern, cumle2):
    print(eslesme.group(), eslesme.span())

cumle3 = "En sevdigim kanal 42base."
patern = r"\w*\d+"

for eslesme in re.finditer(patern, cumle3):
    print(eslesme.group(), eslesme.span())