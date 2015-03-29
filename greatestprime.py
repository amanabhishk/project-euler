def prime_check(n):
	total = True
	for i in range(2,n/2):
		total = total and n%i != 0
		if total == False:
			return False
	return True

prime = []
for i in range(2,100000):
	if prime_check(i) == True:
		prime.append(i)


def greatest_prime_factor(n,prime):
	k = 1
	for i in range(0,len(prime)):
		print 'prime is:' ,prime[i]
		if n%prime[i] == 0:
			k = prime[i]
			while n%prime[i] == 0:
				n = n/prime[i]
				print n
		if n == 1:
			return prime[i]

#print prime_check(600851475143)
print greatest_prime_factor(600851475143,prime)