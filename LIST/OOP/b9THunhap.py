

from math import *


class nv:
	def __init__(self,ma ,name , luong , nc , cv):
		self.ma = ma
		self.name = name
		self.luong = luong
		self.nc = nc
		self.cv = cv
	def get_cong(self):
		return self.luong * self.nc
	def get_thuong(self):
		ans = self.get_cong()
		if self.nc >= 25:
			return int(0.1 * ans)
		elif self.nc >=22:
			return int(0.2 * ans)
		else:
			return 0
	def lay_phu_cap(self):
		if self.cv == 'GD':
			return 250000
		elif self.cv == 'PGD':
			return 200000
		elif self.cv == 'TP':
			return 180000
		else:
			return 150000
	def tong(self):
		return self.lay_phu_cap() + self.get_cong() + self.get_thuong()
	def __str__(self):
		return f'{self.ma} {self.name} {self.get_ong()} {self.get_thuong()} {self.tong()}'



if __name__ == '__main__':
	sv = nv('NV01' , input() , input() , int(input()) , input())
	print(sv)