
#from math import log
import time
#from decimal import *
t = time.time()
#getcontext().prec = 40
# ctx = Context(prec=20)
# two = Decimal(2)
#ctx.divide(ctx.power(a, Decimal(b)).ln(ctx), a.ln(ctx))

c = 100
data = [a**b for a in range(2,c+1) for b in range(2,c+1)]
#print sorted(data[1::50])
print len(set(data))
print time.time()-t