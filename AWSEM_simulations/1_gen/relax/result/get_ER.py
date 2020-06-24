#!/usr/bin/python2

import numpy as np

from VectorAlgebra import *
from Bio.PDB.PDBParser import PDBParser

def checkIfNative(xyz_CAi, xyz_CAj):
    v = vector(xyz_CAi, xyz_CAj)
    r = vabs(v)
    if r< 12.0: return True
    else: return False


p = PDBParser(PERMISSIVE=1)
s = p.get_structure("1", "end-1.pdb")
N = len(s[0]["H"])
A = len(s[0]["A"])

ca_atoms_pdb = []
cb_atoms_pdb = []
chains = s[0].get_list()
for chain in chains:
   for res in chain:
           is_regular_res = res.has_id('CA') and res.has_id('O')
           if is_regular_res:
                   ca_atoms_pdb.append(res['CA'].get_coord())
                   if res.has_id('CB'):
                      cb_atoms_pdb.append(res['CB'].get_coord())
                   else:                                         #For GLY
                      cb_atoms_pdb.append(res['CA'].get_coord()) #Doesn't matter beacuse CB of GLY won't be considered in simulation 
M=len(ca_atoms_pdb)
print(len(ca_atoms_pdb), len(cb_atoms_pdb))

sigma_AA = np.zeros((M,M))
dist_AA = np.zeros((M,M))
sigma_AB = np.zeros((M,M))
dist_AB = np.zeros((M,M))
sigma_BB = np.zeros((M,M))
dist_BB = np.zeros((M,M))
   
for k in range(1 ,21): 
        for i in range(M-N, M):
                for j in range(0, M-N):
                                xyz_CAi = ca_atoms_pdb[i]
                                xyz_CAj = ca_atoms_pdb[j]
                                xyz_CBi = cb_atoms_pdb[i]
                                xyz_CBj = cb_atoms_pdb[j]
                                if checkIfNative(xyz_CAi, xyz_CAj):
                                     sigma_AA[i][j] += 1
                                     dist_AA[i][j] += vabs(vector(xyz_CAi, xyz_CAj))
                                if checkIfNative(xyz_CAi, xyz_CBj):
                                     sigma_AB[i][j] += 1
                                     dist_AB[i][j] += vabs(vector(xyz_CAi, xyz_CBj))
                                if checkIfNative(xyz_CBi, xyz_CAj):
                                     sigma_AB[j][i] += 1
                                     dist_AB[j][i] += vabs(vector(xyz_CBi, xyz_CAj))
                                if checkIfNative(xyz_CBi, xyz_CBj):
                                     sigma_BB[i][j] += 1
                                     dist_BB[i][j] += vabs(vector(xyz_CBi, xyz_CBj))

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
                               if res.has_id('CB'):
                                  cb_atoms_pdb.append(res['CB'].get_coord())
                               else:                                         #For GLY
                                  cb_atoms_pdb.append(res['CA'].get_coord()) #Doesn't matter beacuse CB of GLY won't be considered in simulation

go_AA = np.ones((M,M))*99
go_AB = np.ones((M,M))*99
go_BB = np.ones((M,M))*99

for i in range(M-N, M):
      for j in range(0, M-N):
            if sigma_AA[i][j] >= 10:
                 go_AA[i][j] = dist_AA[i][j]/sigma_AA[i][j]
                 go_AA[j][i] = go_AA[i][j]
            if sigma_AB[i][j] >= 10:
                 go_AB[i][j] = dist_AB[i][j]/sigma_AB[i][j]
            if sigma_AB[j][i] >= 10:
                 go_AB[j][i] = dist_AB[j][i]/sigma_AB[j][i]
            if sigma_BB[i][j] >= 10:
                 go_BB[i][j] = dist_BB[i][j]/sigma_BB[i][j]
                 go_BB[j][i] = go_BB[i][j]

np.savetxt("go_rnativeCACA.dat", go_AA, fmt='%10.5f')
np.savetxt("go_rnativeCACB.dat", go_AB, fmt='%10.5f')
np.savetxt("go_rnativeCBCB.dat", go_BB, fmt='%10.5f')
