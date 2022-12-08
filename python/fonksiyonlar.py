def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b

print(buyuk_sayi_dondur(3,7))

def metin_yazdir(a,b):
    buyuk_sayi = buyuk_sayi_dondur(a,b)#buyuk_sayi_dondur fonksiyonunu çağırır ve dönen sayıyı buyuk_sayi'ya atar
    sablon_text = "{} daha buyuk sayidir" .format(buyuk_sayi)
    print(sablon_text)

metin_yazdir(20,12)

print("Zeynep Aslan".split()) #ayırma metodu

def isim_soyisim_ayirma(isim_soyisim):
    isim = isim_soyisim.split()[0]
    soyisim= isim_soyisim.split()[1]
    return isim,soyisim

print(isim_soyisim_ayirma("Yasin Altunbasak"))
a, b = isim_soyisim_ayirma("Yasin Altunbasak")
print(a)
print(b)

print(" ".join(["Yasin", "Altunbasak" ]))#birlestirme metodu " ".join

def isim_soyisim_birlestir(isim, soyisim):
    return " ".join([isim, soyisim])

print(isim_soyisim_birlestir("Atahan", "Kaya"))

def tum_isim_soyisim_birlestir(*args):#*args özelliği listedeki tüm elemanlar üzerinde işlem yapmamızı sağlar.(tüm argümanlar= *args)
    return " ".join(args)#args zaten bir liste olduğu için tekrar köşeli parantez kullanmana gerek yok.

print(tum_isim_soyisim_birlestir("Fatih", "Sultan", "Mehmet", "Han", "Yigit"))

def gobek_adi_yazdir(**kwargs):
    if 'gobekadi' in kwargs:
        print(kwargs['gobekadi'])
        
    else:
        print("gobekadi yok")

gobek_adi_yazdir(adi="yasin",gobekadi ="gonzales", soyadi ="Altunbasak")