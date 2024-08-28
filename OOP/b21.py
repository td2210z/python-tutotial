



class mh:
	def __init__(self , ma , tenmh , dv , gia , ban):
		self.ma = str(ma)
		while len(self.ma) < 4:
			self.ma = '0' + self.ma
		self.ma = 'MH' + self.ma
		self.tenmh = tenmh
		self.dv = dv
		self.gia = gia
		self.ban = ban
	def __str__(self):
		return f'{self.ma} {self.tenmh} {self.dv} {self.gia} {self.ban} {self.ban - self.gia}'
	def get_loi_nhuan(self):
		return self.ban - self.gia
	def get_ma(self):
		return self.ma





if __name__ == '__main__':
	n = int(input())
	a = []
	for i in range(n):
		m = mh(i + 1, input() , input() , int(input()) , int(input()))
		a.append(m)
	a.sort(key = lambda x : -x.get_loi_nhuan())
	for x in a:
		print(x)
