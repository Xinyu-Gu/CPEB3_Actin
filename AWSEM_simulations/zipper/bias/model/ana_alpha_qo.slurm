#!/bin/bash

#SBATCH --job-name=xg23
#SBATCH -o trial-alpha-qo.out
#SBATCH -e trial-alpha-qo.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=interactive
#SBATCH --time=00:30:00
#SBATCH --mem=10G
#SBATCH --export=ALL


python3 mm_analysis_alpha_qo.py zip --thread 1
