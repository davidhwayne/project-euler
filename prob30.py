list=[]
for i in range(2,400000):
	n=str(i)
	tot=0
	for j in n:
		tot=tot+int(j)**5
	if tot==i:
		list.append(i)

print list
print sum(list)
	
	

