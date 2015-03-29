import time
t = time.time()
def ad(a):		#does long addition to check for all odd digits and retuns False as soon as encountering even digit rather than finishing
				#the summation process and then checking together. This is better, I checked.
	x = list(str(a))
	#y = list(reversed(x))
	output = 0
	c = 0
	for i in range(0,len(x)):
		c += int(x[i]) + int(x[::-1][i])
		#print c
		if c%2 == 0:
			return False
		c = (c - c%10)/10
		#print c
	return True#int(''.join(x))+int(''.join(x[::-1]))


#2 digit numbers
i = 11
ans = 0
digits = 2
while i < 10**digits:
	for x in xrange(i,i+9):
		if ad(x):
			ans += 1
	# if i%9 == 9:
	# 	i += 2
	i += 11

	











print time.time() - t


