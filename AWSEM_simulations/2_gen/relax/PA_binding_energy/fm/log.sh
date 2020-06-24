awk '{printf "%s %s %s %s %s\n", $1, $2-1, $3, $4, $5}' P1.mem >P1.log
awk '{printf "%s %s %s %s %s\n", $1, $2-5, $3, $4, $5}' P2.mem >P2.log
for i in {3..5}
  do
      awk -v a="$i" '{printf "%s %s %s %s %s\n", $1, $2-(4*(a-3)+7), $3, $4, $5}' P$i.mem >P$i.log
  done

for i in {6..11}
 do
      awk -v a="$i" '{printf "%s %s %s %s %s\n", $1, $2-(4*(a-6)+19), $3, $4, $5}' P$i.mem >P$i.log
 done

for i in {12..35}
 do
      awk -v a="$i" '{printf "%s %s %s %s %s\n", $1, $2-(4*(a-12)+42), $3, $4, $5}' P$i.mem >P$i.log
 done
