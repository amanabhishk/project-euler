master = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten', 11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80: 'eighty',90:'ninety',100:'hunderd'}

def number_to_name(n,master):
	
	output = ''
	if n <21:
		output = master[n]
		return output
	k = n
	if n%10 != 0 and not(k%100 < 20 and k%100 > 10 and k>100): #(k%100 < 20 and k%100 > 10 and k>100) checks if 'eleven, twleve' etc have to be used or not
		output = master[n%10]+output
	n = (n - n%10)
	
	if n%100 != 0 and not(k%100 < 20 and k%100 > 10 and k>100):
		output = master[n%100] + output
	


	if n <100:
		return output
	#print k,k%100 < 20 and k%100 > 10 and k>100
	if k%100 < 20 and k%100 > 10 and k>100:
		output = master[k%100]+output 

	n = (n - n%100)
	#print n
	output = master[n/100]+'hundredand'+output  

	return output

j=1
answer = 0
while j<1000:
	print j,number_to_name(j,master)
	answer = answer+len(number_to_name(j,master))
	j = j+1

print answer+11-27 # +11 is for 1000, -27 is for adding useless 'and' in the end of multiples of 100