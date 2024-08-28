
from functools import cmp_to_key



if __name__ == '__main__':
	s = input()
	t = input()
	s1 = set(s)
	s2 = set(t)
	

	res1 = s1.difference(s2)
	res2 = s2.difference(s1)
	print(''.join(sorted(res1)))
	print(''.join(sorted(res2)))
