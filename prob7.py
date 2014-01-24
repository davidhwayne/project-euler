primelist=[2]
i=1
while i>-1:
	i=i+1
	if len(primelist)<10002:
		for k in primelist:
			if i%k==0:
				break
		else:	
			primelist.append(i)	
	else:
		break
print primelist[10000]
