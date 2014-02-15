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

start=len(primes(1000))
plist=primes(10000)[start:]
psort=[]
for p in plist:
	ps=list(str(p))
	ps.sort()
	psort.append([p,''.join(ps)])
psorted=sorted(psort, key=lambda prime: prime[1])
i=0

for i in range(len(psorted)-1):
	dif=0
	permuts=[]
	while psorted[i][1]==psorted[i+1][1]:
		if dif==0:
			dif=psorted[i+1][0]-psorted[i][0]
			permuts.append(psorted[i][0])
			permuts.append(psorted[i+1][0])
		elif dif!=psorted[i+1][0]-psorted[i][0]:
			break
		else:
			permuts.append(psorted[i+1][0])
		i+=1
	else:
		if len(permuts)>2:
			print permuts
#This code does not actually output the example solution because it only checks the current index with previous one, not with all of the previous primes in the permutation group.  
