#31626


import math

def d(n):
	a = 1
	i = 2
	while i < int(math.sqrt(n))+1:
		if n%i == 0:
			a = a + i + (n/i)
		i = i+1
	# if int(math.sqrt(n))**2 == n:
 # 		print  a -1

	return a

i = 0
ans = 0
while i < 10000:
	if d(d(i)) == i:
		if d(i) != i: 
			print i,d(i)
			ans = ans + i 

	i = i+1





print ans
# print d()
