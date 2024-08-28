



from functools import cmp_to_key




class hs1:
	def __init__(self , ma,name , diem):
		self.ma = format(ma , '02d')
		self.ma = 'HS' + self.ma
		self.name = name
		self.diem = diem[::]
	def tinh_diem(self):
		tong = sum(self.diem) / 10
		return tong
	
	def get_ma(self):
		return self.ma
	def __str__(self):
		res = ''
		dtb = sum(self.diem) / 10
		if dtb >= 9:
			res += 'XUAT SAC'
		elif dtb >= 8:
			res += 'GIOI'
		elif dtb >= 7:
			res += 'KHA'
		elif dtb >= 5:
			res += 'TB'
		else:
			res += 'YEU'
		return f'{self.ma} {self.name} {dtb:.1f} {res}'

		



def cmp(a , b):
	a1 = a.tinh_diem()
	b1 = b.tinh_diem()
	if a1 != b1:
		if a1 > b1:
			return -1
		else:
			return 1
	else:
		m1 , m2 = a.get_ma() , b.get_ma()
		if m1 < m2:
			return -1
		else:
			return 1





if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		p = hs1(i + 1, input() , list(map(float , input().split())))
		a.append(p)
	a.sort(key = cmp_to_key(cmp))
	for x in a:
		print(x)
