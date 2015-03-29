from math import sqrt
l = 50					#Upto what number. Enter even number here. Add 1 if upto an odd number.
sieve = [True]*((l-2)/2)
i = 1
c = sqrt(l)+1
while i<len(sieve):
	n = i+(2*i+1)
	while n < len(sieve):
		
		sieve[n] = False
		n = n + (2*i+1)
	i = i + 1
	if 2*i+1 > c:
		break
k = 1

s = 0
while k<len(sieve):
	if sieve[k]:
		#s = s + 2*k+1
		print 2*k+1
	k = k + 1


#print s