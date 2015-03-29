#5482660, 17 sec. this was the ONLY D that was found, no minimisation required
import time
t = time.time()
limit = 10**8
data = [False]*limit

i = 2
n = 1
pent = [1]
while n < limit:
	data[n] = True
	n = i*(3*i-1)/2
	pent.append(n)
	i += 1
# print i

ans = limit
j = 0
while j < len(pent):
	a = pent[j]
	k = j+1
	while k < len(pent):
		b = pent[k]
		if (a+b) < limit:
			# if (b-a)<0: print 'fix'
			if data[a+b] and data[b-a]: 
					print 'yea'
					ans = min(ans,b-a)


		k += 1

	j += 1
# output.sort()
print ans
print time.time()-t


