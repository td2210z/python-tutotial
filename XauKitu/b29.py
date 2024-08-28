



if __name__ == '__main__':
	s = input()
	t = ''
	for x in s:
		if x.isalpha():
			t += ' '
		else:
			t += x
	b = list(map(int , t.split()))
	print(sum(b))