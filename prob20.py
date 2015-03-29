#648

import math

a = math.factorial(100)

sum = 0

while True:
	
	sum = sum + a%10
	if a < 10:
		print sum
		break
	a = (a-a%10)/10


