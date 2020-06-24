#cp ../../background/3actins/info.dat actin.dat
#sed -i '1d' actin.dat

for i in {1..35}
 do
#    mkdir P$i
#    cp ../../3actins/P$i/info.dat P$i/bind.log
#    sed -i '1d' P$i/bind.log
#    cp ../../background/P$i/info.dat P$i/P.dat
#    sed -i '1d' P$i/P.dat
       
    cd P$i
      python  ../bk.py
      python ../mean.py
        tail -1 mean* >>../mean.log
        echo  >>../mean.log
    cd ../
 done
