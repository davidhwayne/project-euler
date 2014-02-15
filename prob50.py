def primes(n):
	sieve=[True]*n
	for i in range(2,n):
		if sieve[i]:
			for j in range(2*i,n,i):
				sieve[j]=False 
	primelistplus=[]
	n=0
	for boo in sieve:
		if boo:
			primelistplus.append(n)
		n=n+1
	primelist=primelistplus[2:]
			
	return primelist

plist=primes(1000000)
top=0
k=len(plist)-1
i=0
while plist[i]<plist[-1]:
	count=0
	sum=0
	j=0
	while sum<1000000 and plist[i+j]<plist[-1]:
		count+=1
		sum=sum+plist[i+j]
		j+=1
	j=j-1
	while sum not in plist and j>=0:
		sum=sum-plist[i+j]
		count=count-1
		j=j-1
	if count>top:
		top=count
		topsum=sum
	if sum-plist[i]+plist[i+j+1]>1000000:
		break	
	i+=1
print topsum
print top

