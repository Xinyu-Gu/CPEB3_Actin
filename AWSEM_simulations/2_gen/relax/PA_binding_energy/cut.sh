for i in {2..24}
 do
	sed -n '/ H *'$i' /p' test.pdb >>P1.pdb        
 done

for i in {6..28}
 do
        sed -n '/ H *'$i' /p' test.pdb >>P2.pdb
 done

for i in {3..5}
 do
   for j in {1..25}
      do 
         sed -n '/ H *'$[4*($i-3)+7+$j]' /p' test.pdb >>P$i.pdb
      done
 done

for i in {6..11}
 do
   for j in {1..24}
      do
         sed -n '/ H *'$[4*($i-6)+19+$j]' /p' test.pdb >>P$i.pdb
      done
 done

for i in {12..35}
 do
   for j in {1..25}
      do
         sed -n '/ H *'$[4*($i-12)+42+$j]' /p' test.pdb >>P$i.pdb
      done
 done
