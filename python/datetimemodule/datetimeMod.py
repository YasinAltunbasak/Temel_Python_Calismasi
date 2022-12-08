import datetime
import time

from datetime import date


bugun = date.today()

print(bugun)

yarin = bugun + datetime.timedelta(days = 1)
print(yarin)

print(bugun.month)

print(date.isocalendar(bugun))

print(date.ctime(bugun))

dt =datetime.datetime(2022,12,5,23,5,23)
print(dt)

print(dt.day)

print(time.time())

baslangic_zamani = time.time()
print("baslama zamani:  {}".format(baslangic_zamani))
time.sleep(5)
bitis_zamani =time.time()
print("bitis zamani:  {}".format(bitis_zamani))
print("calisma süresi:  {}".format(bitis_zamani - baslangic_zamani))
