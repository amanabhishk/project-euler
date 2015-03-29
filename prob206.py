#138901917'0', around 1 min 20 sec running time
def alternate_digit_check(n):
	#l = len(str(n)):
	alt = []
	for i in range(0,17):
		if i%2 == 0:
			alt.append(int(n%10))
		n = (n-n%10)/10
	#print alt
	alt.reverse()
	#print alt
	if alt == range(1,10):
		return True
	else:
		return False

for x in xrange(101010103,138902662,10):
	#print x
	if alternate_digit_check(x**2) == True:
		print x,x**2
		exit(0)
for x in xrange(101010107,138902662,10):
	#print x
	if alternate_digit_check(x**2) == True:
		print x,x**2
		exit(0)


#print alternate_digit_check(22233445566778899)

