


from functools import cmp_to_key
from math import *

def check(s):
	lt = 1
	n = 0
	for x in s[::-1]:
		n = n + int(x) * lt
		lt *= 2
		n %= 5
		lt %= 5
	return n % 5 == 0


if __name__ == '__main__':
	s = input()
	if check(s):
		print("YES")
	else:
		print("NO")
