# 26241, 1.4 sec

import time
from math import sqrt
t = time.time()
from primes_till_one_million import prime

def prime_check(n):
	i = 0
	m = 2
	l = sqrt(n)+1
	while m < l:
		if n%m == 0: return False
		i += 1
		m = prime[i]
	return True

i = 3
diag = []
count = 0
while True:
	a = i*i
	diag += [a-i+1,a-2*i+2,a-3*i+3]
	size = 2*i-1

	if prime_check(diag[-1]): 
		# print diag[-1]
		count += 1
	if prime_check(diag[-2]): 
		# print diag[-2]
		count += 1
	if prime_check(diag[-3]): 
		count += 1
		# print diag[-3]
	# print i,count,size
	if count*10 < size: 
		print i
		break
	i += 2
	# if i>7: break


print time.time()-t
