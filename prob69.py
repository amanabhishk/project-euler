import time
t = time.time()

# sieve = [True] * 10**6 # Sieve is faster for 2M primes
# def mark(sieve, x):
#     for i in xrange(x+x, len(sieve), x):
#         sieve[i] = False

# for x in xrange(2, int(len(sieve) ** 0.5) + 1):
#     if sieve[x]: mark(sieve, x)
from primes_till_one_million import prime

r = [0]*1*10**6

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
r = [i-1-r[i] for i in range(0,len(r))]
for i in range(2,501):
	print i,r[i] 

#210,220,228,234,240,252 ARE ALL WRONG.
# exit(0)
# print a[2:10]
i = 2
output = []
while i<len(r):
	# if i<500: print i/float(r[i])
	output.append(i/float(r[i]))
		# N = i
		# output =  i/float(r[i])
	i += 1

	# if i == 11: break
output.sort()
print output[-1]#, N,i
print time.time()-t

