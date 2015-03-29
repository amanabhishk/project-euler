import time
t = time.time()
k = 2
a = 1
b = 1
pan = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
	k += 1
	c = a + b
	last = sorted(list(str(c%10**9)))
	#d = len(str(c))-2
	first = sorted(list(str((c/10**(len(str(c))-9)))))
	if (first == pan) and (last == pan):
		print k
		break
	a = b
	b = c

print time.time()-t