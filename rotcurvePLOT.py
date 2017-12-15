import math
import numpy as np
import matplotlib.pyplot as plt
import parameters as par

b0 = par.b0
R0 = par.Rskpc
v0 = par.Vs

b0dt95 = 0.0

R = 0.0
Ar = []
Av_reid14 = []
Av_dt95 = []
while R <= 20.0 :
   v_reid  = v0-b0*(R-R0)
   
   v_dt95= v0*(1.0-b0dt95*(R-R0)/R0)

   #print v, R
   Av_reid14.append(v_reid)
   Av_dt95.append(v_dt95)

   Ar.append(R)
   R = R + 1.0

#print Av
#print Ar


plt.xlabel('R (kpc)')
plt.ylabel('Vp (km/s)')
plt.ylim(0,300)
plt.xlim(0,17)
plt.title('Galactic Rotation Curves')

plt.plot(Ar,Av_reid14, 'r')
plt.plot(Ar,Av_dt95, 'g')
plt.grid()
plt.show()

