
from functools import cmp_to_key


if __name__ == '__main__':
	s = input()
	# ans = len(s)
	# for i in range(len(s)):
	# 	for j in range(i + 1 , len(s)):
	# 		if s[i] == s[j]:
	# 			ans += 1
	# print(ans)
	ans = len(s)
	cnt = [0] * 256
	for x in s:
		cnt[ord(x)] += 1

	for i in range(0 , 256):
		if cnt[i] != 0:
			ans += cnt[i] * (cnt[i] -1) //2
	print(ans)


