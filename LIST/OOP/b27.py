



from functools import cmp_to_key




class nv2:
	def __init__(self , tk , mk  , name , den , ve):
		self.tk = tk
		self.mk =mk
		self.name = name
		self.den = den
		self.ve = ve
	def tg_gian_chs(self):
		h1 , m1 = int(self.den[0:2]) , int(self.den[3:])
		h2 , m2 = int(self.ve[0:2]) , int(self.ve[3:])
		time1 = h1 * 60 + m1
		time2 = h2 * 60 + m2
		return time2 -time1
	def get_user(self):
		return self.tk
	def __str__(self):
		ans = self.tg_gian_chs()
		h = ans // 60
		p = ans % 60
		return f'{self.tk} {self.mk} {self.name} {h} gio {p} phut'
		







if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		p = nv2( input() , input() , input() , input() , input() ,)
		a.append(p)
	a.sort(key = lambda x : (-x.tg_gian_chs() , x.get_user()))
	for x in a:
		print(x)
