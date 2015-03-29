def digit_count(n):
	k = 1
	j = n
	while j >= 10:
		j = j/10
		k = k+1
	return k 

def number_to_list(n): 
	k = digit_count(n)
	output = [0]*k
	output2 = [0]*k
	digit = n
	d = 10
	for i in range(0,k):
		output[i] = digit%d
		output2[k-1-i] = digit%d
		digit = digit - (digit%d)
		digit = digit/10
	return output2 == output
k =0
answer = []
for i in range(100,1000):
	for j in range(100,1000):
		k = j*i
		if number_to_list(k) == True:
			if i*j > 900000:
				answer.append(j*i)
				# print k
		# else:
		# 	continue
	
print answer