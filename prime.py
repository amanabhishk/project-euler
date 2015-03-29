def prime_check(n):
	total = True
	i = 2
	while True:
		total = total and n%i != 0
		i = i+1
		if i == n/2:
			break
		if total == False:
			return False
	return True

# prime = []
i = 3
k = 1
while k != 5:
	if prime_check(i) == True:
		k = k+1
	i = i+2

# print prime
print i-2
