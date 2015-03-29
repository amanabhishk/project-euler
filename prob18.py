grid = [75],[95+75,64+75],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[04,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

# max_sum = 0

# for a1 in range(0, len(grid[1])):
	
# 	for a2 in range(a1, a1+2):
		
# 		for a3 in range(a2,a2 + 2):
			
# 			for a4 in range(a3,a3 + 2):
				
# 				for a5 in range(a4,a4 + 2):
					
# 					for a6 in range(a5,a5 + 2):
						
# 						for a7 in range(a6,a6 + 2):
							
# 							for a8 in range(a7,a7 + 2):
								 
# 								for a9 in range(a8,a8 + 2):
									
# 									for a10 in range(a9,a9 + 2):
										 
# 										for a11 in range(a10,a10 + 2):
											 
# 											for a12 in range(a11,a11 + 2):
												
# 												for a13 in range(a12,a12 + 2):
													 
# 													for a14 in range(a13,a13 + 2):
# 														s = 75 + grid[13][a13]+grid[14][a14]+ grid[12][a12]+grid[1][a1]+ grid[2][a2]+ grid[3][a3]+ grid[4][a4]+ grid[5][a5]+ grid[6][a6] + grid[7][a7]+ grid[8][a8]+ grid[9][a9]+ grid[10][a10]+ grid[11][a11]
# 														if max_sum < s:
# 															max_sum = s


# print max_sum

for j in xrange(2,15):
	for i in xrange(0,len(grid[j])):
		if i == 0: grid[j][i] = grid [j][i] + grid[j-1][i]
		elif i == len(grid[j]) - 1: grid[j][i] = grid [j][i] + grid[j-1][i-1]
		else: grid[j][i] = grid [j][i] + max(grid[j-1][i], grid[j-1][i-1])

print max(grid[14])