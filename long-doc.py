#!/usr/bin/env python

import sys

f = open(sys.argv[1] + ".txt","w+")
num = int(sys.argv[2])
word = sys.argv[3]

for i in range(num):
	f.write(word)
	if i % 10 == 0:
		f.write("\n")

f.close()
