#see Euclid's pythogorean triple generating formula
perimeter = [0]*1001
triples = []
for m in range(1,24):
	for n in range(m+1,24):
		c = m*m + n*n
		a = abs(m*m - n*n)
		b = 2*m*n
		p = a+b+c
		w = [a,b,c]
		w.sort()
		# w = [p] + w
		k = 1
		# if not(w in triples): triples += [w]
		# counter = 0
		while p < 1001: 
			# print a,b,c,p
			
			w = [i*k for i in w]
			if  w==[2*8,2*15,2*17] and k == 2: print w
			if not(w in triples): triples += [w]
			# if  w==[3*16,3*30,3*34] and k == 3: print triples
			# if w == [8,15,17]: print 'yes',k,p
			# w = [a,b,c]
			# w.sort()
			# w = [p] + w
			
			k += 1
			p *= k
			if  w==[2*8,2*15,2*17] and k == 3: print p
			# if w == [8,15,17]: print 'yes',k,p,p<1001

triples.sort()

for i in range(0,len(triples)):
	perimeter[sum(triples[i])] += 1
# triples = set(tri)
# print triples
# print max(perimeter),'for the perimeter of:',perimeter.index(max(perimeter))#,perimeter 
