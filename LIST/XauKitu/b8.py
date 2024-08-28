
from functools import cmp_to_key


if __name__ == '__main__':
	s = input()
	t = s[::-1]
	if s == t:
		print("YES")
	else:
		print("NO")
