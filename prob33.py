# from __future__ import division

for x in xrange(10,100):
	for y in xrange(10,100):
		if x/y == 0:
			a = [x%10,(x-x%10)/10]
			b = [y%10,(y-y%10)/10]
			common = list(set(a).intersection(b))
			if len(common) != 0:
				a = list(set(a)-set(common))
				b = list(set(b)-set(common))
			if len(b) == 0:
				b = list(set(common))
			if len(a) == 0:
				a = list(set(common))
			
			#print x,y,a,b
			if len(a) == 1 and b[0] != 0:
				if x/float(y) == a[0]/float(b[0]):
					print x,'/',y 


		else: continue
