#31875000
for a in range(1,1000):
	for b in range(1,1000):
		if 2*a*b == -1000000 + 2000*(a+b):
			print a,b
			c = 1000 - a -b
			print c*c == a*a + b*b
			print 'ans', a*b*c
# c = 1000 - a -b
# print c*c , a*a + b*b