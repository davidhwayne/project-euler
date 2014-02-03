top=0
current=0
for i in range(999,0,-1):
	count=0
	remainders=[]
	q=1
	while 1>0:
		while q<i:
			q=q*10
		if q%i==0:
			count=0
			break
		elif q%i in remainders:
			break
		else:
			q=q%i
			remainders.append(q)
			count+=1
	if top<count:
		current=i
		top=count
print current
