#142857, about 1 sec. Total brute force

import time
t = time.time()
i = 101
while True:
	a1 = sorted(list(str(i)))
	a2 = sorted(list(str(2*i)))
	a3 = sorted(list(str(3*i)))
	a4 = sorted(list(str(4*i)))
	a5 = sorted(list(str(5*i)))
	a6 = sorted(list(str(6*i)))
	if (a1 == a2) and (a2 == a3) and (a3 == a4) and (a4 == a5) and (a5 == a6):
		print i
		break
	i += 1

print time.time()-t


