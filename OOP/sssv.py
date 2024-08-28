



from functools import cmp_to_key




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

def cmp(a , b):
	a1= a.get_lop()
	b1 = b.get_lop()
	if a1 != b1:
		if a1 > b1:
			return 1
		else:
			return -1
	else:
		m1 ,m2 = a.get_ma() , b.get_ma()
		if m1 < m2:
			return -1
		else:
			return 1









if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		p = hs1(input() , input(),input(),input())
		a.append(p)
	a.sort(key = lambda x : (x.get_lop() , x.get_ma()))
	for x in a:
		print(x)
