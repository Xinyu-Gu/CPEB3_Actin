import matplotlib
matplotlib.use('Agg')

import numpy as np
from matplotlib import pyplot as plt
#from scipy import signal as sig


x=np.arange(1,698)
a= np.loadtxt('mature-low.data', dtype='float')

#c= sig.savgol_filter(a,7,3,deriv=2)
#
plt.figure(figsize=(10,5))
plt.plot(x,a)
plt.xlim(0,700)
#
#
plt.xlabel('Resid', fontsize=18)
plt.ylabel('Intensity', fontsize=18)
#plt.hlines(0, 0, len(a))
plt.vlines(167, -100, 4500, colors='b', linestyles='dashed')
plt.vlines(325, -100, 4500, colors='b', linestyles='dashed')
plt.savefig('cpeb3-PA.png')
#np.savetxt('SG-7-3.npy',c,fmt='%.3f')
#plt.savefig('SG-7-3.png')
