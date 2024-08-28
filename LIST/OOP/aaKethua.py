

class ng:
	def __init__(self , name , ten):
		self.name = name
		self.ten = ten
	


class sv(ng):
	def __init__(self , name , ten , ns):
		ng.__init__(self , name , ten)
		self.ns = ns
	def __str__(self):
	    return f'{self.name} {self.ten} {self.ns}'

if __name__ == '__main__':
	p = sv('thang' , 'ngueyn' , 'dinh')
	print(p)
	

