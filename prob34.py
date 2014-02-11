def factorial(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	return fact
		

list=[]
for i in range(3,300000):
	n=str(i)
	tot=0
	for j in n:
		tot=tot+factorial(int(j))
	if tot==i:
		list.append(i)

print list
print sum(list)
	
