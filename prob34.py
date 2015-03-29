#40730
import math

def fact_sum(n):
	s = 0
	while n > 9:	
			
		s = s + math.factorial(n%10)
		#print n%10
		n = (n - n%10)/10
	
	return s + math.factorial(n)


i = 3
ans = 0
while i < 10**7:
	#print i, fact_sum(i)
	if fact_sum(i) == i:
		ans = ans + i 
		print i
		#print 'J' 
	i = i+1

print ans

