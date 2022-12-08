# def tam_sayiya_cevir():
#     girdi = input("Bir ondalik sayi giriniz: ")

#     try:
#         girdi = float(girdi)
#         print("yuvarlama islemi sonucu : {}".format(round(girdi)))
#         sonuc_mesaji = "basarili"
#     except:#kodun hata vermesine izin vermeden kullanıcı girişinin hatalı olduğuna dair mesaj çevirmesini sağlar.
#         print("{} girdisi ondalik tipe cevrilemiyor".format(girdi))
#         sonuc_mesaji = "basarisiz"
#     finally:
#         print("tam sayiya cevirme islemi {} olarak tamamlandi!".format(sonuc_mesaji))

# tam_sayiya_cevir()

vatandas = {
    'ad': 'yasin',
    'tc': '3131'
}

try:
    print(vatandas[-1])
except IndexError:
    print("Indexlememeye calistiginiz eleman listenin disinda")
except KeyError:
    print("Aranan dict'de verilen key mevcut degil")
except:
    print("kod duzgun calismio")