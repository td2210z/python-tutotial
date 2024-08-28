
from functools import cmp_to_key
from math import *


def check(s):
	t = s[::-1]
	return s == t and '6' in s

if __name__ == '__main__':
	s = input()
	if check(s):
		print("YES")
	else:
		print("NO")