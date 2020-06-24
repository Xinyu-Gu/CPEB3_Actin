#!/bin/bash

#SBATCH --job-name=xg23
#SBATCH -o trial-beta.out
#SBATCH -e trial-beta.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=interactive
#SBATCH --time=00:30:00
#SBATCH --mem=10G
#SBATCH --export=ALL


python3 mm_analysis_beta.py zip --thread 1
