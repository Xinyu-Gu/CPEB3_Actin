#!/bin/bash

#SBATCH --job-name=xg23
#SBATCH -o trial.out
#SBATCH -e trial.err
#SBATCH --ntasks=1
#SBATCH --partition=commons
#SBATCH --time=12:00:00
#SBATCH --mem=10G
#SBATCH --export=ALL
#SBATCH --gres=gpu:volta:1


python3 mm_run.py olig -m 1 -s 6e6
