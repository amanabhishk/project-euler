coins = [1,2,5,10,20,50,100,200]

ways = [1]*200

for i in coins: ways[i-1] = ways[i-1]+1
ways[0] = 1
#print ways
for j in range(1,200): ways[j] = ways[j] + ways[j-1]
print ways
