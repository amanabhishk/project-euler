#76576500

import math

def divisors(n):
	a = 2
	i = 2
	while i < int(math.sqrt(n))+1:
		if n%i == 0:
			a = a + 2
		i = i+1
	if int(math.sqrt(n))**2 == n:
 		return  a -1

	return a

n = 50

while True:
	
	k = n*(n+1)/2

	a = divisors(k)
	print n,a
	if a > 500:
		print 'output',k
		break

	n = n+1


# if int(math.sqrt(n-1))**2 == n-1:
# 		print  a -1



#print a
