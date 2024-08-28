

def email(s):
	res = s.lower().split()
	a = res[-1]
	for x in res[:-1]:
		a += x[0]
	a += '@gmail.com'
	return a
def ns(s):
	res = s.split('/')
	tmp = ''
	for x in res:
		tmp += str(int(x))
	return tmp

f1 = open("input.txt" , "r")
f2 = open("output.txt" , "w")

data = []
for x in f1:
	data.append(x[:-1])
for i in range(0 , len(data) , 2):
	f2.write(email(data[i]) + '\n')
	f2.write(ns(data[i + 1]) + '\n')

f1.close()
f2.close()