
from functools import cmp_to_key
from math import *


def check(s):
	for i in range(1 , len(s)):
		if s[i] < s[i-1]:
			return False
	return True

def ans(s):
	for i in range(1 , len(s)):
		if s[i] > s[i-1]:
			return False
	return True

if __name__ == '__main__':
	s = input()
	if check(s) or check1(s):
		print("YES")
	else:
		print("NO")