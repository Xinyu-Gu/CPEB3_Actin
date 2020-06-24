#!/bin/bash

#SBATCH --job-name=xg23
#SBATCH -o trial.out
#SBATCH -e trial.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --partition=interactive
#SBATCH --time=00:30:00
#SBATCH --mem=20G
#SBATCH --export=ALL


python3 mm_analysis.py P12 --thread 12 -t P12.pdb 
