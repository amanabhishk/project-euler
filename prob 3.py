def prime_check(n):
	total = True
	for i in range(2,n/2):
		total = total and n%i != 0
		if total == False:
			return False
	return True

prime = []
for i in range(1,100):
	if prime_check(i) == True:
		prime.append(i)


def greatest(n,prime):
	for i in range(2,len(prime)):
		if n =< prime[i]:
			return k
		if n%prime[i] == 0:
			k = prime[i]
			while n%prime[i] != 0:
				n = n/prime[i]

greatest(45,prime)