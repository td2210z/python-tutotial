



if __name__ == '__main__':
	s = input()
	id = 0
	t = 'python'
	for x in s:
		if x == t[id]:
			id += 1
		if id == 6:
			print("YES")
			exit()
	print("NO")