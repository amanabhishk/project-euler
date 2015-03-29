#932718654, 0.007 sec
import time
t = time.time()
def pandigital_check(a):
	if len(str(a)) != 9: return False
	i = a
	val = [0]*10
	while i > 9:
		val[i%10] = i%10
		i = (i - i%10)/10

	val[i] = i
	if val == [0,1,2,3,4,5,6,7,8,9]: return True
	else: return False


r = range(90,99)+range(900,999)+range(9000,9900)
# r = range(900,920)
# print r
for i in r:
	n = []
	k = 1
	while len(n)+len(str(k*i)) < 10:
		n += list(str(k*i))
		k += 1
	a = int(''.join(n))
	if pandigital_check(a): print i, a,k-1
	# print n

print time.time()-t