#56370, 45228 after removing 2 repeated entries. Run time can be reduced by working on the i, j ranges better. Felt lazy

def pandigital_check(a):
	ref = [0,1,1,1,1,1,1,1,1,1]
	b = [0]*10
	while a > 9:
		
		b[a%10] = b[a%10] + 1
		a = (a - a%10)/10
		# print a
	b[a%10] = b[a%10] + 1
	# print b
	if b == ref:
		return True
	else:
		return False 

ans = 0
for i in range(2,10000):
	for j in range(i, 10000):
		if len(str(i))+len(str(j))+len(str(i*j)) == 9:
			if pandigital_check(int(str(i)+str(j)+str(i*j))) == True:
				print i,j,i*j
				ans = ans + i*j

print ans

#print pandigital_check(987651234)

