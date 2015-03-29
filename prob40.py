#210
# A factoradic type system can be made with respect to the number of 
#digits. That will be a factoradic type ipmrovement over brute force in that other question 
import time
 
start = time.time()

s = ''
i = 1
l = range(1,200000)
#s = ''.join(str(i) for i in l)

while len(s) < 1000001:
	s = s + str(i)
	i = i + 1

#s = ''.join(x in xrange(1,10**6) if len(s) < 10**6+1)

length =  len(s)
n = int(s)
#print n
ans  = 1

i = 1
# for k in range(1,length+1):
while i < 1000001:	
	# print ((n - n%(10**(length-i)))/10**(length-i))%10
	ans = ans*(((n - n%(10**(length-i)))/10**(length-i))%10)
	i = i*10
# k = 12
# print 10**(length-k),n%(10**(length-k)),(n - n%(10**(length-k))),((n - n%(10**(length-k)))/10**(length-k))%10
elapsed = (time.time() - start)
print ans, elapsed
