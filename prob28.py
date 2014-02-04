matrix=[]
for i in range(1001):
	row=[]
	for j in range(1001):
		row.append(0)
	matrix.append(row)
		
s=(len(matrix))/2
nx=s
ny=s
for i in range(1001*1001):
	matrix[ny][nx]=i+1
	dx=nx-s
	dy=ny-s
	if dx<0:
		dx=-dx
	if dy<0:
		dy=-dy

	if dx<dy:
		if ny>s:
			nx=nx-1
		else:
			nx=nx+1
	elif dy<dx:
		if nx>s:
			ny=ny+1
		else:
			ny=ny-1
	elif nx==ny:
		if nx<=s:
			nx=nx+1
		else:
			nx=nx-1
	elif nx!=ny:
		if ny<=s:
			nx=nx+1
		else:
			ny=ny-1	
sum=0
for i in range(1001):
	sum=sum+matrix[i][i]
	sum=sum+matrix[1000-i][i]
sum=sum-1
print sum

