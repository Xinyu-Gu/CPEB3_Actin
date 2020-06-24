#!/bin/bash

#SBATCH --job-name=n-b
#SBATCH -o trial.out
#SBATCH -e trial.err
#SBATCH --ntasks=1
#SBATCH --partition=commons
#SBATCH --time=06:00:00
#SBATCH --mem=10G
#SBATCH --export=ALL
#SBATCH --gres=gpu:volta:1


python3 mm_run.py cpeb3-449-716 -m 1 -s 8e6
