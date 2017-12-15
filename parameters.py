import math

global pi,degtorad,dtoyr,c,kpctom,yrts,Vs,Rskpc,conversion
pi = math.pi
degtorad= pi/180.0
dtoyr = 1.0/365.25
c = 299792458.0 #m/s
kpctom = 30856775714409184000.0
yrts = 365.25*24.0*3600.0
conversion = 1000.0/(c*yrts*pow(10.0,6.0))

## terms below have errors, we will add those later

Vs = 240.0 #km/s
sigVs = 8.0

Rskpc = 8.34 #kpc
sigRs = 0.16 
'''
Vs = 220.0 #km/s
sigVs = 0.0

Rskpc = 8.00 #kpc
sigRs = 0.50 
'''

b0reid14 = -0.2 # km s^-1 kpc^-1, (dV/dR)
sigb0r = 0.4
b0dt91 = 0.00 # km s^-1 kpc^-1, (Vs/Rs)*(dV/dR)
sigb0dt = 0.03

'''
Vs = 220.0 #km/s
sigVs = 0.0

Rskpc = 8.00 #kpc
sigRs = 0.50 

b0reid14 = -0.2 # km s^-1 kpc^-1, (dV/dR)
sigb0r = 0.4
b0dt91 = 0.00 # km s^-1 kpc^-1, (Vs/Rs)*(dV/dR)
sigb0dt = 0.03
'''
#-----Converted to string----to be used in rounding off-----
'''
Vsraw = '240.0' #km/s
sigVsraw = '8.0'

Rskpcraw = '8.34' #kpc
sigRsraw = '0.16' 

b0reid14raw = '-0.2' # km s^-1 kpc^-1, (dV/dR)
sigb0rraw = '0.4'
b0dt91raw = '0.00' # km s^-1 kpc^-1, (Vs/Rs)*(dV/dR)
'''
sigb0dtraw = '0.03'
