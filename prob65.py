#272, 0.0002 sec
import time
t = time.time()

s = []
i = 2
while len(s)<99:
	s += [1,i,1]
	i += 2


s = [2]+s
print s,len(s)

b = 1
s = s[::-1]


# for i in range(1,10):
a = s[0]
b = 1
for x in s[1:len(s)]:
	A =  x*a+b
	B =	 a
	a = A
	b = B

	i += 1
ans = 0
while a>9:
	ans += a%10
	a = (a-a%10)/10

print ans+a
print time.time()-t