#153, 0.009
import time
t = time.time()
a = 3
b = 2
i = 0
ans = 0
while i<1000:
	A =  2*b+a
	B =	 b+a
	a = A
	b = B
	if len(str(A)) > len(str(B)): 
		# print a,b
		ans += 1
	i += 1

print ans
print time.time()-t

