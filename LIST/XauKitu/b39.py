


from functools import cmp_to_key
from math import *

def check(s):
	c , l =0 , 0
	for i in range(len(s)):
		if i % 2 == 0:
			c += int(s[i])
		else:
			l += int(s[i])
	return abs(c - l) % 11 == 0


if __name__ == '__main__':
	s = input()
	if check(s):
		print("YES")
	else:
		print("NO")
