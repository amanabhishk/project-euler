prime_list = [2    ,     3   ,      5  ,       7    ,    11    ,    13    ,    17    ,    19 ,23     ,   29    ,    31   ,     37   ,     41   ,     43     ,   47    ,    53,59    ,    61    ,    67   ,     71     ,   73      ,  79     ,   83 ,       89 ,97,101]
factor = 0
factorisation = []
all_factorisations = []
for a in range(2,11):
	n = a
	i = 0
	#print a
	while prime_list[i] <= a: 
		while n%prime_list[i] == 0:
			n = n/prime_list[i]
			factor = 1+factor
		
		factorisation.append(factor)
		factor = 0
		# factorisation[i] = 100*factorisation[i]
		i = i+1
	#print a,factorisation
	#factors.append(factorisation)
	
	#factorisation = [0]*len(prime_list)
	all_factorisations.append(factorisation)
	#print a,factorisation
	#print factorisation 
	factorisation = []
print all_factorisations
all_factorisations_with_power = []
for y in all_factorisations:
	#print y
	for b in range(2,3):
		k = map(lambda x: x * b, y)
		print k
		all_factorisations_with_power.append(list(k))
		print all_factorisations

# #print factors
# total = 100
# for x in xrange(0,100):
# 	for y in xrange(x+1,100):
# 		if set(factorisation[x]) == set(factorisation[y]): total = total - 1 

# print total