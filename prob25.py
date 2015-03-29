i = 2
a = 1
b = 1
s = 0
for i in range(0,100000):
	print 'k'
while True:
	c = a + b
	if c >= 4000000:
		print s
		exit(0)
	if c%2 == 0:
		s = s+c
	a = b
	b = c

print digit_count(1000)
