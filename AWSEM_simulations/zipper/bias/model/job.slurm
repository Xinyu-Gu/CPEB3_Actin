#!/bin/bash

#SBATCH --job-name=l
#SBATCH -o trial.out
#SBATCH -e trial.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=commons
#SBATCH --time=14:00:00
#SBATCH --mem=10G
#SBATCH --export=ALL

python3 mm_run.py zip -p CPU -t 1 -m 0 -s 3e6
