class Ucus():
    havayolu = "THY"
    #Eğer bir class'tan nesne türetecek isek __init__ ,
    # class'ın ilk metodu olmak zorundadır.
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu
    
    def anons_yap(self):
        return "{} sefer sayili {}-{} ucusumuz {} dakika sürecektir".format(
        self.kod,
        self.kalkis,
        self.varis,
        self.sure)

    def koltuk_sayisi_guncelle(self):
         return self.kapasite - self.yolcu

    def bilet_satis(self, bilet_adedi=1):
        #self.yolcu = self.yolcu + bilet_adedi
        if self.yolcu + bilet_adedi <= self.kapasite: 
            self.yolcu += bilet_adedi
            self.koltuk_sayisi_guncelle()
            print('{} adet bilet satilmistir, kalan koltuk sayisi {}'.format(
                bilet_adedi,
                self.koltuk_sayisi_guncelle()))
        else:
            print('Islem gerceklestirilemedi. Yetersiz koltuk sayisi..')
    
    def bilet_iptal(self, bilet_adedi=1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            print('{} adet bilet iptal edilmistir, güncel koltuk sayisi {}'.format(
                bilet_adedi,
                self.koltuk_sayisi_guncelle()))
        else:
            print('Islem gerceklestirilemedi. Iptal edilecek kadar yolcu yok..')
    
ucus1 = Ucus('TR32','Sakarya','Isparta',35,200,45)

print(ucus1.anons_yap())

print(ucus1.koltuk_sayisi_guncelle())

print(ucus1.bilet_satis(20))

print(ucus1.bilet_iptal(2000))

print(ucus1.koltuk_sayisi_guncelle())