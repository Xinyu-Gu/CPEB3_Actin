for i in {2..35}
 do
    cd P$i
#	rm trial.*
#	rm -r __pycache__/
#	rm info.dat
#	rm frag_table.npy
#	rm analysis_commandline_args.txt
#        cp ../mm_* .
       sbatch job.slurm
    cd ../
 done
