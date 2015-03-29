#9110846700, .03 sec
import time
t = time.time()
data = sum([(i**i)%(10**10) for i in range(1,1001)])

#s = sum[(n%(10**10)) for n in data]

print data%10**10
print time.time()-t