# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 12:07:31 2016

@author: chris
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import stats
T = 1
r=0.06
m=0.03
mu = r-m
sigma = 0.2
H=99
S0 = 100
M=100
N =10
dt = T/N
t = np.linspace(0, T, N)
W = np.random.standard_normal(size = N) 
W = np.cumsum(W)*np.sqrt(dt) ### standard brownian motion ###
X = (mu-0.5*sigma**2)*t + sigma*W 
S = S0*np.exp(X) ### geometric brownian motion ###
i = 1
j=100
for i in range(0,j):
    Si=S*np.exp(X)    
    if Si>H:
        Si = Si*np.exp(X)
        i += 1
    if S<H:
        print(" Barrier crossed at ",i)
        break
    

plt.plot(t, S)
plt.show()