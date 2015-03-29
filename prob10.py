#142913828922
import math

primes = [2, 3]

n = 1

#length = 15
ans = 0
# while len(primes) < length:
truth_expression = True

while primes[len(primes)-1] < 2000000:
	k = 1
	x = 0
	number = [6*n-1,6*n+1]
	#loops = 0
	while x < 2:
		#print number[x], truth_expression, k, primes,primes[k],number[x]%primes[k] != 0
		truth_expression = truth_expression and number[x]%primes[k] != 0
		
		if truth_expression == False:
			x = x+1
			truth_expression = True
			if x > 1:
				break
			
			k = 1

		

		if primes[k] >= int(math.sqrt(number[x])):
			primes.append(number[x])
			print number[x]
			#ans = ans + number[x]
			#loops = loops+1
			#print '\n',loops,'\n'
			x = x+1
			k = 1
		
		k = k+1
		
	
	n = n+1

y = 0
while primes[y] < 2000000:
	ans = ans +primes[y]
	y = y+1

print 'ans', ans











# k = 1
# ans = 0
# while primes[len(primes)-1] < 30:
	
# 	for x in range(0,2):
# 		while primes[len(primes)-1] < 30:
# 			truth_expression = truth_expression and  number[x]%primes[k] != 0 
# 			print number[x]
			
			
# 			if truth_expression == False:
# 				#n = n+1
# 				k = 1
# 				truth_expression = True

# 			k = k+1
# 			if k >= int(math.sqrt(n)):
# 				primes.append(6*n+1)
# 				n = n+1
# 				k = 1
			
		

	#print truth_expression
	#primes.append(n)
	#	primes.append(n)


# i = 0
# while primes[i] < 2000000:
# 	ans = ans + primes[i]
# 	i = i+1

