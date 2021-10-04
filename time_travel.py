import math
import matplotlib.pyplot as plt
import openpyxl


#calculate time dilation

#t' = time from the stationary observer
#t= time measured by a moving object
#c= the speed of light
#V = speed of light

a=[]
b=[]



def time_dilation(velocity,t):
    c=299792458
    
    #taking the value of v for various moving objects in kilometer per hour
    conversion=(velocity)
    print(conversion)
    soli=(conversion**2/c**2)
    print(soli)

    tt=t/(math.sqrt(1-soli))
    print(tt)
    a.append(tt)
    b.append(velocity)




    
plt.plot(a,b)
#k=100000
            

for i in range(1,1000000):
    time_dilation(i,2)

plt.plot(b,a)
plt.show()
