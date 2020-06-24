import numpy as np

a=np.loadtxt("inter.log")

mean=[]

for i in range(1,len(a[0])):
	mean.append(np.mean(a[:,i]))

np.savetxt("mean.log",mean,fmt='%-8.2f',newline=' ')
