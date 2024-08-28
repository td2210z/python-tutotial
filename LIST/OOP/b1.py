
from math import *

class phanso:
	def __init__(self , tu , mau):
		self.__tu = tu
		self.__mau = mau
	def ans(self):
		uc = gcd(self.__tu , self.__mau)
		self.__tu //= uc
		self.__mau //= uc
	def __str__(self):
		return f'{self.__tu} / {self.__mau}'

if __name__ == '__main__':
	tu , mau = map(int , input().split())
	p = phanso(tu , mau)
	p.ans()
	print(p)