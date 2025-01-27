a=input()
b=input()

ahour=int(a[0:2])
bhour=int(b[0:2])

amin=int(a[3:5])
bmin=int(b[3:5])

asec=int(a[6:8])
bsec=int(b[6:8])

if(bsec<asec):
    bsec+=60
    amin+=1

sec = bsec - asec

if(bmin<amin):
    bmin+=60
    ahour+=1

min = bmin - amin

hour = bhour - ahour
if(hour<0):
    hour+=24

if(hour == 0 and min == 0 and sec == 0):
    hour=24


sec = '{0:02d}'.format(sec)
min = '{0:02d}'.format(min)
hour = '{0:02d}'.format(hour)


print(hour+ ":" + min + ":" + sec)