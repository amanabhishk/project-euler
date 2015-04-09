import time
t = time.time()
sieve = [True] * 5*10**6 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

prime = []
# print sum(i for i in xrange(2, len(sieve)) if sieve[i])
for i in xrange(2,len(sieve)):
  if sieve[i] : prime.append(i)
print 'prime generation complete in', time.time()-t,'sec.'