
from functools import cmp_to_key
from math import *

def check(s):
	tong =0
	last = int(s[-1])
	if last % 2 == 1:
		return False
	for x in s:
		tong += int(x)
	return tong % 3 == 0

if __name__ == '__main__':
	s = input()
	if check(s):
		print("YES")
	else:
		print("NO")