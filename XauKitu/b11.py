

from functools import cmp_to_key



if __name__ == '__main__':
	s = input()
	a = s.split()

	a.sort()
	print(' '.join(a))
    a.sort(key = lambda x : (len(x) , x))
    print(' '.join(a))
