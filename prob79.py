# number = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]
# number = sorted(list(set(number)))
# print number
number = [129, 160, 162, 168, 180, 289, 290, 316, 318, 319, 362, 368, 380, 389, 620, 629, 680, 689, 690, 710, 716, 718, 719, 720, 728, 729, 731, 736, 760, 762, 769, 790, 890]
for x in xrange(0,len(number)):
	c = number[x]%10
	b = ((number[x]-number[x]%10)/10)%10
	a = (number[x]-number[x]%100)/100
	#print c,b,a
	Truth1 = True
	Truth2 = True
	for y in xrange(0,len(number)):
		if x != y:
			r = number[y]%10
			#q = ((number[x]-number[x]%10)/10)%10
			p = (number[y]-number[y]%100)/100
			if (p == a and r == b): print number[x],number[y]
			if (p == b and r == c): print number[x],number[y]
	# if Truth1: print a,b
	# if Truth2: print b,c

