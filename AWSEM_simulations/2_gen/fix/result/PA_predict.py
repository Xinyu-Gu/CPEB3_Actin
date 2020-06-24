#!/usr/bin/python2

import matplotlib
matplotlib.use('Agg')
import matplotlib.cm as cm
import numpy as np
from matplotlib import pyplot as plt

from VectorAlgebra import *
from Bio.PDB.PDBParser import PDBParser

def checkIfNative(xyz_CAi, xyz_CAj):
    v = vector(xyz_CAi, xyz_CAj)
    r = vabs(v)
#    if r< 9.5: return True
    if r< 12.0: return True
    else: return False

expt=np.loadtxt("ABD_scaled_intensity.array")

p = PDBParser(PERMISSIVE=1)
s = p.get_structure("1", "end-1.pdb")
#M = len(s[0]["A"])+len(s[0]["B"])+len(s[0]["C"])+len(s[0]["D"])
N = len(s[0]["H"])
A = len(s[0]["A"])
sigma = np.zeros(N)      
actin = np.zeros(A)
actin_lmd = np.zeros(A)
#print(M,N)

ca_atoms_pdb = []
chains = s[0].get_list()
for chain in chains:
   for res in chain:
           is_regular_res = res.has_id('CA') and res.has_id('O')
           if is_regular_res:
                   ca_atoms_pdb.append(res['CA'].get_coord())
M=len(ca_atoms_pdb)



for k in range(1 ,21): 
        for i in range(0, N):
                for j in range(0, M-N):
                                xyz_CAi = ca_atoms_pdb[M-N+i]
                                xyz_CAj = ca_atoms_pdb[j]
                                if checkIfNative(xyz_CAi, xyz_CAj):
                                     sigma[i] += 1
                                     actin[j%A] += 1
                                     if i>50 and i<119:
                                          actin_lmd[j%A] += 1                            
        if k != 20:    
            p = PDBParser(PERMISSIVE=1)
            pdb_id = str(k+1)
            pdb_file = "end-" + str(k+1) + ".pdb"
            s = p.get_structure(pdb_id, pdb_file)
            ca_atoms_pdb = []
            chains = s[0].get_list()
            for chain in chains:
               for res in chain:
                       is_regular_res = res.has_id('CA') and res.has_id('O')
                       if is_regular_res:
                               ca_atoms_pdb.append(res['CA'].get_coord())

#np.savetxt("contactN.dat",sigma, fmt='%d')
res_id=np.arange(168,327)
plt.plot(res_id, sigma/np.max(sigma), color='tab:blue')
plt.plot(res_id, expt, color='tab:red')
plt.xlabel('Residue')
plt.legend(('Contact number','Peptide array data'), loc='upper left')
#plt.ylabel('Contact numbers/peptide array ')
plt.savefig("ABD-expt_12cutoff.png")
plt.cla()

#res_id=np.arange(1,376)
#plt.plot(res_id, actin)
#plt.xlabel('Residue')
#plt.ylabel('Contact numbers')
#plt.savefig("actin.png")
#plt.cla()
#
#plt.plot(res_id, actin_lmd)
#plt.xlabel('Residue')
#plt.ylabel('Contact numbers')
#plt.savefig("actin_ABD.png")
#plt.cla()
#
#
