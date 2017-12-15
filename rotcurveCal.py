from __future__ import print_function
import parameters as par

b0 = par.b0
R0 = par.Rskpc
v0 = par.Vs


## Reild et al 2014


R = float(input("Enter R in kpc: "))


v = v0-b0*(R-R0)


  
print ("R (kpc)"," and ","v (km/s) are (Reid 2014), v/vs: ", R, v, v/v0)
   
