#!/bin/sh
for i in {1..20}
  do
       python ~/CPEB3/analysis/Convert_openmm.py end-$i.pdb *.fasta      
  done
