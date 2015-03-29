import time
t = time.time()
n = 1
ans = 0
while int((10**n - 1)**(1/float(n))) - (int((10**(n - 1))**(1/float(n))) + 1)  >= 0:
	b = int((10**n - 1)**(1/float(n))) + 5
	a = int((10**(n - 1))**(1/float(n)))
	#print a,b
	i = a
	while i < b+1:
		if len(str(i**n)) == n:
			# print i
			ans += 1
		i += 1
		# print i
		# print '-------------'




	# print '---------------'
	# print n,ans
	# print (int((10**(n - 1))**(1/float(n)))+1),len(str((int((10**(n - 1))**(1/float(n)))+1)**n))
	# print (int((10**n - 1)**(1/float(n)))), len(str((int((10**n - 1)**(1/float(n))))**n))
	# ans = int((10**n - 1)**(1/float(n))) - int((10**(n - 1))**(1/float(n)))  + ans
	n += 1

print ans
print time.time()-t
