from __future__ import print_function
import math
import numpy as np
import parameters as par
from ExcessZ import g
from Excesspl import aplmod
from Excesspl import Rpkpcfunc
from Excesspl import Vprat
from err_NT import errNT
from err_excesspl_Reid import err_Reid14




def calc(bdeg, sigb, ldeg, sigl, dkpc, sigd, Har):           
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      zkpc = dkpc*math.sin(b)

      adrc = aplmod(dkpc,b,l)*math.cos(b) #s^-1
      errReid = err_Reid14(bdeg, sigb, ldeg, sigl, dkpc, sigd) #s^-1
      azbcnt = g(zkpc)*math.sin(b) #s^-1
      errnt = errNT(bdeg, sigb, dkpc, sigd) #s^-1
      be = (dkpc/par.Rskpc)*math.cos(b) - math.cos(l)#remove afterwards
      Vp = par.Vs*Vprat(Rpkpcfunc(dkpc,b,l,par.Rskpc))#km/s
      Vpms = 1000.0*Vp
      Vsms = 1000.0*par.Vs
      Rs = par.kpctom*par.Rskpc #m
      Rp = par.kpctom*Rpkpcfunc(dkpc,b,l,par.Rskpc) #m
      coslam =  be*(par.Rskpc/Rpkpcfunc(dkpc,b,l,par.Rskpc))
      Vp2byRp = (Vpms*Vpms)/Rp #m/ss
      Vs2byRs = (Vsms*Vsms)/Rs #m/ss

      if Har==1:
         print ("Excess_parallel_Reid2014, Excess_z_NT95 = ", adrc,", ", azbcnt)
         
         print ("Vp/Vs= ", Vprat(Rpkpcfunc(dkpc,b,l,par.Rskpc)))
         print ("Rp' in m= ", Rp)
         print ("cos(l)= ", math.cos(l))
         print ("cos(lambda) = ", coslam)
         print ("vp2/Rp= ", Vp2byRp)
         print ("Vs2/Rs= ", Vs2byRs)
         print ("(vp2/Rp)*cos(lambda)= ", Vp2byRp*coslam)
         print ("(vs2/Rs)*cos(l)= ", Vs2byRs*math.cos(l))
      else:      
         print ("Excess_parallel_Reid2014, Excess_z_NT95 = ", adrc,"+/-",errReid, ", ", azbcnt,"+/-",errnt)
         
         print ("Vp/Vs= ", Vprat(Rpkpcfunc(dkpc,b,l,par.Rskpc)))
         print ("Rp' in m= ", Rp)
         print ("cos(l)= ", math.cos(l))
         print ("cos(lambda) = ", coslam)
         print ("vp2/Rp= ", Vp2byRp)
         print ("Vs2/Rs= ", Vs2byRs)
         print ("(vp2/Rp)*cos(lambda)= ", Vp2byRp*coslam)
         print ("(vs2/Rs)*cos(l)= ", Vs2byRs*math.cos(l))

      return None;
