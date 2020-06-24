for i in {1..35}
 do
   awk '{printf "%s %s %s %s %s\n", $1, $2+1125, $3, $4, $5}' P$i.log >tmp.log
   cat frags.mem tmp.log >../P$i/P$i.mem

#   mv ../P$i/P$i.mem .
   


 done
