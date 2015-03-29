#1533776805, .05 sec
import time
tm = time.time()

t = [40755]
p = [40755]

#k = 1
c = 143
t_v = 285
p_v = 165
while True:
	
	h = [(2*i*i - i) for i in range(c,c+100)]
	
	while t[-1] < h[-1]:
		t.append((t_v*t_v + t_v)/2)
		#print t_v
		t_v += 1
	
	#print 't:',len(t)
	while p[-1] < h[-1]:
		p.append((3*p_v*p_v - p_v)/2)
		p_v += 1
	
	if len((set(h) & set (t)) & set(p)) != 0:
		#k += 1
		print (set(h) & set (p))
		print time.time()-tm
		# if k == 3:
		# 	break
	t = [t[::-1][0]]
	p = [p[::-1][0]]

	#print t
	c += 100
	#print c

