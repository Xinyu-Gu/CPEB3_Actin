#!/usr/bin/python

# ----------------------------------------------------------------------
# Copyright (2010) Aram Davtyan, David Winogradoff and Garegin Papoian

# Papoian's Group, University of Maryland at Collage Park
# http://papoian.chem.umd.edu/

# Last Update: 03/04/2011
# ----------------------------------------------------------------------
import sys
import numpy as np
from VectorAlgebra import *

#from Bio.PDB.PDBParser import PDBParser

atom_type = {'1' : 'C', '2' : 'N', '3' : 'O', '4' : 'C', '5' : 'H', '6' : 'C'}
atom_desc = {'1' : 'C-Alpha', '2' : 'N', '3' : 'O', '4' : 'C-Beta', '5' : 'H-Beta', '6' : 'C-Prime'}
PDB_type = {'1' : 'CA', '2' : 'N', '3' : 'O', '4' : 'CB', '5' : 'HB', '6' : 'C' }

class PDB_Atom:
	no = 0
	ty = ''
	mol = 0
	res = 'UNK'
	res_no = 0
	x = 0.0
	y = 0.0
	z = 0.0
	atm = 'C'
	
	def __init__(self, no, ty, mol, res, res_no, x, y, z, atm):
		self.no = no
		self.ty = ty
		self.mol = mol
		self.res = res
		self.res_no = res_no
		self.x = x
		self.y = y
		self.z = z
		self.atm = atm
		
	def write_(self, f):
		f.write('ATOM')
		f.write(('       '+str(self.no))[-7:])
		f.write('  ')
		f.write(self.mol)
		f.write('  ')
		f.write((self.ty+'    ')[:4])
		f.write(self.res)
		f.write(' ')
		f.write('T')
		f.write(('    '+str(self.res_no))[-4:])
		f.write(('            '+str(round(self.x,3)))[-12:])
		f.write(('        '+str(round(self.y,3)))[-8:])
		f.write(('        '+str(round(self.z,3)))[-8:])
		f.write('  1.00')
		f.write('  0.00')
		f.write(('            '+self.atm)[-12:]+'  ')
		f.write('\n')

class Atom:
	No = 0
	ty = ''
	x = 0.0
	y = 0.0
	z = 0.0
	desc = ''
	
	def __init__(self, No, ty, No_m, x, y, z, desc=''):
		self.No = No
		self.ty = ty
		self.No_m = No_m
		self.x = x
		self.y = y
		self.z = z
		self.desc = desc
	
	def write_(self, f):
		f.write(str(self.No))
		f.write(' ')
		f.write(PDB_type[self.No_m])
		f.write(' ')
		f.write(str(round(self.x,8)))
		f.write(' ')
		f.write(str(round(self.y,8)))
		f.write(' ')
		f.write(str(round(self.z,8)))
		f.write(' ')
		f.write(self.desc)
		f.write('\n')

if len(sys.argv)!=3:                               # and len(sys.argv)!=5:
	print "\nCalcPdbQ.py Output_file qonuchic_flag(1 for q_o, 0 for q_w)\n"


output_file = sys.argv[1]

sigma_exp = 0.15
qo_flag = float(sys.argv[2])


from Bio.PDB.PDBParser import PDBParser

p = PDBParser(PERMISSIVE=1)

M = 159
Num = 20
eta = np.ones((Num,Num))

def computeQ(ca_atoms_pdb, ca_atoms_pdb2):
	if len(ca_atoms_pdb2)!=len(ca_atoms_pdb):
		print "Error. Length mismatch!"
		print "Pdb1: ", len(ca_atoms_pdb), "Pdb2: ", len(ca_atoms_pdb2)
		exit()

	N = len(ca_atoms_pdb)
        Q = 0.0
        norm = 0.0
	for ia in range(N-M, N):
		for ja in range(0, N-M):
			r = vabs(vector(ca_atoms_pdb[ia], ca_atoms_pdb[ja]))
			rn = vabs(vector(ca_atoms_pdb2[ia], ca_atoms_pdb2[ja]))
			if qo_flag == 1 and rn >= 9.5 and r >=9.5: continue
			dr = r - rn
			Q += exp(-dr*dr/10)
			norm += 1
		for ja in range(N-M, ia-3):
			r = vabs(vector(ca_atoms_pdb[ia], ca_atoms_pdb[ja]))
			rn = vabs(vector(ca_atoms_pdb2[ia], ca_atoms_pdb2[ja]))
			if qo_flag == 1 and rn >= 9.5 and r >=9.5: continue
			dr = r - rn
			Q += exp(-dr*dr/(2*sigma_sq[ja-ia]))
			norm += 1
        Q = Q/norm
	return Q


pdbs = []
for i in range(Num):
     ca_atoms_pdb = []
     struct_id = 'end-' + str(i)
     pdb_file = 'end-' + str(i+1) + '.pdb'
     s = p.get_structure(struct_id, pdb_file)
     chains = s[0].get_list()
     for chain in chains:
     	for res in chain:
     		is_regular_res = res.has_id('CA') and res.has_id('O')
     	        if is_regular_res:#(res_id==' ' or res_id=='H_MSE' or res_id=='H_M3L' or res_id=='H_CAS' ) and is_regular_res:
     			ca_atoms_pdb.append(res['CA'].get_coord())
     pdbs.append(ca_atoms_pdb)

sigma = []
sigma_sq = []
for l in range(0, len(ca_atoms_pdb)+1):
           sigma.append( (1+l)**sigma_exp )
           sigma_sq.append(sigma[-1]*sigma[-1])


for i in range(Num):
       for j in range(i+1,Num):
          q = computeQ(pdbs[i],pdbs[j])
          eta[i][j] = q
          eta[j][i] = q               


np.savetxt(output_file, eta, fmt='%.3f')
