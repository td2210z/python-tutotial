



from functools import cmp_to_key
from sys import stdin



class hs1:
	def __init__(self , ma , name , lop , email):
		self.ma = ma
		self.name = name
		self.lop = lop
		self.email = email
	def get_lop(self):
		return self.lop
	def get_ma(self):
		return self.ma
	def __str__(self):
		return f'{self.ma} {self.name} {self.lop} {self.email}'










if __name__ == '__main__':
	a =[]
	line = []
	for x in stdin:
		line.append(x[:-1])
	for i in range(0 , len(line) , 4):
		s = hs1(line[i] , line[i+1] , line[i+2] , line[i+3])
		a.append(s)
	a.sort(key = lambda x : x.get_ma())
	for x in a:
		print(x)
