

from functools import cmp_to_key

def tn(s):
	t = s[::-1]
	if s == t:
		return True
	else:
		return False

if __name__ == '__main__':
	s = input()
	a = s.split()

	se = set({})
	b = []
	for x in a:
		if tn(x) and x not in se:
			b.append(x)
			se.add(x)
	b.sort(key = lambda x : len(x))
	print(' '.join(b))
