#1587000, 5.6 sec

import time
t = time.time()
k = 100
ans = 0

while True:
	a = sorted(list(str(k)))
	#print a 
	b = int(str(''.join(a[::-1])))
	a = int(''.join(a))
	#print a,b
	if (k != a) and (k != b):
		ans += 1
		if ans/float(k) == 0.99:
			print k
			print time.time()-t
			exit(0)
	k += 1

#print ans