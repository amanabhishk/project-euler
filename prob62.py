#127035954683,.05 sec
import time
k = time.time()
a = sorted([[sorted(list(str(i**3))),i**3] for i in xrange(100,10**4)])
i = 0
#a = [1,2,3,4,4,4,4,5,6,6,7,7,7,7,7]
while i < len(a): #very optimised way of finding a string of 5 B-)
	#print i
	t = a[i][0] == a[i+1][0]
	if t:
		t = t and a[i+1][0]==a[i+2][0]
		if t:
			t = t and a[i+2][0]==a[i+3][0]
			if t:
				t = t and a[i+3][0]==a[i+4][0]
				if t:
					print 'ANS',a[i][1],a[i+1][1],a[i+2][1],a[i+3][1],a[i+4][1]
					break
				else:
					i += 4
			else:
				i += 3
		else:
			i += 2
	else:
		i += 1 
#print len(set(list(a)))



print time.time()-k