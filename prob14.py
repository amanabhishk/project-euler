# 837799

def collatz(n):
	i = 1
	while n != 1:	
		if n%2 == 0:
			n = n/2
			#print n
			i = i+1
			# if n == 1:
			# 	break
		else:
			n = 3*n +1
			#print n
			i = i+1

	return i


#collatz(6)
ans = [0,0]
i = 2
while i < 10**6:
	
	print i
	if ans[0] < collatz(i):
		ans[0] = collatz(i)
		ans[1] = i
	
	i = i+1 		

print ans	