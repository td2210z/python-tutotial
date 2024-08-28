
from functools import cmp_to_key



if __name__ == '__main__':
	# s = input()
	# sum = 0
	# for x in s:
	# 	sum += int(x)
	# print(sum)
	s = list(input())
	s = [int(x) for x in s]
	print(sum(s))