l = []

for x in range(4000,6001):
	c = x/float(12000)
	if not(c in l):
		l.append(c)

print len(l)
