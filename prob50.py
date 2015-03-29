#997651, 0.48 sec
import time
t = time.time()
from primes_till_one_million import prime

i = 1
output = []
while i < len(prime):
	s = prime[i]
	j = i
	while s < 999984 and (j+2 < len(prime)):
		s += prime[j+1] + prime[j+2]
		j += 2
		if s < 999984: output.append([j-i+1,s])
	i += 1  
output.sort()
sieve = [True] * 10**6 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

# print sieve


r = len(output)-1
while r > -1:
	if sieve[output[r][1]]: 
		print output[r]
		break
	r -= 1
	# print r

print time.time()-t
# print max(output)
# print len(output)
# print output

