# 983, 0.22 sec
import time
T = time.time()

def remainder_count(i):
	t = []
	q = 1
	length = 0
	while q < i: q *= 10
	
	while True:
		if q < i:	q *= 10
		q = q%i
		
		if q == 0:	return 0
		elif q in t:	return length - t.index(q) 
		else:	t.append(q)
		
		length += 1
		

a = [remainder_count(i) for i in xrange(2,1000)]
print a.index(max(a))+2
print time.time() - T
