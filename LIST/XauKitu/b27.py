

if __name__ == '__main__':
	s = input()
	s += s[-1]
	dem , t = 1 , s[0]
	cnt , ans = 1 , s[0]
	for i in range(1 , len(s)):
		if s[i] != s[i-1]:
			dem += 1
			t += s[i]
		else:
			if dem > cnt:
				cnt = dem
				ans = t
			elif dem == cnt:
				if t > ans:
					ans = t
			dem = 1
			t = s[i]
	print(ans)