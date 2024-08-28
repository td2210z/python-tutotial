



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
	def ch5(self):
		res = self.name.split()
		ans = ' '.join(res).title()
		self.name = ans
	def khoa(self):
		return self.ma[0:4]
	def __str__(self):
		return f'{self.ma} {self.name} {self.lop} {self.email}'



if __name__ == '__main__':
	n = int(input())
	a = []
	for _ in range(n):
		s = hs1(input() , input() , input() , input())
		s.ch5()
		a.append(s)
	q = int(input())
	for _ in range(q):
		res = input()
		print('DANH SACH SINH VIEN KHOA' , res , ':')
		for x in a:
			if x.khoa() == res:
				print(x)
