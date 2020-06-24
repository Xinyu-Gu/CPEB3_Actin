f = open('abd.seq', "r")
for line in f:
	seq = line.strip()

print(seq)

f1 = open('P1.seq', "w")
f1.write(seq[1:24] + '\n')
f1.close()

f1 = open('P2.seq', "w")
f1.write(seq[5:28] + '\n')
f1.close()

for i in range(3,6):
	filename='P' + str(i) + '.seq'
	f1 = open(filename, "w")
	f1.write(seq[(4*(i-3)+7):(4*(i-3)+32)] + '\n')
	f1.close()

for i in range(6,12):
        filename='P' + str(i) + '.seq'
        f1 = open(filename, "w")
        f1.write(seq[(4*(i-6)+19):(4*(i-6)+43)] + '\n')
        f1.close()

for i in range(12,36):
        filename='P' + str(i) + '.seq'
        f1 = open(filename, "w")
        f1.write(seq[(4*(i-12)+42):(4*(i-12)+67)] + '\n')
        f1.close()

