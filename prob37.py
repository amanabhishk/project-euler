#748317, 75 sec
import time
t = time.time()
from primes_till_one_million import prime 

def truncator(i):
	# output = True
	a = i
	while a in prime and (a > 10):
		a = (a-a%10)/10
		# print 'this a',a
	if not(a in [2,3,5,7]): return False

	b = i
	ten = (10**len(str(i)))/10

	while b in prime and (b > 10):
		b = b%ten
		ten = ten/10
		# print 'this b',b
	if not(b in [2,3,5,7]): return False
	
	return True
		

# print truncator(19)

i = 4
count = 0
ans = 0
while i < len(prime):
	if truncator(prime[i]): 
		count += 1
		ans += prime[i]
		# print count,prime[i]
	if count == 11: 
		print ans
		break 
	i += 1	

print time.time()-t











	# if (10*prime[i]/(10**len(str(prime[i]))))%2 == 0: i += 1
	# else: 
	# 	if truncator(i): 
	# 		count += 1
	# 		print count,prime[i]
	# 	i += 1


# print truncator(3797)
