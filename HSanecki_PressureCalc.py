#import numpy as np 
#from scipy.integrate import quad 
#import matplotlib.pyplot as plt
from math import *

#Angle of repose
phi = radians(38) #radians

#Initial an
omega = 0
delta = 0

#load Factors
g = 9.810 
ay = 0.4
az = 2

#resultant acceleration
ayz = sqrt(ay**2+az**2)

#Angle of resultant
e = atan(ay/az)

#Bucket Dimensions 
L = 5806 #mm 
B = 3212 #mm 
h = 1640 #mm 
M = 72000 #kg 

#Lateral LoadTransfer
Ftrans = M*ay*g

#Tipper Volume
v1 = L*B*h 

#Angle of Maximum Stable embankment with symmetrical shape
beta0 = phi-e

#Overload Volume
v2 = L*(0.5*B*(0.5*B*tan(beta0)))

#Density
rho = M/((v1+v2)) #kg*mm-3 

#Hydrostatic Force
F = 0.5*rho*L*ayz*g*(h**2)
#print(F,Ftrans)

#Coefficient for Side wall 1 by H.Sanecki
KH1 = cos(e)*((cos(phi-e))**2)/((cos(e)**3))
#Coefficient for Side wall 2
KH2 = cos(e)*((cos(phi+e))**2)/((cos(e)**3))
print (KH1, KH2)

#Pressure function for Wall 1 & 2 by H.Sanecki
FH1 = F*KH1
FH2 = F*KH2
#print (FH1,FH2) 

#Coefficient for Side wall 1 by Simple BackTrack
omega = asin(Ftrans/(2*F*sin(phi)))
KS1 = cos(phi-omega)
KS2 = cos(phi+omega)
print (KS1, KS2)

#Pressure function for Wall 1 & 2 by Simple BackTrack
FS1 = F*KS1
FS2 = F*KS2
#print (FS1,FS2) 

#Check Differences
diffH = ((FH1-FH2) - Ftrans)*100/Ftrans
diffS = ((FS1-FS2) - Ftrans)*100/Ftrans
print (diffH,diffS)
