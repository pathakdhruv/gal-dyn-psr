import math
from galpy.potential import MWPotential2014
from galpy.util import bovy_conversion
from astropy import units
from galpy.potential import KeplerPotential
from galpy.potential import evaluateRforces
import parameters as par
from Excesspl import Rpkpcfunc

def MWBHRfo(bdeg,ldeg,dkpc):

    b = bdeg*par.degtorad
    l = ldeg*par.degtorad
    Rskpc = par.Rskpc
    Vs = par.Vs
    conversion = par.conversion
    Rpkpc = Rpkpcfunc(dkpc,b,l,Rskpc)
    zkpc = dkpc*math.sin(b)
    be = (dkpc/Rskpc)*math.cos(b) - math.cos(l)
    coslam =  be*(Rskpc/Rpkpc)

    MWPotential2014.append(KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(Vs,Rskpc)))

    rforce1 = evaluateRforces(MWPotential2014, Rpkpc/Rskpc,zkpc/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)

    rfsun = evaluateRforces(MWPotential2014, Rskpc/Rskpc,0.0/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)

    #rf = (rforce1-rfsun)*conversion*math.cos(b) # s-1
    rf0 = rforce1*coslam + rfsun*math.cos(l) 
    rf = rf0*conversion*math.cos(b) # s-1
    
    return rf;


