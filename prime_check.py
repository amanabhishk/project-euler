def prime_check(n):
	total = True
	if n%2 == 0:
		return False
	i = 3
	while True:
		total = total and n%i != 0
		i = i+2
		if i >= n/2:
			break
		if total == False:
			return False
	return True