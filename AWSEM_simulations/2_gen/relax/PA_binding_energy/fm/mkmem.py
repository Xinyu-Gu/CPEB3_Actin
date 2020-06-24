#!/usr/bin/python3

import pandas as pd

a= pd.read_csv('log.mem', header=None, delim_whitespace=True)
a.columns = ['path', 'site', 'fragsite','len', 'weight']


b = a[((a.site + a.len -1) < 25) & (a.site > 1)]
b.to_csv('P1.mem', sep = ' ', index = False, header = False)

b = a[((a.site + a.len -1) < 29) & (a.site > 5)]
b.to_csv('P2.mem', sep = ' ', index = False, header = False)

for i in range(3,6):
	filename='P' + str(i) + '.mem'
	b = a[((a.site + a.len -1) < (4*(i-3)+33)) & (a.site > (4*(i-3)+7))]
	b.to_csv(filename, sep = ' ', index = False, header = False)

for i in range(6,12):
        filename='P' + str(i) + '.mem'
        b = a[((a.site + a.len -1) < (4*(i-6)+44)) & (a.site > (4*(i-6)+19))]
        b.to_csv(filename, sep = ' ', index = False, header = False)

for i in range(12,36):
        filename='P' + str(i) + '.mem'
        b = a[((a.site + a.len -1) < (4*(i-12)+68)) & (a.site > (4*(i-12)+42))]
        b.to_csv(filename, sep = ' ', index = False, header = False)
