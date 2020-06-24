import numpy as np

dock=np.loadtxt("bind.log")
P=np.loadtxt("P.dat")
actin=np.loadtxt("../actin.dat")

bind=np.ones((len(P),len(P[0])))

for i in range(0,len(P)):
	bind[i][0]=i
	for j in range(1,len(P[0])-1):
		bind[i][j]=dock[i][j]-P[i][j]-actin[i][j]
	bind[i][-1]=sum(bind[i][1:-1])


np.savetxt("inter.log", bind, fmt='%-8.2f')
