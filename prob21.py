def isam(n):
	divisors=[]
	for j in range(1,n):
		if n%j==0:
			divisors.append(j)
	sumdiv=sum(divisors)
	if n!=sumdiv:
		otherdivs=[]
		for k in range(1,sumdiv):
			if sumdiv%k==0:
				otherdivs.append(k)
		othersum=sum(otherdivs)
		if othersum==n:
			return True
		else:
			return False
	else:
		return False
ams=[]
for i in range(1,10000):
	if isam(i):
		ams.append(i)
print ams
print sum(ams)
