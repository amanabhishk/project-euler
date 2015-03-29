#4179871, .6 sec
import time
t = time.time()

l = [1]*(28123+1)

i = 2
#k = 2*i
while i < 28124/2 +2:
	k = 2*i
	while k < 28123 + 1:
		l[k] += i
		k += i 
	i += 1

s = 0
k = set()
for n in range(1,28123+1 ):
  if l[n] > n:
    k.add(n)
  if not any( (n-a in k) for a in k ):
   	s += n

print s
print time.time()-t
