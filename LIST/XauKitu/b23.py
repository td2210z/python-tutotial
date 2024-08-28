
from functools import cmp_to_key

def cmp(a , b):
	ab = a + b
	ba = b + a
	if ab > ba:
		return -1
	else:
		return 1

if __name__ == '__main__':
	n = int(input())
	s = input().split()
	a.sort(key = cmp_to_key(key))
	print(' '.join(s))


