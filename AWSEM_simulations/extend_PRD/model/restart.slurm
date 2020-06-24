#!/bin/bash

#SBATCH --job-name=xg23
#SBATCH -o trial-1.out
#SBATCH -e trial-1.err
#SBATCH --ntasks=1
#SBATCH --partition=commons
#SBATCH --time=10:00:00
#SBATCH --mem=10G
#SBATCH --export=ALL
#SBATCH --gres=gpu:volta:1


python3 restart.py olig -m 1 -s 6e6
