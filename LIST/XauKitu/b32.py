
from functools import cmp_to_key
from math import *


def nt(n):
	if n < 2:
		return False
	for i in range(2 , isqrt(n) + 1):
		if n % i == 0:
			return False
	return  n>1

# def cs(n):
# 	while n != 0:
# 		res = n % 10
# 		if (not(res == 2 or res == 3 or res == 5 or res == 7)):
# 			return False
# 		n //= 10
# 	return True

def cs(s):
	tong =0
	for x in s:
		tong += int(x)
		if x in not '2357':
			return False
	return nt(tong)

def tong(n):
	sum =0
	while(n != 0):
		sum += n % 10
		n //= 10
	return nt(sum)

if __name__ == '__main__':
	n = int(input())
	if cs(n) and tong(n):
		print("YES")
	else:
		print("NO")