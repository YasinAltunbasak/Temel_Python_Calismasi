def eposta_kontrol():
    girdi = input("E-posta adresinizi giriniz: ")

    while not  ("yasinaltunbasak@gmail.com" in girdi):
        print("Yanlış eposta adresi!")
        girdi = input("Lütfen doğru eposta adresini girin: ")

    else:
        print("Yasin Bey Hoşgeldiniz!")

eposta_kontrol()