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

prime = []
i =3
while len(prime) != 10001-1:
	if prime_check(i) == True:
		prime.append(i)
	i = i+2

print prime[len(prime)-2]