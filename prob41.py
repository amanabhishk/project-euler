#7652413. 0.00159382820129 s

import time
t = time.time()
import math
import itertools

digits = ['7','6','5','4','3','2','1'] #with 8 and 9 the number will be divisible by 3

while True:
	p = list(itertools.permutations(digits))
	#del digits[0]
	for z in p:
		a = int(''.join(list(z)))
		#print a
		#truth = True
		if a%2 != 0:
			for x in xrange(3,int(math.sqrt(a))+1,2):
				#truth = truth + a%x != 0
				if a%x == 0:
					break
			if a%x != 0:
				print 'ans',a
				print time.time()-t
				exit(0)
	del digits[0]