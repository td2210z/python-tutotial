


from functools import cmp_to_key
from math import *

def check(s):
	if s == '0':
		return True
	tmp = s[-2:]
	if tmp % 25 == 0:
		return True
	else:
		return False


if __name__ == '__main__':
	s = input()
	if check(s):
		print("YES")
	else:
		print("NO")
