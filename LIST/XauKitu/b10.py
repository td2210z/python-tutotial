
from functools import cmp_to_key
from collections import Counter

if __name__ == '__main__':
	s = input()
	z = s.split()
	

	print(''.join(sorted(set(z))))
	set1 = set(z)
	for x in z:
		if x in set1:
			print(x , end = ' ')
			set1.remove(x)
