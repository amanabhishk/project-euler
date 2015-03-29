#4075
import time
t = time.time()
import math

def C(n,r):
	return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))

#print C(23,10)
ans = 0
for x in xrange(23,101):
	ansx = 0
	#print '--------'
	for y in xrange(2,x/2+1):
		if C(x,y) > 10**6:
			#print y 
			break
			#ans =  ans + 1
	if (x+1)%2 == 0:
		ansx = (((x+1)/2) - y)*2 
	else:
		ansx = ((x/2) - y)*2 + 1
	#print x,ansx
	ans = ans + ansx

print ans
print (time.time()-t)