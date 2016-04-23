#! /usr/bin/python

import sys

if __name__ == "__main__":

	for i in range(100):
		print i
		if i  == 20:
			print "finish"
			sys.exit()
