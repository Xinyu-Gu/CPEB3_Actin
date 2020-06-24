#!/usr/bin/python2

import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib import pyplot as plt

from VectorAlgebra import *
from Bio.PDB.PDBParser import PDBParser

def checkIfNative(xyz_CAi, xyz_CAj):
    v = vector(xyz_CAi, xyz_CAj)
    r = vabs(v)
    if r<12.0: return True
    else: return False

p = PDBParser(PERMISSIVE=1)
s = p.get_structure("1", "end-1.pdb")
N = len(s[0]["A"])
sigma = np.ones((N,N))*0       
   
for k in range(1 ,21): 
        ca_atoms_pdb = [] 
        chains = s[0].get_list()
        chain = chains[0]
        for res in chain:
                is_regular_res = res.has_id('CA') and res.has_id('O')
                res_id = res.get_id()[0]
                if is_regular_res:
                        ca_atoms_pdb.append(res['CA'].get_coord())
        
        for i in range( 0, len(ca_atoms_pdb) ):
                for j in range( i+4, len(ca_atoms_pdb) ):
                                xyz_CAi = ca_atoms_pdb[i]
                                xyz_CAj = ca_atoms_pdb[j]
                                if checkIfNative(xyz_CAi, xyz_CAj):
                                     sigma[i][j] += 1
                                     sigma[j][i] += 1
        if k != 20:    
            p = PDBParser(PERMISSIVE=1)
            pdb_id = str(k+1)
            pdb_file = "end-" + str(k+1) +".pdb"    
            s = p.get_structure(pdb_id, pdb_file)

plt.imshow(sigma)
plt.colorbar()
plt.savefig("contact-12.png")

np.savetxt('contact-hb-12.dat', sigma, fmt='%d')
