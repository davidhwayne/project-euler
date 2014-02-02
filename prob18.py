tri=[]
tri.append([75])
tri.append([95, 64])
tri.append([17, 47, 82])
tri.append([18, 35, 87, 10])
tri.append([20, 04, 82, 47, 65])
tri.append([19, 01, 23, 75, 03, 34])
tri.append([88, 02, 77, 73, 07, 63, 67])
tri.append([99, 65, 04, 28, 06, 16, 70, 92])
tri.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
tri.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
tri.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
tri.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
tri.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
tri.append([63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
tri.append([04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23])

#Find max by summing through the triangle backwards.
for row in range(14,0,-1):
	partsum=tri
	for col in range(len(partsum[row-1])):
		if partsum[row][col]>partsum[row][col+1]:
			partsum[row-1][col]=partsum[row-1][col]+partsum[row][col]
		else:
			partsum[row-1][col]=partsum[row-1][col]+partsum[row][col+1]
largestsum=partsum[0][0]
print largestsum
	

