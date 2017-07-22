#!/usr/bin/env python

smile = open("smile.txt","w+")

for i in range(100):
	smile.write(":) ")
	if i % 10 == 0:
		smile.write("\n")
		
smile.close()
