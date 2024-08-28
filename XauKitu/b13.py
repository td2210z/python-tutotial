

from functools import cmp_to_key


if __name__ == '__main__':
	s = input()
	a = s.split()

	d = dict({})
	for x in a:
		if x in d:
			d[x] += 1
		else:
			d[x] = 1
	for x in sorted(d):
		print(x , d[x])
	print()
	for x ,y in d.items():
		print(x , y)
