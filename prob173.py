#1572729
import time
t = time.time()
even = []
odd = []
for x in xrange(2,250002,2): even.append(x**2)
for y in xrange(1,250002,2): odd.append(y**2)

print "even[] and odd[] made." 

le = []
lo = []
for x in xrange(len(even)-1,-1,-1):
	y = x - 1
	while y > -1:
		if (-even[y]+even[x]) <= (10**6):
			le.append(-even[y]+even[x])
		#if (even[y]-even[x]) == 16:
			#print "THIS",even[y],even[x]
			y = y - 1
		else:
			break


print "le[] made."
for x in xrange(len(odd)-1,-1,-1):
	y = x - 1
	while y > -1:
		if (-odd[y]+odd[x]) <= (10**6):
			lo.append(-odd[y]+odd[x])
		#if (odd[y]-odd[x]) == 16:
			#print "THIS",odd[y],odd[x]
			y = y - 1
		else:
			break

print "lo[] made."
data = {}

for x in xrange(0,len(le)):
	#print le[x],le[x] in data ,not(le[x] in data)
	if not(le[x] in data):
		data[le[x]] = 1
		#print data
	else:
		data[le[x]] = data[le[x]] + 1
print "data{} made for le[]."
for x in xrange(0,len(lo)):
	#print le[x],le[x] in data ,not(le[x] in data)
	if not(lo[x] in data):
		data[lo[x]] = 1
		#print data
	else:
		data[lo[x]] = data[lo[x]] + 1
print "data{} made for lo[]. "
ans  = 0
for i in xrange(4,1000001):
	if i in data:
		#print i,data[i]
		ans  = ans + data[i]

print ans
print len(data)
print time.time() -t