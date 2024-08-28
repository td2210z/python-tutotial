
from functools import cmp_to_key



if __name__ == '__main__':
	s = input()
	t = input()
	s1 = set(s)
	s2 = set(t)
	

	giao = s1.intersection(s2)
	hop = s1.union(s2)

	print(''.join(sorted(giao)))
	print(''.join(sorted(hop)))
