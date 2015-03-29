#16695334890, 0.014 sec


import time
t = time.time()

def pan_check(i):
	ref = [0]*10
	a = i
	while a > 9:
		ref[a%10] += 1
		a = (a-a%10)/10
	ref[a] += 1
	a = 0
	while a < 10:
		if ref[a] >1: return False
		a += 1
	return True
two = []
a = 12
while a<1000:
	if pan_check(a): two.append(a)
	a += 2

result = []

for n2 in two:
	l3 = (n2%100)*10
	r3 = l3%3
	three = [x for x in range(l3-r3+3,l3+10,3)]
	three = [x%10 for x in three]
	result3 = [n2*10+three[x] for x in range(0,len(three))]
	result3 = [a for a in result3 if pan_check(a)]
	# if n2 == 406: print result3	
	
	for n3 in result3:
		l5 = (n3%100)*10
		r5 = l5%5
		five = [x for x in range(l5-r5+5,l5+10,5)]
		five = [x%10 for x in five]
		result5 = [n3*10+five[x] for x in range(0,len(five))]
		result5 = [a for a in result5 if pan_check(a)]

		# print result5	
	
		for n5 in result5:
			l7 = (n5%100)*10
			r7 = l7%7
			seven = [x for x in range(l7-r7+7,l7+10,7)]
			seven = [x%10 for x in seven]
			result7 = [n5*10+seven[x] for x in range(0,len(seven))]
			result7 = [a for a in result7 if pan_check(a)]
			

			for n7 in result7:
				l11 = (n7%100)*10
				r11 = l11%11
				eleven = [x for x in range(l11-r11+11,l11+10,11)]
				eleven = [x%10 for x in eleven]
				result11 = [n7*10+eleven[x] for x in range(0,len(eleven))]
				result11 = [a for a in result11 if pan_check(a)]


				for n11 in result11:
					l13 = (n11%100)*10
					r13 = l13%13
					thirteen = [x for x in range(l13-r13+13,l13+10,13)]
					thirteen = [x%10 for x in thirteen]
					result13 = [n11*10+thirteen[x] for x in range(0,len(thirteen))]
					result13 = [a for a in result13 if pan_check(a)]


					for n13 in result13:
						l17 = (n13%100)*10
						r17 = l17%17
						seventeen = [x for x in range(l17-r17+17,l17+10,17)]
						seventeen = [x%10 for x in seventeen]
						result17 = [n13*10+seventeen[x] for x in range(0,len(seventeen))]
						result17 = [a for a in result17 if pan_check(a)]

						result += result17


result = [x for x in result if len(str(x)) == 9]
print result
print sum(result)+15*10**9
print time.time()-t











			# result += result7
			# print result7	
			# result11=[]
			# for n7 in result7:
			# 	l11 = (n7%100)*10
			# 	r11 = l11%11
			# 	eleven = l11-r11+11
			# 	if eleven-l11>9: eleven = 0
			# 	else:	
			# 		eleven = n7*10+eleven%10
			# 		# if pan_check(result11) == False: result11 = 0
			# 		result11.append(eleven)
			# 	# print result11	

			# 	result11 = [a for a in result11 if pan_check(a)]
			# 	result13= []
			# 	for n11 in result11:
			# 		l13 = (n11%100)*10
			# 		r13 = l13%13
			# 		thirteen = l13-r13+13
			# 		if thirteen-l13>9: thirteen = 0
			# 		else:	
			# 			thirteen = n11*10+thirteen%10
			# 				# if pan_check(result13) == False: result13 = 0
			# 			result13.append(thirteen)

			# 		result13 = [a for a in result13 if pan_check(a)]
			# 		result17= []
						

			# 		for n13 in result13:
			# 			l17 = (n11%100)*10
			# 			r17 = l17%13
			# 			seventeen = l17-r17+13
			# 			if seventeen-l17>9: seventeen = 0
			# 			else:	
			# 				seventeen = n13*10+seventeen%10
			# 				# if pan_check(result17) == False: result17 = 0
			# 				result17.append(seventeen)
			# 			# print result17

# result3.sort()
# print result3