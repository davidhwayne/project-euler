def primeandoddcomps(n):
	sieve=[True]*n
	for i in range(2,n):
		if sieve[i]:
			for j in range(2*i,n,i):
				sieve[j]=False
	primelistplus=[]
 	complist=[]
	n=0
	for boo in sieve:
		if boo:
			primelistplus.append(n)
		elif n%2==1:
			complist.append(n)
		n=n+1
	primelist=primelistplus[2:]		
	return [primelist,complist]

print 'Generating primes and odd composites...'
nums=primeandoddcomps(10000)
primes=nums[0]
comps=nums[1]
print 'Checking...'
first=0
for n in comps:
	next=False
	i=1
	while primes[i]<n and not next:
		for j in range(1,n):
			if primes[i]+2*j**2==n:
				next=True
				break
		i+=1
	if not next:
		first=n
		break
print n

	



 
