
# class sv:
# 	def __init__(self ,  ma , name , toan , li , hoa):
# 		self.ma = ma
# 		self.name = name
# 		self.toan = toan
# 		self.li = li
# 		self.hoa = hoa
# 	def khu_vuc(self):
# 		return int(self.ma[2:3])
# 	def tong(self):
# 		ans = float(self.toan + self.li + self.hoa)
# 		pu = self.khu_vuc()
# 		if pu == 1:
# 			return float(0.5 + ans)
# 		elif pu == 2:
# 			return float(1.0 + ans)
# 		else:
# 			return float(2.5 + ans)

# 	def kq(self):
# 		ans = self.tong()
# 		if ans >= 24:
# 			return 'TRUNG TUYEN'
# 		else:
# 			return 'TRUOT'
# 	def __str__(self):
# 		return f'{self.ma} {self.name} {self.khu_vuc()} {self.tong():.1f} {self.kq()}'

from math import *

class sv:
	def __init__(self ,  ma , name , toan , li , hoa):
		self.ma = ma
		self.name = name
		self.toan = toan
		self.li = li
		self.hoa = hoa
	def khu_vuc(self):
		return int(self.ma[2])
	def tong(self):
		print(self.ma + ' ' + self.name + ' ' + str(self.khu_vuc()) , end = ' ')
		diem = self.toan + self.li + self.hoa
		kv = self.khu_vuc()
		if kv == 1:
			diem += 0.5
		elif kv == 2:
			diem += 1
		else:
			diem += 2.5
		if diem == int(diem):
			print(int(diem()) ,end= ' ')
		else:
			print('%.1f' % diem , end= ' ')
		if diem >= 24:
			print('TRUNG TUYEN')
		else:
			print('TRUOT')


if __name__ == '__main__':
	g = sv(input() , input() , float(input()) , float(input()) , float(input()))
	g.tong()