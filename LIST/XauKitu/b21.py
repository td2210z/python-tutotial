



if __name__ == '__main__':
	s = input().lower()
	t = input().lower()

	a = set(s.split())
	b = set(t.split())
	
	print(' '.join(sorted(a.intersection(b))))


