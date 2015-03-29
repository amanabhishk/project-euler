#402. Run-time 97 sec. Can be made faster by noting: permutations of same digit => same chains
import time
start_time = time.time()
import math
ref = []
def permutations_check(ref, n):
	digits = []
	while n > 9:
		digits.append(n%10)
		n = (n-n%10)/10
	digits.append(n)
	#print digits
	digits = sorted(digits)
	#print digits
	ref.append(digits)
	# if (len(list(set(ref))) != len(ref)):
	# 	return False
	# else: return True


def fact_sum(n):
	s = 0
	while n > 9:	
		s = s + math.factorial(n%10)
		n = (n - n%10)/10
	return s + math.factorial(n)



# print permutations_check(ref,1234456);permutations_check(ref,123499999996);permutations_check(ref,1654432)
# print ref
s = 0

for y in xrange(3,10**6):
	#print x 
	chain = [y]
	x = y
	while True:
		
		a = fact_sum(x)
		chain.append(a)
		#print chain 
		#common = list(set([a]).intersection(chain))
		if (len(chain) != len(list(set(chain)))):
			if len(chain) == 61:	
				#print y
				s = s+1
			break
			#exit(0)
		x = a 

print s
print time.time() - start_time, "seconds"