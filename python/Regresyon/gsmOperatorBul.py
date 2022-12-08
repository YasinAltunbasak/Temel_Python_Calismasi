import re

def gsm_operator_bul(tel_no):
    patern = r"(\d{3})-(\d{7})"#paterndeki tipte yazıyı bulmaya çalışır.
    eslesme = re.search(patern, tel_no)
    
    if eslesme:
        gsm_kod = eslesme.groups()[0]#paternde 2 grup var  (\d{3}) ilk grup olduğu için 0. indistedir.
        print(gsm_kod)
        if gsm_kod.startswith("54"):
            return "Vodafone"
        elif gsm_kod.startswith("501") or gsm_kod.startswith("505") or gsm_kod.startswith("506"):
            return "AVEA"
        elif gsm_kod.startswith("53"):
            return "Turkcell"
        else:
            return "Sebeke bulunamadi"
    else:
        return "Patern bulunamadi"
        
tel_no = input("Telefon numaranızı girin(gsm kodundan sonra - bırakın): ")
print(gsm_operator_bul(tel_no))