# 73681+1, Very inefficient, 32 min running time.

ways = 0
for x1 in range(0,3):
	for x2 in range(0,5):
		for x3 in range(0,11):
			for x4 in range(0,41):
				for x5 in range(0,101):
					for x6 in range(0,201):
						for x7 in range(0,21):
							if 100*x1 + 50*x2 + 20*x3 +10*x7 +5*x4 + 2*x5 + x6 == 200:
								ways = ways + 1
							# print x1,x2,x3,x4,x5,x6
							# if ways < 500 and ways > 450:
							# 	exit(0)

print ways

# RUN TIME < 1 SEC. STUDY THIS

# target = 200
# coins = [1,2,5,10,20,50,100,200]
# ways = [1]+[0]*target

# for coin in coins:
#   for i in range(coin, target+1):
#     ways[i] += ways[i-coin]
 
# print "Answer to PE31 = ", ways[target]