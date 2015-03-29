# -59231,35 sec

import time
t = time.time()
from primes_till_one_million import prime 

def nth(a,b):
	n = 2
	till = 1
	while (n*n + n*a + b) in prime:
		till += 1
		n += 1
	return till

ans = 0
for i in range(3,168): #prime[168] = 997
	b = prime[i]
	for k in xrange(0,len(prime)):
		
		a = prime[k]-1-b
		# print b,a
		if a > 1000 or a < -1000: break
		c = nth(a,b)
		if c > 35: print a,b,c, a*b
		# ans = max(c,ans)
# print ans

print time.time()-t



