#872187
s = 0
for n in xrange(1,10**6):
	if (bin(n) + 'b0' == '0b' + bin(n)[::-1] and str(n) == str(n)[::-1]) == True:
		s  = s + n

print s