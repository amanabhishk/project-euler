def days(i):
	if i%100 == 0:
		if i%400 == 0: return 366
		else: return 365
	elif i%4 == 0: return 366
	else: return 365

al = [True]+[False]*30  +[True]+[False]*28  +[True]+[False]*30  +[True]+[False]*29  +[True]+[False]*30  +[True]+[False]*29  +[True]+[False]*30  +[True]+[False]*30  +[True]+[False]*29  +[True]+[False]*30  +[True]+[False]*29  +[True]+[False]*30
an = [True]+[False]*30  +[True]+[False]*27  +[True]+[False]*30  +[True]+[False]*29  +[True]+[False]*30  +[True]+[False]*29  +[True]+[False]*30  +[True]+[False]*30  +[True]+[False]*29  +[True]+[False]*30  +[True]+[False]*29  +[True]+[False]*30

calender = []

for x in range(1901,2001):
	if days(x) == 365: calender += an
	elif days(x) == 366: calender += al
	else: print 'Error'

ans = 0
for y in xrange(5,len(calender),7):
	if calender[y]: 
		ans += 1

print ans 