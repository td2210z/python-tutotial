
from functools import cmp_to_key




class nv2:
	def __init__(self , ma , name , gt , ns , dc , mst , nkhd):
		self.ma = format(ma , '05d')
		self.name = name
		self.gt = gt
		self.ns = ns
		self.dc = dc
		self.mst = mst
		self.nkhd = nkhd
	def read3(self):
		if self.ns[1] == '/':
			self.ns = '0' + self.ns
		if self.ns[4] == '/':
			self.ns = self.ns[0:3] + '0' + self.ns[3:]
		if self.nkhd[1] == '/':
			self.nkhd = '0' + self.nkhd
		if  self.nkhd[4] == '/':
			self.nkhd = self.nkhd[0:3] + '0' + self.nkhd[3:]
	def get_ns(self):
		return self.ns
	def get_ma(self):
		return self.ma
	def __str__(self):
		return f'{self.ma} {self.name} {self.gt} {self.ns} {self.dc} {self.mst} {self.nkhd}' 


def cmp(a , b):
	ns1 = a.get_ns()
	ns2 = b.get_ns()
	res1 = list(map(int , ns1.split('/')))
	res2 = list(map(int , ns2.split('/')))
	for i in range(-1 , -4 , -1):
		if res1[i] != res2[i]:
			return res1[i] - res2[i]
	ma1 , ma2 = a.get_ma() , b.get_ma()
	if ma1 < ma2:
		return -1
	else:
		return 1







if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		p = nv2(i+1 , input() , input() , input() , input() , input() , input())
		p.read3()
		a.append(p)
	a.sort(key = cmp_to_key(cmp))
	for x in a:
		print(x)
