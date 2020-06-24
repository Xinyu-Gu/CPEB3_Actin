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
    if r< 12.0 : return True
    else: return False


p = PDBParser(PERMISSIVE=1)
s = p.get_structure("1", "end-1.pdb")
#M = len(s[0]["A"])+len(s[0]["B"])+len(s[0]["C"])+len(s[0]["D"])
N = len(s[0]["H"])
A = len(s[0]["A"])
#sigma = np.zeros((N,M))      
#print(M,N)

ca_atoms_pdb = []
chains = s[0].get_list()
for chain in chains:
   for res in chain:
           is_regular_res = res.has_id('CA') and res.has_id('O')
           if is_regular_res:
                   ca_atoms_pdb.append(res['CA'].get_coord())
M=len(ca_atoms_pdb)
sigma = np.zeros((N,M))
print(M,N)

   
for k in range(1 ,21): 
        for i in range(0, N):
                for j in range(0, M-N+i):
                                xyz_CAi = ca_atoms_pdb[M-N+i]
                                xyz_CAj = ca_atoms_pdb[j]
                                if checkIfNative(xyz_CAi, xyz_CAj):
                                     sigma[i][j] += 1
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


single=sigma[...,750:1875]
plt.figure(figsize=(40,10))
plt.imshow(single)
plt.savefig("2gen-345-p.png")


