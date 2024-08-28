
from functools import cmp_to_key
from math import *

def check(s):
	if len(s) == 1:
		if int(s) % 4 == 0:
			return True
		else: return False
	t = int(s[-2:])
	return t % 4 == 0

if __name__ == '__main__':
	s = input()
	if check(s):
		print("YES")
	else:
		print("NO")