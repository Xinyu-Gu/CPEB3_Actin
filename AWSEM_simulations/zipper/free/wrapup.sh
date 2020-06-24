for i in {0..50}
  do
    cp -r model $i
    sed -i 's/0\.02\*50/0\.02\*'$i'/g' $i/mm_run*
    cd $i
      sed -n '109p' mm_run*
      sbatch job.slurm
#       tail -1 trial.out
#       cp ../*ana* .
#       sbatch ana_beta.slurm
#       sbatch ana_alpha_qo.slurm
#       rm frag*
#       rm -r __*
       
    cd ../


  done
