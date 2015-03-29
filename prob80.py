from decimal import *
import math


s = 0
getcontext().prec = 101
b = 101
i = 2
while i < b:
	if int(math.sqrt(i)) == math.sqrt(i): continue#b = b+1
	else:
		
		n = Decimal(i).sqrt() - int(Decimal(i).sqrt())
		#print n
		nsum = 0
		k = 1
		while k != 101:
			nsum = nsum + int(10*n)
			#print nsum
			n = 10*n - int(10*n)
			k = k+1
		print i,Decimal(i).sqrt(),nsum
	s = s + nsum
	i = i+1
	#else: b = b+1 

print s

