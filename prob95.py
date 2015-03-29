import math

def div_sum(n):
	output = 1
	for i in xrange(2,int(math.sqrt(n)+1)):
		if n%i == 0:
			output = output + i + (n/i)
	return output


def database_update(chain,database):
	if div_sum(chain[len(chain)-1]) == chain[0]:
	print l
	for j in xrange(0,len(chain)):
		if chain[j] == l:
			L = j
	print L
	for k in xrange(0,L):
		if not(chain[k] in database):
			database[chain[k]] = False
	return database

database = {1:False}
data = []
x = 20

# while (x < 100 +1) and not(x in database):
# 	#x = 12496
# 	chain = []
# 	y = x
# 	while len(set(chain).intersection([div_sum(x)])) == 0:
# 		chain.append(x)
# 		x = div_sum(x)
# 		if (len(str(x)) >= 100):
# 			break
# 	if x != 1:
# 		chain.append(x)
# 		data.append([len(chain),min(chain)])
# 	database_update(chain,database)
# 	x = y + 1
# 	print chain

# print min(data)

print database_update([14288,15472,14536,14264,12496],database)