#!python3

#Modified by Xinyu
# transfer peptide array to residue based
# "actin" is peptide array data, single column, 72 lines
# in this case, each peptide has 25 residues
# in this case, two adjecent peptides have a shift of 4 residues

import numpy as np

raw_bg = np.loadtxt('high.raw')
raw = raw_bg - np.min(raw_bg)


a = []
m = 0
for i in range(6):
   m += raw[i]
   n = m/(25.0*(i+1))
   for j in range(4):
      a.append(n)
a.append((m+raw[6])/(25.0*7))

for l in range(1,len(raw)-6):
   m=0
   for i in range(6):
         m += raw[l+i]
   n = m/(25.0*6)
   for j in range(3):
         a.append(n)
   a.append((m+raw[l+6])/(25.0*7))

l+=1
m=0
for i in range(6):
    m += raw[l+i]
for k in range(6):
    n = m/(25.0*(6-k))
    for j in range(4):
        a.append(n)
    m -= raw[l+k]

np.savetxt('mature-high.data', a, fmt='%.3f')
