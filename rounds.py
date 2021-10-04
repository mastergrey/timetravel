import matplotlib.pyplot as plt
from scipy import constants

c=constants.c #speed of light
cir=40030174 #circumference of eart in meters
a=[]
b=[]
speek={}





for i in range(1,1000):
    con=(i/100000)
    speed=(c*con)
    rou=(speed/cir)
    a.append(speed)
    b.append(rou)



for i in a:
    for j in b:
        speek[i]=j
plt.xlabel("speed of light")
plt.ylabel("number of rotations")
plt.plot(a,b)
plt.show()

print(speek)