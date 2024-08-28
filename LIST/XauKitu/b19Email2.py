



if __name__ == '__main__':
	t = int(input())
    d = dict({})
	for _ in range(t):
		s = input().lower()
	    a = s.split()
	    res = a[-2]
	    ns = a[-1]
	    for i in range(0 , len(a) - 2):
	    	res += a[i][0]
	    if res in d:
	    	d[res] += 1
	        print(res , d[res], '@xyz.edu.vn', sep = '')
	    else:
	        d[res] = 1
	        print(res + '@xyz.edu.vn')

	    b = ns.split('/')

	    for x in b:
	    	print(int(x) , end ='')
	    print()