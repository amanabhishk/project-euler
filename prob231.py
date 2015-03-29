import time
t = time.time()

n = 20000000
r = 15000000


sieve = [True]*(int(n**0.5)+4)
n = [i for i in xrange(0,len(sieve))]
for a in n[2:len(n)]:
	if sieve[a]:
		k = 2*a
		#print k
		while k < len(sieve):
			sieve[k] = False
			k += a 

primes = [i for i in xrange(2,len(sieve)) if sieve[i]]

denominator_sum = [[i,0] for i in range(0,n-r+1)]





















































# import time
# t  = time.time()

# n = 20000000
# r = 15000000

# sieve = []


# denominator_count = [x for x in xrange(0,n-r+1)]
# denominator_sum = [0]*(n-r+1)

# for x in xrange(2,int(n**0.5)+1):
# 	if x == denominator_count[x]:
# 		denominator_sum[x] = x
# 		sieve.append(x)
		
# 		k = 2*x
# 		while k < len(denominator_count):
# 			while denominator_count[k]%x == 0:
# 				denominator_sum[k] += x
# 				denominator_count[k] = denominator_count[k]/x
# 			#print k
# 			k += x
# 	#print x

# #print denominator_sum[575439]
# numerator_count = [i for i in xrange(r-1,n+1)]
# numerator_sum = [0]*len(numerator_count)
# a = n
# b = r-1
# for x in sieve:
# 	print x
# 	i = b/x
	
# 	if not(i*x in numerator_count):
# 		i += 1
# 	k = i*x
# 	if k in numerator_count:
# 		indx = numerator_count.index(k)
# 		while k < n+1:
# 			while numerator_count[indx]%x == 0:
# 				numerator_sum[indx] += x
# 				numerator_count[indx] = numerator_count[indx]/x 

# 			k += x
# print numerator_sum[0:10]
# print numerator_count[0:10]



# print time.time()-t



