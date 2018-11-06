# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 20:41:22 2018

@author: marek
"""

import math
import matplotlib.pyplot as plt
import numpy as np


def SPWMcalc(M, Udc, L_sigma):
    return (Udc/L_sigma)**2 * ((deltaT**2)/48.0)*((3.0/2.0)*M**2 \
    -((4*math.sqrt(3))/math.pi)*M**3+(9.0/8.0)*M**4)
            
def TH3PWM16calc(M, Udc, L_sigma):
    return (Udc/L_sigma)**2 * ((deltaT**2)/48.0)* \
            ((3.0/2.0)*M**2-((4*math.sqrt(3))/math.pi)*M**3+M**4)

def TH3PWM14calc(M, Udc, L_sigma):
    return (Udc/L_sigma)**2 * ((deltaT**2)/48.0)* \
            ((3.0/2.0)*M**2-((4*math.sqrt(3))/math.pi)*M**3+(63.0/64.0)*M**4)
    
def SVPWMcalc(M, Udc, L_sigma):
    return (Udc/L_sigma)**2 * ((deltaT**2)/48.0)* \
            ((3.0/2.0)*M**2-(4*math.sqrt(3)/math.pi)*M**3+\
            (9.0/8.0)*(3.0/2.0-(9.0/8.0)*math.sqrt(3)/math.pi)*M**4)

def DPWM02calc(M, Udc, L_sigma):
    return (Udc/L_sigma)**2 * ((deltaT**2)/48.0)* \
            (6*M**2-((35*math.sqrt(3))/(2.0*math.pi))*M**3+\
            (27.0/8.0+(81.0/64.0)*math.sqrt(3)/math.pi)*M**4)

def DPWM1calc(M, Udc, L_sigma):
    return (Udc/L_sigma)**2 * ((deltaT**2)/48.0)* \
            (6*M**2-(45.0/(2*math.pi)+(4*math.sqrt(3))/math.pi)*M**3+\
            (27.0/8.0+(27.0/32.0)*math.sqrt(3)/math.pi)*M**4)
            
def DPWM3calc(M, Udc, L_sigma):
    return (Udc/L_sigma)**2 * ((deltaT**2)/48)* \
            (6*M**2+(45.0/(2*math.pi)-(31*math.sqrt(3))/(math.pi))*M**3+\
            (27.0/8.0+(27.0/16.0)*math.sqrt(3)/math.pi)*M**4)
    



deltaT = 25e-6
Udc = 1500
L_sigma = 1.4e-3
aI_rms_SPWM=[]
aI_rms_TH3PWM16=[]
aI_rms_TH3PWM14=[]
aI_rms_SVPWM=[]
aI_rms_DPWM1=[]
aI_rms_DPWM02=[]
aI_rms_DPWM3=[]
diff = 0

for M in range(0,115,1):
    #Count THD for SPWM

    I_rms_SPWM = SPWMcalc(M/100.0, Udc, L_sigma)
    I_rms_TH3PWM16 = TH3PWM16calc(M/100.0, Udc, L_sigma)
    I_rms_TH3PWM14 = TH3PWM14calc(M/100.0, Udc, L_sigma)
    I_rms_DPWM02 = DPWM02calc(M/100.0, Udc, L_sigma)
    I_rms_DPWM3 = DPWM3calc(M/100.0, Udc, L_sigma)
    I_rms_DPWM1 = DPWM1calc(M/100.0, Udc, L_sigma)
    I_rms_SVPWM = SVPWMcalc(M/100.0, Udc, L_sigma)
    aI_rms_SPWM.append(I_rms_SPWM)
    aI_rms_DPWM1.append(I_rms_DPWM1)
    aI_rms_SVPWM.append(I_rms_SVPWM)
    aI_rms_TH3PWM16.append(I_rms_TH3PWM16)
    aI_rms_TH3PWM14.append(I_rms_TH3PWM14)
    aI_rms_DPWM02.append(I_rms_DPWM02)
    aI_rms_DPWM3.append(I_rms_DPWM3)
    if M == 109:
        diff = I_rms_DPWM3-I_rms_SVPWM
        print("\nDiffence between DPWM3 and SVPWM for M = 1.09 is %f" %diff)


plt.plot(np.linspace(0, 1.0, 100),aI_rms_SPWM[0:100],np.linspace(0, 1.15, 115),aI_rms_SVPWM,
         np.linspace(0, 1.15, 115),aI_rms_DPWM1,np.linspace(0, 1.15, 115),aI_rms_TH3PWM16,
         np.linspace(0, 1.15, 115),aI_rms_DPWM02,np.linspace(0, 1.15, 115),aI_rms_DPWM3,
         np.linspace(0, 1.15, 115),aI_rms_TH3PWM14)
plt.ylabel('THD')
plt.xlabel('Modulation Index')
plt.show()
   