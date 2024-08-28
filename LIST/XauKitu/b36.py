# so chia het cho 15


from functools import cmp_to_key
from math import *

def check(s):
	last = s[-1]
	if last not in '05':
		return False
	tong = 0
	for x in s:
		tong += x
	return tong % 3 == 0


if __name__ == '__main__':
	s = input()
	if check(s):
		print("YES")
	else:
		print("NO")