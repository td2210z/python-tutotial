
from functools import cmp_to_key

def cmp(a , b):
	ab = a + b
	ba = b + a
	if ab > ba:
		return -1
	else:
		return 1


if __name__ == '__main__':
	s = input()
	t = ''
	for x in s:
		if x.isalpha():
			t += ' '
		else:
			t += x
	a = list(map(int , t.split()))
	b = list(map(str , a))
	b.sort(key = cmp_to_key(cmp))
	print(''.join(b))