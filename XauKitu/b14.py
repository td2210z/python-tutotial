

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

	vl1 , vl2 = '' , ''
	m1 , m2 = 0 , 10**9
	for x in sorted(d):
		if d[x] >=m1:
			m1 = d[x]
			vl1 = x
		if d[x] <= m2:
			m2 = d[x]
			vl2 = x
	print(vl1 , m1)
	print(vl2 , m2)
