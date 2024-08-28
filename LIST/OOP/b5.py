
from math import *

class sv1:
	def __init__(self , ma , name , gt , ns , dc , mst , nkhd):
		self.ma = ma
		self.name = name
		self.gt = gt
		self.ns = ns
		self.dc = dc
		self.mst = mst
		self.nkhd = nkhd
	def ch1(self):
		if self.ns[1] == '/':
			self.ns = '0' + self.ns
		if self.ns[4] == '/':
			self.ns = self.ns[0:3] + "0" + self.ns[3:]
	def ch2(self):
		if self.nkhd[1] == '/':
			self.nkhd = '0' + self.nkhd
		if self.nkhd[4] == '/':
			self.nkhd = self.nkhd[0:3] + "0" + self.nkhd[3:]
	def ch3(self):
		tmp = self.name.split()
		res = ' '.join(tmp)
		res = res.title()
		self.name = res
	def __str__(self):
		return f'{self.ma} {self.name} {self.gt} {self.ns} {self.dc} {self.mst} {self.nkhd}'


if __name__ == '__main__':
	name = input()
	gt = input()
	ns = input()
	dc = input()
	mst = input()
	nkhd = input()
	p = sv1('00001' , name , gt , ns , dc , mst , nkhd)
	p.ch1()
	p.ch2()
	p.ch3()
	print(p)
