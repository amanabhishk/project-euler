import math

primes = [2,3]
n = primes[len(primes)-1]+2
length = 100000

# while len(primes) < length:
truth_expression = True
k = 1

while len(primes) < length:
	
	truth_expression = truth_expression and  n%primes[k] != 0 
	#print n,primes[k],truth_expression
	
	
	if truth_expression == False:
		n = n+2
		k = 1
		truth_expression = True

	k = k+1
	if k >= int(math.sqrt(n)):
		primes.append(n)
		n = n+2
		k = 1
	
		

	#print truth_expression
	#primes.append(n)
	#	primes.append(n)


print primes	