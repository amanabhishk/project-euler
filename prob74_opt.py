#generating a list of all possible permuations of numbers. Its better than checking a million of them later
ref = []
def permutations_check(ref, n):
	digits = []
	while n > 9:
		digits.append(n%10)
		n = (n-n%10)/10
	digits.append(n)
	#print digits
	digits = sorted(digits)
	#print digits
	ref.append(digits)
	# if (len(list(set(ref))) != len(ref)):
	# 	return False
	# else: return True

for x in xrange(10,10**6):
	ref = sorted(ref)
	permutations_check(ref,x)

ref = sorted(ref)
ref1 = ref[0]
total = 1
for y in xrange(1,len(ref)):
	if ref[y] != ref[y-1]:
		#print ref[y]
		total = total + 1

print total
print ref1


#print sorted(ref)