#8581146 Running time around 35 sec
chain89 = {89:89}
chain1 = {1:1}

def chain_operation(n):
	output = 0
	while n > 9:	
		output = output + (n%10)**2
		n = (n-n%10)/10
	output = output + (n%10)**2
	return output

def chain_update(a,d,chain1,chain89):
	if d == 1:
		for x in xrange(0,len(a)):
			if a[x] in chain1 :
				break
			chain1[a[x]] = 1
	if d == 89:
		for x in xrange(0,len(a)):
			if a[x] in chain89 :
				break

			chain89[a[x]] = 1

#print chain_operation(44),chain_operation(32),chain_operation(13),chain_operation(10)
ans = 0
for i in xrange(1,10**7):
	chain = []
	k = i
	while (k != 1) or (k != 89):
		#print k
		if (k in chain1):
			chain_update(chain,1,chain1,chain89)
			#print i,'Terminates at', 1
			break
		elif (k in chain89):
			chain_update(chain,89,chain1,chain89)
			#print i,'Terminates at', 89
			ans  = ans + 1
			break
		else:
			chain.append(k)
			k = chain_operation(k)


print ans
#print chain1

