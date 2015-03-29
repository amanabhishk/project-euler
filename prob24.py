import math
c = 10**6
a = [None]*9
print c
for i in range(0,9):
	a[i] = (c/math.factorial(10-i-1))+1
	c = c - (a[i]-1)*math.factorial(10-i-1)
	print c

print a

s = 0
for i in range(0,9):
	s = s+ a[i]*math.factorial(10-1-i)

print s



# c = 23
# a = [None]*3
# #print c
# for i in range(0,3):
# 	a[i] = (c/math.factorial(4-i-1))+1
# 	print (a[i])*math.factorial(4-i-1) > c
# 	c = c - (a[i]-1)*math.factorial(4-i-1)
# 	print c

# print a