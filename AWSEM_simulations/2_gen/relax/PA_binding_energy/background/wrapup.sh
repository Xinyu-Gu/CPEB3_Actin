for i in {1..35}
 do

    cd P$i
#      rm ana*txt
#      rm *npy
#      rm info*
#      rm trial*
#      rm -r __*
#       tail -2 *.fasta >log
#       mv log P$i.fasta
#       tail -1 *.seq >log
#       mv log P$i.seq
#       head -4 frag* >log
#       sed '1,7d' frag* > log.mem
#       awk '{printf "%s %s %s %s %s\n", $1, $2-1125, $3, $4, $5}' log.mem >tmp.mem
#       cat log tmp.mem >frags.mem
#       rm log* tmp*
#        sed -i '/NGP E/d' P$i.pdb
#        sed -i '/IPR E/d' P$i.pdb
#        sed -i '/IGL E/d' P$i.pdb
#        sed -i '/NGP D/d' P$i.pdb
#        sed -i '/IPR D/d' P$i.pdb
#        sed -i '/IGL D/d' P$i.pdb
#        sed -i '/NGP C/d' P$i.pdb
#        sed -i '/IPR C/d' P$i.pdb
#        sed -i '/IGL C/d' P$i.pdb
#        sed -n '1,/ENDMDL/p' P$i.pdb > P$i-openmmawsem.pdb
     sbatch job.slurm
    cd ../
 done
