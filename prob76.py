#190569291, .002 sec
import time
t = time.time()

a = [1]*101 #0-100
b = list(a)
i = 2
#k = 2
while i < len(a):
	#a[0] += 1
	k = i
	while k < len(a):
		
		a[k] = b[k] + a[k-i]
		#print 's(',k,i,') = s(',k,i-1,')+s(',k-i,i,')'
		k += 1
	i += 1
	b = list(a)

print a[-1]-1
print time.time()-t