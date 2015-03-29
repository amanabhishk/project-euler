#840, 0.0015 sec
import time
t = time.time()
triples = []

for m in range(1,24):
	for n in range(m+1,24):
		c = m*m + n*n
		a = abs(m*m - n*n)
		b = 2*m*n
		p = a+b+c
		if a > b: triples.append([p,b,a,c])
		else: triples.append([p,a,b,c])
l = len(triples)
for i in range(0,l):
	p = triples[i][0]
	# print p
	k = 2
	while k*p < 1000:
		d = [k*x for x in triples[i]]
		# print d
		triples.append(d)
		k += 1 
triples.sort()
for x in range(0,len(triples)):
	if x+1<len(triples):
		while triples[x] == triples[x+1]: del triples[x+1]

r = 3000
data = [0]*r

for x in range(0,len(triples)): data[triples[x][0]] += 1

print max(data), data.index(max(data))
print time.time() -t


# print triples