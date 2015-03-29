#import prob82c.py

grid_original = [[131	,673	,234,	103	,18],[201	,96	,342	,965	,150],[630,	803,	746,	422,	111],[537,	699	,497	,121	,956],[805	,732,	524	,37	,331]]
grid = [[131	,673	,234,	103	,18],[201	,96	,342	,965	,150],[630,	803,	746,	422,	111],[537,	699	,497	,121	,956],[805	,732,	524	,37	,331]]

def reset(grid):
	grid = [[131	,673	,234,	103	,18],[201	,96	,342	,965	,150],[630,	803,	746,	422,	111],[537,	699	,497	,121	,956],[805	,732,	524	,37	,331]]
def set_1st_column(grid_original,grid,a): #Dont check,works fine
	#grid = list(grid_original)
	for x in xrange(a+1,len(grid)):
		# print grid[x-1][0],grid[x][0]
		grid[x][0] = grid[x-1][0] + grid[x][0]
	for x in xrange(1, a+1):
		#print a-x+1 , a-x+2 
		grid[a-x][0] = grid[a-x][0] + grid[a-x+1][0]
	return grid 
	#print grid[0],'\n',grid[1],'\n',grid[2],'\n',grid[3],'\n',grid[4]


def set_nth_column(grid_original,grid,n): #Does what it says, but that is wrong
	
	for x in xrange(1,len(grid_original)-1):
		grid[x][n] = grid_original[x][n] + min(grid[x][n-1],grid_original[x+1][n],grid_original[x-1][n])
	grid[0][n] = grid[0][n] + min(grid[0][n-1],grid_original[1][n])
	grid[len(grid)-1][n] = grid[len(grid)-1][n] + min(grid[len(grid)-1][n-1],grid_original[len(grid)-2][n])
	# print 'result'
	# print grid[0],'\n',grid[1],'\n',grid[2],'\n',grid[3],'\n',grid[4]	
	return grid

ans = []
for a in xrange(1,2):#len(grid)):
	set_1st_column(grid_original,grid,a)
	for n in xrange(1,len(grid)):
		set_nth_column(grid_original,grid,n)

	m = 1000000
	for x in xrange(0,len(grid)):
		m = min(m,grid[x][len(grid)-1])
	ans.append(m)
print grid[0],'\n',grid[1],'\n',grid[2],'\n',grid[3],'\n',grid[4]	
print min(ans)
