def digitcancel(m,n):	
	ms=str(m)
	ns=str(n)
	for x in ms:
		for y in ns:
			if x==y and x!=0:
				newms=ms.replace(x,"",1)
				newns=ns.replace(y,"",1)
				newm=int(newms)
				newn=int(newns)
				if newm==0 or newn==0:
					return 1
					break
				return float(newm)/newn
				break
	else:
		return 1 
		

fractions=[]
for i in range(10,100):
	for j in range(i+1,100):
		frac=float(i)/j
		if frac==digitcancel(i,j) and str(i)[1]!='0':
			fractions.append((i,j))
		
print fractions
