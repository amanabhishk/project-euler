# x + 2y + 3z + 4k = 50
from math import factorial
import time
t = time.time()
sol = []
c = 1000
yc = 2
zc = 3
kc = 4

for k in xrange(0,c/kc + 1):
	for z in xrange(0,c/zc + 1):
		
		xmax = c
		ymax = c/yc
		x = xmax
		y = 0
		
		while True:
			l = x + yc*y + zc*z + kc*k - c
			#print x,'+',2*y,l
			if x == -1:
				break
			if l == 0:
				sol.append([x,y,z,k])
				x -= 1
				y += 1
			if l > 0:
				x -= 1
			if l < 0:
				y += 1

#print sol
print sum(factorial(a[0]+a[1]+a[2]+a[3])/(factorial(a[0])*factorial(a[1])*factorial(a[2])*factorial(a[3])) for a in sol)
print time.time()-t



		

