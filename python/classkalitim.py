# ucus3.__dir__()
# ['kod',
#  'kalkis',
#  'varis',
#  'sure',
#  'kapasite',
#  'yolcu',
#  '__module__',
#  'havayolu',
#  '__init__',
#  'anons_yap',
#  'koltuk_sayisi_guncelle',
#  'bilet_satis',
#  'bilet_iptal',
#  '__dict__',
#  '__weakref__',
#  '__doc__',
#  '__repr__',
#  '__hash__',
#  '__str__',
#  '__getattribute__',
#  '__setattr__',
#  '__delattr__',
#  '__lt__',
#  '__le__',
#  '__eq__',
#  '__ne__',
#  '__gt__',
#  '__ge__',
#  '__new__',
#  '__reduce_ex__',
#  '__reduce__',
#  '__subclasshook__',
#  '__init_subclass__',
#  '__format__',
#  '__sizeof__',
#  '__dir__',
#  '__class__']

class Seyahat():
    
    def __init__(self, kalkis, varis):
        self.kalkis = kalkis
        self.varis = varis
        
    def anons(self):
        return "{}-{} seyahatine hosgeldiniz".format(self.kalkis, self.varis)
    
class Otobus(Seyahat):
    
    def __init__(self, mola_duraklari, kalkis, varis):
        Seyahat.__init__(self, kalkis, varis)
        self.mola_duraklari = mola_duraklari

oto1 = Otobus(['FET', 'ALAN'], 'ANT', 'BOD')

print(oto1.mola_duraklari)
print(oto1.anons())