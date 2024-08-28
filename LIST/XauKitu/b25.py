
from functools import cmp_to_key


if __name__ == '__main__':
	m , s = map(int , input().split())
	lon , be = [0] * m , [0] * m
	if (s > m * 9) or (s == 0 and m >1):
		print("NOT FOUND")
	else:
		t = s
		for i in range(m):
			if s >=9:
				lon[i] = 9
				s -= 9
			else:
				lon[i] = s
				s =0
		t -= 1
		for i in range(m -1 , 0 , -1):
			if t >= 9:
				be[i] = 9
				t -= 9
			else:
				be[i] = t
				t = 0
		be[0] = t + 1
		for x in be:
			print(x ,end ='')
		print()
		for x in lon:
			print(x , end = '')



