#20492570929,.0003 sec
import time

t = time.time()
from math import factorial

length = 50
ans = 0
for i in [2,3,4]:
	mx = length/i
	for rods in xrange(1,mx+1):
		black_boxes = length - rods*i
		
		total_objects = black_boxes + rods
		ways = factorial(total_objects)/(factorial(black_boxes)*factorial(rods))
		ans += ways
	#print '------'











print ans
print time.time()-t