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
primes=primes(2000000)
sum=0
for n in primes:
	sum=sum+n
print sum
