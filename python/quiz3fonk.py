#soru 1
def ustel_sayi_v1():
    #    """
    # parametre: a: taban sayisi  b: kuvvet (üs) sayisi
    # tip:       a: integer       b: integer
    # örnek:     a: 3             b: 2
    
    # r-return:  a üzeri b matematik isleminin sonucu
    # r-tip:     integer
    # r-örnek:   9
    # """
    tabanSayi = input("üsteli alınacak sayının tabanini girin: ")
    print("{} usteli alinacak sayi".format(int(tabanSayi)))
    ustelSayi = input("tabanin kacinci derecesini almak istediginizi girin: ")
    print(" istediginiz sayinin almak istediginiz usteli {} ".format(int(ustelSayi)))
    
    print(int(tabanSayi)**int(ustelSayi))

ustel_sayi_v1()

