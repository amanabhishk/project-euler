#669171001
n = []
for i in range(2,1001**2+1):
	n.append(i)

#print n
i = 2
ans = 1
index = 0
c = 0
while index != 1002001:
	for k in range(1,5):
		index = i*k+1+c 
		 
		ans = ans + index
		print index
		# if index == 1002001:
			
		# 	break

	c = index-1
	i = i+2

print 'ans', ans


