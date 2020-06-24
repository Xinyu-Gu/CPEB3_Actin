#for j in {0..50}
# do
#    tail -250 $j/beta.dat >>b.dat
#    awk 'NR==FNR{a[FNR]=$2;next}NR>FNR{print $1, $2, a[FNR]}' $j/alpha-qo.dat $j/beta.dat  >$j-wham.dat
#
#    sed -i '1,51d' $j-wham.dat
#    echo $j-wham.dat $j 0 10000 0 >>metadata
# done
#
#awk '{printf "%s %-3s %s %s %s\n", $1, $2*0.02, $3, $4, $5}' metadata > log
#mv log metadata

#wham-2d Px=0 0.0 1.0 100 Py=0 0.1 0.8 70 0.00001 300 0 metadata pmf-mask-t5.dat 1 > wham-mask-t5.out
#wham-2d Px=0 0.0 1.0 100 Py=0 0.1 0.8 70 0.000001 300 0 metadata pmf-mask-t6.dat 1 > wham-mask-t6.out

#wham-2d Px=0 0.0 1.0 60 Py=0 0.1 0.8 35 0.00001 300 0 metadata pmf-mask-t5.dat 1 > wham-mask-t5.out
#wham-2d Px=0 0.0 1.0 60 Py=0 0.1 0.8 35 0.000001 300 0 metadata pmf-mask-t6.dat 1 > wham-mask-t6.out


wham-2d Px=0 0.0 1.0 20 Py=0 0.0 1.0 25 0.00001 300 0 metadata pmf-mask-t5.dat 1 > wham-mask-t5.out
wham-2d Px=0 0.0 1.0 20 Py=0 0.0 1.0 25 0.000001 300 0 metadata pmf-mask-t6.dat 1 > wham-mask-t6.out
#wham-2d Px=0 0.0 1.0 20 Py=0 0.1 0.8 14 0.0000001 300 0 metadata pmf-mask-t7.dat 1 > wham-mask-t7.out




