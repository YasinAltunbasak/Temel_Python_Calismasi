# girdi = input("Bir sayi girin:")
# print(type(girdi))

# def uygulama():
#     girdi2 = input("Bir sayi giriniz:")
#     if int(girdi2)%2==0:
#         return('girdiniz cift sayidir')
#     elif int(girdi2)%2==1:
#         return(f'girdiniz {girdi2} sayidir')
#     else:
#         print('lutfen integer bir deger giriniz')


# print(uygulama())

def sayi_girdisi_kontrol():
    girdi =input("Bir sayi giriniz: ")
    
    if girdi.isdigit():
        print("bu bir sayi")
        return  'islemden cikiliyor...'
        
    else:
        print("bu bir sayi degil")
        return 'islemden cikiliyor...'
        

print(sayi_girdisi_kontrol())

def sayi_girdi_dongusu():
    girdi = input("Bir sayi girin")

    while not girdi.isdigit():
        print("Bu bir sayı degil!")
        girdi = input("Lütfen bir sayi girin!")

    else:
        print(f"teşekkürler bu bir sayi. Sayiniz da budur ---->{girdi} ")

sayi_girdi_dongusu()

