#!/bin/bash

#SBATCH --job-name=xg23
#SBATCH -o trial.out
#SBATCH -e trial.err
#SBATCH --partition=scavenge
#SBATCH --ntasks=1
#SBATCH --time=04:00:00
#SBATCH --mem=10G
#SBATCH --export=ALL
#SBATCH --gres=gpu:volta:1


python3 restart.py dock -m 1 -s 3e6
