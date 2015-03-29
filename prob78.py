#190569291, .002 sec
import time
t = time.time()

a = [1]*6*10**4 #0-100
b = list(a)
i = 2
#k = 2
while i < len(a):
	print i
	k = i
	while k < len(a):
		
		a[k] = b[k] + a[k-i]
		#print 's(',k,i,') = s(',k,i-1,')+s(',k-i,i,')'
		k += 1
	i += 1
	b = list(a)

#print a[]
for x in xrange(0,len(a)):
	if a[x]%10**6 == 0:
		print x
		print time.time()-t
		break
#print a[-1]