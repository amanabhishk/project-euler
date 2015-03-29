#443839
def power_sum(n):
	output = 0
	while n > 9:
		output = output+(n%10)**5
		n = (n-n%10)/10
	output = output+(n%10)**5
	return output



i = 2
ans = 0 
while i < 10**7:
	if power_sum(i) == i:
		print i
		ans = ans + i

	i = i+1

print ans
