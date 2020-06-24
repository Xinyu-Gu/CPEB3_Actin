#!/usr/bin/python2

import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib import pyplot as plt

sigma = np.loadtxt('contact-hb-12.dat') 
sigma1 = np.loadtxt('contact-nohb-12.dat')
  
for i in range(0, len(sigma)):
         for j in range( i, len(sigma)):
                 sigma[i][j] = sigma1[i][j]
 

plt.imshow(sigma)
plt.colorbar()
plt.savefig("compare-contact-12.png")

