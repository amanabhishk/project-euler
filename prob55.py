#249, 0.2 sec
import time
t = time.time()

def pal_check(i):
	a = list(str(i))
	if len(a)%2 == 0: 
		a1 = a[0:len(a)/2]
		a2 = a[len(a)/2:len(a)]
	else:
		a1 = a[0:len(a)/2]
		a2 = a[(len(a)/2)+1:len(a)]
	if a1[::-1] == a2: return True
	else:	return False

# print pal_check(21122)
ans = 0
for x in range(1,10000):
	i = 0
	a = list(str(x))
	while i < 50:
		
		b = int(''.join(a))+int(''.join(a[::-1]))
		# print b
		if pal_check(b): break
		i += 1
		a = list(str(b))
	if i == 50: ans += 1

print ans 
print time.time()-t


