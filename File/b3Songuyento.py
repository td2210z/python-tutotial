
from math import *

def nt(n):
	for i in range(2 , isqrt(n) + 1):
		if n % i == 0:
			return False
	return n>1

f1 = open("input.txt" , "r")
f2 = open("output.txt" , "w")


a = list(map(int , f1.read().split()))
b = [x for x in a if nt(x)]

b.sort()
for x in b:
	f2.write(str(x)+ ' ')
f1.close()
f2.close()
