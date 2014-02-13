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

primes=primes(1000000)

def istrunc(n):
	global primes
	p=str(n)
	for j in p[1:]:
		if j=='0' or j=='2' or j=='4' or j=='5' or j=='6' or j=='8':
			return False
			break
	for k in range(len(p)):
		ltr=int(p[k:])
		rtr=int(p[:len(p)-k])
		i=0
		while primes[i]<int(ltr) and i<len(primes)-1:
			i=i+1
		if primes[i]!=int(ltr):
			return False
			break
		i=0
		while primes[i]<int(rtr) and i<len(primes)-1:
			i=i+1
		if primes[i]!=int(rtr):
			return False
			break
	else:
		return True

truncs=[]
i=4
count=0
while count<11:
	if istrunc(primes[i]):
		print primes[i]
		truncs.append(primes[i])
		count+=1
	i+=1
print sum(truncs)
	


