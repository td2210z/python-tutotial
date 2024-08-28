

from math import *

class nv:
	def __init__(self , ma , name , luong , nc, cv):
		self.ma = ma
		self.name = name
		self.luong = luong
		self.nc = nc
		self.cv = cv
	def luong_thang(self):
		return self.luong * self.nc
	def thuong(self):
		luong1 = self.luong_thang()
		
		if self.nc >=25:
			return int(0.2 * luong1)
		elif self.nc >= 22:
			return int(0.1 * luong1)
		else:
			return 0
	def phu_cap(self):
		
		if self.cv == 'GD':
			return  250000
		elif self.cv== 'PGD':
			return  200000
		elif self.cv == 'TP':
			return  180000
		else:
			return  150000
	def thu_nhap(self):
		return self.luong_thang() + self.thuong() + self.phu_cap()
	def __str__(self):
		return f'{self.ma} {self.name} {self.luong_thang()} {self.thuong()} {self.phu_cap()} {self.thu_nhap()}'




if __name__ == '__main__':
	g = nv('NV01',input() , int(input()) , int(input()) , input())
	print(g)