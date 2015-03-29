import time
t = time.time()

# from primes_till_one_million import prime
from crap import prime
r = [0]*5*10**6

for p in prime:#[0:100]:
	add = 1
	i = 2*p
	while i<len(r):
		r[i] += add
		add += 1
		i += p
		# if i==80: print p,add

	
	# lower_p = list(prime[0:prime.index(p)])
	correction = []
	l = 0
	k = prime[l]
	while k*p < len(r) and k < p:
		correction.append(k*p)
		l += 1
		k = prime[l]

	# print correction
	for c in correction:
		sub = 1
		k = 2*c	
		while k < len(r):
			r[k] -= sub
			sub += 1
			k += c
			
print 'inequality check started.'

for i in range(5*10**6,len(r)):
	if 94744*(i-1-r[i])< 15499*(i-1) :
		print i
		break 

	# print i,r[i]

print time.time()-t
