import time

global start_time
def start():
	global start_time
	#output = ''
	#if t:
	start_time = time.time()
	t = False
	#if not t:

def end():
	#start_time
	output = ''
	run_time = time.time() - start_time
	if int(run_time/3600) != 0:
		#print run_time
		output += str(int(run_time/3600)) + ' h '
		run_time = (run_time - run_time/3600)%3600
	if int(run_time/60) != 0:
		#print run_time
		output += str(int(run_time/60)) + ' min '
		run_time = (run_time - run_time/60)%60
	#print run_time,'jgwe'
	#if run_time > 0:
		#print run_time
		#if int(run_time) == 0:
			# t = True
	output += str(int(run_time)) + ' s '
	run_time = (run_time - int(run_time))
	output += str(int(run_time*1000)) + ' ms '
	#print run_time*1000
	# if t:
	# 	run_time = int((((run_time*1000)%1000)*1000)%1000)
	# 	output += str(int(run_time)) + ' us '
	print 'running time: ',output

# j = time.time()
# start()
# s = sum(x*x*x for x in xrange(10000000))
# print s
# end()
# print time.time()-j