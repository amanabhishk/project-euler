c = 2**15
answer = 0
while True:
	answer = answer + c%10
	c = (c-c%10)/10
	if c <10:

		print answer+c
		break