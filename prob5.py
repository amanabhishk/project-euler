k = 40

while True:
	ans = True
	print k
	for i in range(2,21):
		
		ans = ans and k%i == 0
		if ans == False:
			break
	if ans == True:
		print k
		break
	k = k+20