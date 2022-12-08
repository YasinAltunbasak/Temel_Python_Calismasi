def decorator_ornek(func):
    def ic_fonksiyon():
        print("Decorate durum")
        func()
    return ic_fonksiyon
 
def fonksiyon():
    print("Ana fonksiyon")
    
 
print(fonksiyon())
nesne = decorator_ornek(fonksiyon)
print(nesne())

@decorator_ornek
def fonksiyon():
    print("Ana Fonksiyon 2")


print(fonksiyon())

def yildiz(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner
 
def yuzde(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner
 
@yildiz
@yuzde
def yaz(msg):
    msg = input("Mesajinizi girin: ")
    print(msg)

print(yaz("a"))
 




