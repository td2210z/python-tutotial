
from functools import cmp_to_key


if __name__ == '__main__':
	s = input()
	s = s.lower()
	a = set(s)
	
	if len(a) == 26:
		print("YES")
	else:
		print("NO")